
import urllib2
 
request = urllib2.Request('http://blog.csdn1.net/cqcre')
try:
    urllib2.urlopen(request)
except urllib2.URLError, e:
    print e.reason
