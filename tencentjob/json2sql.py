#! python3
#coding:utf-8
import json


data = []
with open('C:/Users/97390/PycharmProjects/tencentjob/tencent.json', encoding="utf-8") as f:  #open() 函数在python2 中是没有encoding这个参数的
    for line in f:
        line = line.encode('utf-8','ignore')
        json_line = json.loads(line)
        data.append(json_line)

str = "\r\n"
for item in data:
    sl = []
    i = 0
    for  v in item.values():
        s = ''.join(v)     #把value值从列表转化为字符串
        sl.append(s)
        i = i + 1
    str = str + "insert into tencent(name,catalog,workLocation,recruitNumber,detailLink,publishTime) values "   # 因为多了一列id自增，所以要把这六列明确写出来，如果省掉会报错，7列而只有6个参数
    str = str + "('%s','%s','%s','%s','%s','%s');\r\n"   % (sl[1], sl[4], sl[5], sl[0], sl[2], sl[3])   # %s 要让单引号''包起来，否则sql语句遇到里面的标点符号时识别不出

with open("scrapy crawl tencent.sql", 'w',encoding='utf-8') as file_object:  # encoding='utf-8' 很重要
    file_object.writelines(str)
    file_object.close()

print("success")
