

import os,json,re

g = os.walk(r"/Users/liqi/Documents/tronlink-extension-pro/src")

file_path=[]
for path,dir_list,file_list in g:
    for file_name in file_list:
        file_path.append(os.path.join(path, file_name))

#print(file_path)
# 匹配规则 id="",引号中间的内容
pattern = re.compile(r'[\"](.*?)[\"]')
pattern1 = re.compile(r'[\'](.*?)[\']')
pattern2 = re.compile("^[A-Za-z0-9_.]*$")
# 结果集
result = []

for path in file_path:
    if ((path != "/Users/liqi/Documents/tronlink-extension-pro/src/i18n/en.json") and (
        path != "/Users/liqi/Documents/tronlink-extension-pro/src/i18n/ja.json") and (
        path != "/Users/liqi/Documents/tronlink-extension-pro/src/i18n/zh_CN.json")):
      # print(path)
      with open(file=path, mode='r',encoding="utf8", errors='ignore') as f:
        contents = f.read()
        # print(contents)
        tempList = pattern.findall(contents)
        tempList1 = pattern1.findall(contents)


        result = result+tempList+tempList1
# 去掉筛选出来的小写的字符串
result1=[]
#for temp in result:
#    if((temp.isupper() and  "." in temp and "_" in temp) or (temp.isupper() and  "." in temp ) or (temp.isupper() and  "." in temp and "_" in temp and  any(chr.isdigit() for chr in temp) ) ):
#        if((" " not in temp) and (("*") not in temp) and (("&") not in temp) and ((("}") not in temp))):
#           result1.append(temp)
#for temp in result:
#    if(re.match("^[A-Z0-9_.]*$",temp)):
#           result1.append(temp)

for temp in result:
    if(( "." in temp and "_" in temp) or (  "." in temp ) or (  "." in temp and "_" in temp and  any(chr.isdigit() for chr in temp) ) ):
        if( (re.match("^[A-Z0-9_.]*$", temp)) or (re.match("^[A-Z.]*$", temp)) or (re.match("^[A-Z_.]*$", temp)) or (re.match("^[A-Za-z.]*$", temp))):
            if(((re.match("^[0-9.]*$", temp)) is  None) or ((re.match("^[a-z.]*$", temp)) is not None)):
               result1.append(temp)
print("key是：")
#去重
print(set(result1))
print(len(set(result1)))

with open("/Users/liqi/Documents/tronlink-extension-pro/src/i18n/zh_CN.json", 'r') as f:
    load_dict_zh = json.load(f)
listFromCode = list(load_dict_zh.keys())

print (list(set(listFromCode).difference(set(result1)))) #

print(len(list(set(listFromCode).difference(set(result1)))))




