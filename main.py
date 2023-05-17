# - * - coding: utf - 8 -*-
#
# 作者：田丰(FontTian)
# 创建时间:'2017/7/17'
# 邮箱：fonttian@Gmaill.com
# CSDN：http://blog.csdn.net/fontthrone
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
import socket
import time
import re
import random

# 在这里填写你要访问的博客地址
# blog_url = [
#     'https://blog.csdn.net/shdabai/article/details/119277588',
#     'https://blog.csdn.net/shdabai/article/details/130505653',
#     'https://blog.csdn.net/shdabai/article/details/130500320',
#     'https://blog.csdn.net/shdabai/article/details/130284750',
#     'https://blog.csdn.net/shdabai/article/details/130219663',
#     'https://blog.csdn.net/shdabai/article/details/130158593',
#     'https://blog.csdn.net/shdabai/article/details/118224046',
#     'https://blog.csdn.net/shdabai/article/details/118224801',
#     'https://blog.csdn.net/shdabai/article/details/130219663',
#     'https://blog.csdn.net/shdabai/article/details/130158593',
#     'https://blog.csdn.net/shdabai/article/details/126034615',
#     'https://blog.csdn.net/shdabai/article/details/118552162',
#     'https://blog.csdn.net/shdabai/article/details/112470240',
#     'https://blog.csdn.net/shdabai/article/details/130171126',
#     'https://blog.csdn.net/shdabai/article/details/118362892',
#     'https://blog.csdn.net/SHdabai/article/details/118054216',
#     'https://blog.csdn.net/SHdabai/article/details/119144623',
#     'https://blog.csdn.net/SHdabai/article/details/119277588',
#     'https://blog.csdn.net/shdabai/article/details/130579622',
#     'https://blog.csdn.net/shdabai/article/details/130579010',
#     'https://blog.csdn.net/shdabai/article/details/130597716',
#     'https://blog.csdn.net/SHdabai/article/details/130635681'
# ]



blog_url = [

    'https://blog.csdn.net/shdabai/article/details/130579622',
    'https://blog.csdn.net/shdabai/article/details/130597716',
    'https://blog.csdn.net/SHdabai/article/details/130635681',
    'https://blog.csdn.net/shdabai/article/details/130505653',
    'https://blog.csdn.net/shdabai/article/details/130658851',
    'https://blog.csdn.net/shdabai/article/details/130680560'
]
class CSDN(object):
    def __init__(self, blog_url=blog_url, csdn_url="http://blog.csdn.net/fontthrone"):
        self.blog_url = blog_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'gzip',
            'Connection': 'close',
            'Referer': None
        }

    def openCsdn(self):
        req = urllib2.Request(self.csdn_url, headers=self.headers)
        response = urllib2.urlopen(req)
        thePage = response.read()
        response.close()
        pattern = "访问：<span>(\d+)次</span>"
        number = ''.join(re.findall(pattern, thePage))
        return number

    def openBlog(self, link='http://blog.csdn.net/fontthrone/article/details/70556507', timeout=100, sleepTime=65,
                 maxTryNum=1):
        tries = 0
        maxNum = 0
        # for tries in range(maxTryNum):
        while tries < maxTryNum:
            try:
                socket.setdefaulttimeout
                req = urllib2.Request(link, None, self.headers)
                resp = urllib2.urlopen(req, None, timeout)
                html = resp.read()
                print "Success!\t",
                print "Rest ", sleepTime, " seconds to continue...\n"
                tries += 1
                time.sleep(sleepTime)
            except:
                if tries < (maxTryNum):
                    maxNum += 1
                    continue
                else:
                    print("Has tried %d times to access blog link %s, all failed!", maxNum, link)
                    break

    def start(self, maxTime=100, blOpenCsdn=False, sleepTimeStart=60, sleepTimeEnd=75, timeout=100):
        for i in range(maxTime * len(self.blog_url)):
            randomLink = random.choice(self.blog_url)
            print 'This tinme the random_blog link is ', randomLink
            if blOpenCsdn == True:
                self.openCsdn()
            self.openBlog(link=randomLink, sleepTime=random.uniform(sleepTimeStart, sleepTimeEnd), timeout=timeout)
            print "Now is " + str(i + 1) + " times to acess blog link\n"



csdn = CSDN()
inputMaxTime = input(u'请输入列表访问次数\n')

print "准开始启动"
# time.sleep(21600)

print "启动成功"

csdn.start(maxTime=int(inputMaxTime))