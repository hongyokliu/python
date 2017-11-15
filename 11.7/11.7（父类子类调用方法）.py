#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Student:        # 定义父类
   stu_count = 0
   def __init__(self, stu_name, stu_num, stu_class, male):
      self.name = stu_name
      self.stu_num = stu_num
      self.stu_class = stu_class
      self.male=male
      Student.stu_count += 1
   def getstucount(Student):
      return Student.stu_count
      

class isyoungpioneers(Student):
   isyoung_stucount =0
   def canRecite(self):
      print "小学生会背诵"
   def canOral(self):
      print "小学生会口算"
   

 
class Middleschstu(Student): # 定义子类
   middle_stucount =0
   def __init__(self, stu_name, stu_num, stu_class, male):
      self.name = stu_name
      self.stu_num = stu_num
      self.stu_class = stu_class
      self.male=male
      Middleschstu.middle_stucount += 1
   def canChemistry(self):
      print "中学生会化学"
   def canPhysics(self):
      print "中学生会物理"
 
#c = Child()          # 实例化子类
#c.childMethod()      # 调用子类的方法
#c.parentMethod()     # 调用父类方法
#c.setAttr(200)       # 再次调用父类的方法 - 设置属性值
#c.getAttr()          # 再次调用父类的方法 - 获取属性值
