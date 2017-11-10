Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> y='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'
>>> import re
>>> re.findall('\w',y)
['1', '2', '3', 'q', 'q', 'c', 'o', 'm', 'a', 'a', 'a', '1', '6', '3', 'c', 'o', 'm', 'b', 'b', 'b', '1', '2', '6', 'c', 'o', 'm', 'a', 's', 'd', 'f', 'a', 's', 'f', 's', '3', '3', '3', '3', '3', 'a', 'd', 'f', 'c', 'o', 'm']
>>> re.findall('\w+',y)
['123', 'qq', 'comaaa', '163', 'combbb', '126', 'comasdfasfs33333', 'adfcom']
>>> re.findall('\w+@',y)
['123@', 'comaaa@', 'combbb@', 'comasdfasfs33333@']
>>> re.findall('\w+@\w\.',y)
[]
>>> re.findall('\w+@\.',y)
[]
>>> re.findall('\w+@\w',y)
['123@q', 'comaaa@1', 'combbb@1', 'comasdfasfs33333@a']
>>> re.findall('\w+@\w+\.',y)
['123@qq.', 'comaaa@163.', 'combbb@126.']
>>> re.findall('\w+@\w+\.\w',y)
['123@qq.c', 'omaaa@163.c', 'ombbb@126.c']
>>> re.findall('\w+@\w+\.\w+',y)
['123@qq.comaaa', 'combbb@126.comasdfasfs33333']
>>> re.findall('\w+@\w+\.',y)
['123@qq.', 'comaaa@163.', 'combbb@126.']
>>> re.findall('\w+@\w+\.com',y)
['123@qq.com', 'aaa@163.com', 'bbb@126.com']
>>> 
