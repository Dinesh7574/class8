#!/usr/bin/env python
# coding: utf-8

# In[7]:


class calc():
    
    def add(self,a,b):                     #fun inside a class named as method 
        print(a+b)                               
    def sub(self,a,b):
        print(a-b)
    def mult(self,a,b):
        print(a*b)


# In[8]:


a = calc()


# In[3]:


a.add(5,4)


# In[9]:


a.mult(5,4)


# In[5]:


print(a)            #here a is object


# In[6]:


print(calc)                       #class is said to be class


# In[10]:


class hotel():
    
    def floor (self,a):
        if a==1:
            print("non veg floor")
        elif a==2:
            print("veg floor")
    def dish (self,a):
        if a==2:
            print("non veg dish")
        elif a==2:
            print("veg dish")


# In[11]:


a = hotel()
a.floor(1)
a.dish(2)


# In[14]:


class hotel():
    
    def __init__ (self,a):                                    #__init__ constructor
        self.a =a                                              
    
    def floor (self):
        
        if self.a==1:
            print("non veg floor")
        elif self.a==2:
            print("veg floor")
    def dish (self):
        if self.a==1:
            print("non veg dish")
        elif a==2:
            print("veg dish")


# In[15]:


a = hotel(1)
a.floor()
a.dish()


# In[47]:


class calc():
    
    def __init__ (self,a,b):                                    
        self.a =a 
        self.b =b
    def add(self):
        print(self.a+self.b)                               
    def sub(self):
        print(self.a-self.b)
    def mult(self):
        print(self.a*self.b)
        print
        


# In[48]:


a = calc(2,2)
a.add()
a.sub()
a.mult()


# In[55]:


class gold():
    def __init__ (self,a,b):
        
        self.a = 1000 
        self.b =b
    
    def mult(self):
        print(self.a*self.b)
        
    
    


# In[56]:


a = gold(a,200)
a.mult()


# In[ ]:




