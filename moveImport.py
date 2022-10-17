import re
import os

# 扫描文件 找到所有的import

g = os.walk(r"/Users/liqi/Desktop/1111/test-新的0915/tronlink-extension/packages")

file_path = []
for path, dir_list, file_list in g:
    for file_name in file_list:
        file_path.append(os.path.join(path, file_name))

#print(file_path)

for i in file_path:
    tempfile = i
    if "node_modules" in i:
        continue

    if ".js" in i:
        f = open(
            i,
            "r")

        originFile = f.read()

        pattern = re.compile(r'import .*;')

        list1 = pattern.findall(originFile)
        #print(list1)

        targerResult = ""

        for i in list1:
           targerResult = targerResult + i
           #print(targerResult)

        # 整体替换文件为修改后的文件

        afterReplaceFile = originFile.replace(targerResult, "")


        resultFile = targerResult + afterReplaceFile
       # print(22222222222222222)
       # print(resultFile)
        with open(tempfile, "w") as f:
            f.write(resultFile)
            #f.flush()
