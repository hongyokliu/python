Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tup1=('physics','chemmistry',1997,2000)
>>> tup2=(1,2,3,4,5)
>>> print tup1[0]
physics
>>> print tup2[1:5]
(2, 3, 4, 5)
>>> tup3=tup1+tup2
>>> print tup3
('physics', 'chemmistry', 1997, 2000, 1, 2, 3, 4, 5)
>>> del tup3
>>> print tup3

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print tup3
NameError: name 'tup3' is not defined
>>> tup1[2]
1997
>>> tup1[-1]
2000
>>> tup1[-2]
1997
>>> 
