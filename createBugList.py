# coding:utf-8
import pygsheets

# client = pygsheets.authorize(service_file = "googleAPI.json")
# 打开谷歌表格testPygSheets
# sh = client.open('4.0插件bug分类')
# 获取表格中的而第一张工作表
# wks = sh.sheet1
# 更新A1数据
# wks.update_value('A2', "我是元素A2")

from selenium import webdriver
import time
import re

# 打开网页
from selenium.webdriver.common.by import By


def get_link_list(url) -> list:
    opt = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=opt)
    driver.get(url)
    driver.maximize_window()
    time.sleep(3)

    # 登陆

    driver.find_element("id", "login-form-username").send_keys("liqi")
    driver.find_element("id", "login-form-password").send_keys("liqiliqi")
    driver.find_element("id", "login-form-submit").click()

    time.sleep(3)

    # 点击"更多"按钮
    button = driver.find_element("id", "show-more-links-link")
    driver.execute_script("arguments[0].click();", button)
    time.sleep(2)

    a = driver.find_elements(By.CLASS_NAME, "link-content")
    list = []
    for i in a:
        b = i.find_element(By.TAG_NAME, "span")
        list.append(b.text)
    list.sort()
    return list


# 插入文档
def insert() -> None:
    client = pygsheets.authorize(service_file="googleAPI.json")
    # 打开谷歌表格testPygSheets
    sh = client.open('4.0插件bug分类')

    # 获取表格中的第一张工作表
    wks = sh.worksheet_by_title("Sheet1")
    # 清除老数据
    wks.clear()
    # 写标题

    wks.update_value('A1', "链接")
    wks.update_value('B1', "bug等级")
    wks.update_value('C1', "简介")

    cellNum = 2
    for i in list_all:
        if (('p' not in i) and ('P' not in i)):
            continue
        listTmp = i.split()
        if (len(listTmp) == 2):
            wks.update_value('A' + str(cellNum), listTmp[0])
            wks.update_value('B' + str(cellNum), listTmp[1])
            cellNum = cellNum + 1
        else:
            wks.update_value('A' + str(cellNum), listTmp[0])
            wks.update_value('B' + str(cellNum), listTmp[1])
            wks.update_value('C' + str(cellNum), listTmp[2])
            cellNum = cellNum + 1


if __name__ == '__main__':
    list_966 = get_link_list('http://39.105.160.65:8080/browse/LINK-966')
    list_1025 = get_link_list('http://39.105.160.65:8080/browse/LINK-1025')
    list_all = list_966 + list_1025
    list_all = list(set(list_all))
    list_all.sort()
    insert()
