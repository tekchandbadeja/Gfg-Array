#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def rotate( arr,n):
    l1=[]
    ele=arr.pop()
    l1.append(ele)
    return l1+arr
obj=rotate([11,6,8,4,3],5)
print(obj)

