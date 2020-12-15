#!/usr/bin/env python
# coding: utf-8

# # 5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:
# # car = 'subaru' 
# # print("Is car == 'subaru'? I predict True.")
# # print(car == 'subaru')
# # print("\nIs car == 'audi'? I predict False.")
# # print(car == 'audi')
# # • Look closely at your results, and make sure you understand why each line evaluates to True or False.
# # • Create at least ten tests. Have at least five tests evaluate to True and another five tests evaluate to False.

# In[13]:


car = "subaru"
morning = "good"


# In[14]:


print(car=="subaru")


# In[15]:


print(car=="audi")


# In[16]:


print(morning=="bad")


# In[17]:


print(morning=="good")


# In[18]:


print((car=="subaru") and (morning=="good"))


# In[19]:


print((car=="subaru") and (morning=="bad"))


# In[20]:


print((car=="subaru") or (morning=="good"))


# In[21]:


print((car=="audi") or (morning=="good"))

