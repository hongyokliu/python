#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("testfile", "w")  #或者fh=open("D:/liusu/test/python/异常处理","w")
    # 在open中用正确路径（D:/liusu/test/python/异常处理）成功，用不正确路径不成功

except IOError:
    print "Error: 没有找到文件或读取文件失败"

finally:
    print "close file"
    fh.close()
