
import urllib2
 
req = urllib2.Request('http://blog.csdn.net/cqcre1')#��csdn��������ʲô�����к����URL error                                                 
try:                                                #��cqcre��������ʲô�����к����http error����������Ǵ���ԭ��
    urllib2.urlopen(req)
except urllib2.URLError, e:
    if hasattr(e,"reason"):
        print e.reason
else:
    print "OK"
