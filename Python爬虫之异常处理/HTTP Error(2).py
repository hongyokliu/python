import urllib2
 
req = urllib2.Request('http://blog.csdn1.net/cqcre1')#��csdn��������ʲô�����к����URL error
try:                                                 #��cqcre��������ʲô�����к����http error����������Ǵ������
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:
    print e.reason
else:
    print "OK"
