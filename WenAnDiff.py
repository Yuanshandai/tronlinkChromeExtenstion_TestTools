"""
=== Excel操作 ===
=== CaseData: 保存数据类 ===
=== ExcelHandle: 处理Excel文件 ===
"""
import os
import openpyxl, json


class CaseData(object):
    pass


class ExcelHandle(object):
    """处理Excel文件"""

    def __init__(self, file_name, sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name

    def __open(self):
        self.wb = openpyxl.load_workbook(self.file_name)
        self.sh = self.wb[self.sheet_name]

    def get_data_dict(self) -> dict:
        """读取数据存储在字典中"""
        self.__open()
        rows = list(self.sh.rows)
        return [dict(zip([i.value for i in rows[0]], [r.value for r in row]))
                for row in rows[1:]]

    def get_data_obj(self) -> list:
        """读取数据存储在类中"""
        self.__open()
        rows = list(self.sh.rows)
        # 定义用例列表，用来存放用例类列表
        cases = []
        # 遍历用例数据行
        for row in rows[1:]:
            # 把每一行的数据通过zip进行打包，然后转成字典，存入到用例数据列表中
            case = dict(zip([i.value for i in rows[0]], [r.value for r in row]))
            # 定义一个用例存放类对象
            case_obj = CaseData()
            for k, v in case.items():
                # 通过setattr()给对象添加属性
                setattr(case_obj, k, v)
            # 把对象添加到列表中
            cases.append(case_obj)
        return cases


if __name__ == '__main__':
    file = "/Users/liqi/Desktop/文档/产品文档.xlsx"
    eh = ExcelHandle(file, "仅V4")
    data = eh.get_data_dict()  # list类型
    # print(data)
    with open("/Users/liqi/Documents/tronlink-extension-pro/src/i18n/en.json", 'r') as f:
        load_dict_en = json.load(f)
    print(load_dict_en)
    with open("/Users/liqi/Documents/tronlink-extension-pro/src/i18n/ja.json", 'r') as f:
        load_dict_ja = json.load(f)
    print(load_dict_ja)
    with open("/Users/liqi/Documents/tronlink-extension-pro/src/i18n/zh_CN.json", 'r') as f:
        load_dict_zh = json.load(f)

print(load_dict_zh)
list = list(load_dict_zh.keys())
print(list)
dict_zh = {}
dict_en = {}
dict_jp = {}
for i in list:
    # 遍历excel中的key,写三个dict(中，英，日)
    for dict in data:
        if (dict['key'] == i):
            dict_zh[i] = dict['zh']
            dict_en[i] = dict['en']
            dict_jp[i] = dict['jp']

print('对比中文文案结果:')
print(load_dict_zh == dict_zh)

# differ = set(load_dict_zh.items()) ^ set(dict_zh.items())
# print(differ)
diff = load_dict_zh.keys() & dict_zh
diff_vals = [(k, load_dict_zh[k], dict_zh[k]) for k in diff if load_dict_zh[k] != dict_zh[k]]
print(diff_vals)
print('对比英文文案结果:')
print(load_dict_en == dict_en)
# differ = set(load_dict_zh.items()) ^ set(dict_zh.items())
# print(differ)
diff = load_dict_en.keys() & dict_en
diff_vals = [(k, load_dict_en[k], dict_en[k]) for k in diff if load_dict_en[k] != dict_en[k]]
print(diff_vals)
print('对比日文文案结果:')
print(load_dict_ja == dict_jp)
# differ = set(load_dict_ja.items()) ^ set(dict_ja.items())
# print(differ)
diff = load_dict_ja.keys() & dict_jp
diff_vals = [(k, load_dict_ja[k], dict_jp[k]) for k in diff if load_dict_ja[k] != dict_jp[k]]
print(diff_vals)
