#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class BMI:
    def __init__(self,name,age,weight,sg):
        self.name = name
        self.age = age
        self.weight = weight
        self.sg = sg
    
    def print_BMI(self):
        getBMI = self.weight/(self.sg*self.sg)
        getStatus = ""
        if getBMI<18.5:
            getStatus = "偏廋"
        elif getBMI<24:
            getStatus = "正常"
        elif getBMI<30:
            getStatus = "偏胖"
        else:
            getStatus = "肥胖"
            
        print("{n}的BMI是{a}".format(n=self.name,a=getBMI))
        print("{n}的健康状态是{b}".format(n=self.name,b=getStatus))
bmi1 = BMI("赵四",18,70,1.75)
bmi1.print_BMI()

