Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list1=["physics","chemistry",1997,2000]
>>> list2=[1,2,3,4,5,6,7]
>>> print list1
['physics', 'chemistry', 1997, 2000]
>>> print list2
[1, 2, 3, 4, 5, 6, 7]
>>> print list1[1]
chemistry
>>> print  list1[-1]
2000
>>> print list1[0:3]
['physics', 'chemistry', 1997]
>>> print list1  * 2
['physics', 'chemistry', 1997, 2000, 'physics', 'chemistry', 1997, 2000]
>>> print list1 + list2
['physics', 'chemistry', 1997, 2000, 1, 2, 3, 4, 5, 6, 7]
>>> print len(list2)
7
>>> list1[2]=2001
>>> print list1
['physics', 'chemistry', 2001, 2000]
>>> del list1[2]
>>> print list1
['physics', 'chemistry', 2000]
>>> print '2000' in list1
False
>>> print 2000 in list1
True
>>> print 'phycis' in list1
False
>>> print 'physics'in list1
True
>>> for i in list1:
	print i

	
physics
chemistry
2000
>>> 
>>> print cmp(list1,list2)
1
>>> print cmp(list[2],list2[4])

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print cmp(list[2],list2[4])
TypeError: 'type' object has no attribute '__getitem__'
>>> print cmp(list1[2],list2[4])
1
>>> print cmp(list2[4],list1[2])
-1
>>> print max([0, 1, 2, 3, 4])
4
>>> print max(list1)
physics
>>> print min([0, 1])
0
>>> print max(list2)
7
>>> print min(list2)
1
>>> aTuple =(1,2,3,4)
>>> list3=list(aTuple)
>>> print list3
[1, 2, 3, 4]
>>> list3.extend(list1)
>>> print list3
[1, 2, 3, 4, 'physics', 'chemistry', 2000]
>>> print list3.count(2000)
1
>>> print list3.index('physics')
4
>>> print list1.index('physics')
0
>>> list3.insert(0,'hello')
>>> print list3
['hello', 1, 2, 3, 4, 'physics', 'chemistry', 2000]
>>> listq.insert(2,'ok')

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    listq.insert(2,'ok')
NameError: name 'listq' is not defined
>>> list1.insert(2,'ok')
>>> print list1
['physics', 'chemistry', 'ok', 2000]
>>> print list3.pop(0)
hello
>>> print list3
[1, 2, 3, 4, 'physics', 'chemistry', 2000]
>>> list3.remove(1)
>>> print list3
[2, 3, 4, 'physics', 'chemistry', 2000]
>>> list3.reverse()
>>> print list3
[2000, 'chemistry', 'physics', 4, 3, 2]
>>> list3.sort()
>>> print list3
[2, 3, 4, 2000, 'chemistry', 'physics']
>>> 
