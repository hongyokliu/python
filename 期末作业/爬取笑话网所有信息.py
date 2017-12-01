#-*- coding:utf-8 -*-
import urllib
import urllib2
import re

for i in range(1,100):
 i=1
 url = 'http://www.xiaohua.com/index/index/type/0/p/'+ str(i) +'.html'
print url
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')

    pattern = re.compile('<div class="one-cont-font clearfix">.*?<em>.*?<i>(.*?)</i>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        print item
        print "----------------------------------------------------------"


    pattern = re.compile('<div class="one-cont-title clearfix">.*?<a.*?>(.*?)</a>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        print item
        print "------------------------------------------------------------"


    pattern = re.compile('<div class="img-1">(.*?)</div>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        print item
        print "----------------------------------------------------------"


    pattern = re.compile('<span sid=.*?".*?>(.*?)</span>.*?<span sid=.*?".*?>(.*?)</span>.*?<span sid=.*?".*?>(.*?)</span>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        print item
        print "----------------------------------------------------------"

        
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

