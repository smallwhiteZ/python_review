'''
目的：使用爬虫爬数据

需求：在豆瓣中任意找到一本书，
1。抓取其中的一页的短评，
2。并将文字短评抽取后并输出，
3。再抽取出其中的评分并且计算其总分

解题思路：

1。使用什么框架？   request

2。使用框架下的什么函数进行获取相关消息？

    get函数

但是之后怎么处理就不清楚了？？


参考答案：

1。使用了re ，requests，beautiSoup框架

2。调用了   re的compile函数   从而返回一个经过正则表达式的对象
                findall函数，传入正则表达式之后完成查找

            requests的get函数  从而返回网页开发工具的全部内容

            使用BeautifulSoup的框架来创建一个对象soup（包含了特定格式）
            再调用这个对象的find_all函数


'''

import requests as rq
import re
from bs4 import BeautifulSoup

#目标url
desurl = 'https://book.douban.com/subject/27194720/comments/'

contents = rq.get(desurl)    #获取网页里的内容

#这一句不是很懂意思
soup = BeautifulSoup(contents.text, 'lxml')
#特定文本格式下的查找
pattern = soup.find_all('span', 'short')


for item in pattern:
    print(item.string+'\n\n')

#re.compile 查找符合正则表达式下的文本
pattern_s = re.compile('<span class="user-stars allstar(.*?) rating"')


#正则表达式下的查找
p = re.findall(pattern_s, contents.text)

score = 0
for i in p:
    score = score + int(i)

print(score)