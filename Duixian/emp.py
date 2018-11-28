#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Parent:        # 定义父类
   __parentAttr = 100
   def __init__(self):
      self.__parentAttr+=1
      print ("调用父类构造函数")
 
   def parentMethod(self):
      print ('调用父类方法')
 
   def setAttr(self, attr):
      Parent.__parentAttr = attr
 
   def getAttr(self):
      print ("父类属性 :", Parent.__parentAttr)
   def jia(self):
      self.__parentAttr+=1
 
class Child(Parent): # 定义子类
   '''def __init__(self):
      print ("调用子类构造方法")'''
 
   def childMethod(self):
      print ('调用子类方法')
 
c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法      # 再次调用父类的方法 - 设置属性值
c.jia()
print(getattr(c,'__parentAttr'))
print(c.__parentAttr)