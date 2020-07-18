# 获取所有样式
import os

dirPath = "./highlight/styles"
for i,j,k in os.walk(dirPath):
    for f in k:
        if ".css" in f:
            name=f.replace(".css","")
            print("<option value=\"" + name + "\">" + name + "</option>")
