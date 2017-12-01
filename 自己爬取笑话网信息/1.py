#-*- coding:utf-8 -*-
import urllib
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

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
    

    all_pattern =re.compile('<div class="one-cont-font clearfix">.*?<em>.*?<i>(.*?)</i>.*?<div class="one-cont-title clearfix">.*?<a.*?>(.*?)</a>.*?<div class="img-1">(.*?)</div>.*?<span sid=.*?".*?>(.*?)</span>.*?<span sid=.*?".*?>(.*?)</span>.*?<span sid=.*?".*?>(.*?)</span>',re.S)
    all_list =re.findall(all_pattern,content)
    for item in all_list:
        print "作者："+ item[0]
        print "内容："+ item[1]
        print "图片："+ item[2].strip()
        print "点赞数不喜欢数收藏数："+item[3]

        input = raw_input()
        if input ==" ":
            print "nextpage:"
            continue
        elif input =="Q":
            break
        
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

