#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Student:
   stu_count = 0
   
   stu_count_jy162 = 0
   stu_count_wl163 = 0
   
   stu_count_male = 0
   stu_count_female= 0
 
 
   def __init__(self, stu_name, stu_num, stu_class, male):
      self.name = stu_name
      self.stu_num = stu_num
      self.stu_class = stu_class
      self.male=male
      Student.stu_count += 1


      
      if self.stu_class=="wl163":
         Student.stu_count_wl163+= 1
      elif self.stu_class=="jy162":
         Student.stu_count_jy162 += 1

      if self.male=="1":
         Student.stu_count_male+= 1
      elif self.male=="0":
         Student.stu_count_female += 1

         

  
   
   def displayCount(self):
     print "Total Student %d" % Student.stu_count
 
   def displayStudent(self):
      print "Name:",self.name,  " Num:",self.stu_num," class:",self.stu_class," male:",self.male
