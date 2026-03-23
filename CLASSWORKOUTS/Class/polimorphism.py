"""
Method overloading:=> Same class ,same method name but different number of paramaters occured within the same methods
Class Calculator:
   def add(self,n1,n2):
      return n1+n2
   def add(self,n1,n2,n3,n4):
      return n1+n2+n3+n4
cal_instance=Calculator()  
print(calculator_instance.add(100,200,300,400))
print(calculator_instance.add(100,200))          ===> from this  line onwards it doesnt work 
print(calculator_instance.add(100,200,300))     
"""