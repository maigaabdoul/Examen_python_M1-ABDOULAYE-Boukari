#!/usr/bin/env python
# coding: utf-8

# # EXERCICE 1

# In[1]:


from numpy import linspace
from matplotlib.pyplot import * 


# In[2]:


x = linspace(5, 30, 20)
y = x**5
plot(x, y, "r")
show()


# In[3]:


import turtle as t1


# In[4]:


t = t1.Turtle()
for i in range(4):
    t.fd(200)
    t.lt(90)
t.reset()


# In[ ]:


class Curve:
    def __init__(self, start, stop, nbr_points = 5432):
        self.start = start
        self.stop = stop
        self.nbr_points = nbr_points
    def privee(self, x):
        return x**5
    def trace(self):
        y = x**5
        plot(x, y, "r")
        show()

