import urllib2
 
req = urllib2.Request('http://blog.csdn1.net/cqcre1')#在csdn后面随便加什么，运行后就是URL error
try:                                                 #在cqcre后面随便加什么，运行后就是http error，出来后的是错误代号
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:
    print e.reason
else:
    print "OK"
