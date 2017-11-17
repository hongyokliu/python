
import urllib2
 
req = urllib2.Request('http://blog.csdn.net/cqcre1')#在csdn后面随便加什么，运行后就是URL error                                                 
try:                                                #在cqcre后面随便加什么，运行后就是http error，出来后的是错误原因
    urllib2.urlopen(req)
except urllib2.URLError, e:
    if hasattr(e,"reason"):
        print e.reason
else:
    print "OK"
