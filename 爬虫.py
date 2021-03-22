import requests
from lxml import etree


##初始化url
url="http://www.51testing.com/html/90/category-catid-90.html"
file=open("potato.txt",'w')
#发送请求
response=requests.get(url=url)
print(response)
#获取网站的编码
print(response.apparent_encoding)
#设置编码格式

response.encoding='gbk'
content=response.text
#将页面信息转换为dom格式
document=etree.HTML(content)
#输出
print(document)
##抓取元素/html/body/div[6]/div[2]/div/div[3]/p   /html/body/div[6]/div[1]/div[3]/p /html/body/div[6]/div[1]/div[4]/p
for j in range(2,4):
    for i in range(1,11):
        ele=document.xpath("/html/body/div[6]/div[1]/div["+str(i)+"]/p/text()")[0]
        print(ele)
        print()
        ss=''.join(ele.split())
        file.write(ss+"\n")


    ##初始化url
    url="http://www.51testing.com/html/90/category-catid-90-page-2.html"
    #发送请求
    response=requests.get(url=url)
    print(response)
    #获取网站的编码
    print(response.apparent_encoding)
    #设置编码格式

    response.encoding='gbk'
    content=response.text
    #将页面信息转换为dom格式
    document=etree.HTML(content)
    #输出
    print(document)
file.close()
    ##抓取元素/html/body/div[6]/div[2]/div/div[3]/p   /html/body/div[6]/div[1]/div[3]/p /html/body/div[6]/div[1]/div[4]/p
    # for i in range(1,11):
    #     ele=document.xpath("/html/body/div[6]/div[1]/div["+str(i)+"]/p/text()")[0]
    #     print(ele)
#     print()