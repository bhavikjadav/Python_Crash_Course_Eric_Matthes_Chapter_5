#!/usr/bin/env python
# coding: utf-8

# # 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
# # • If the list is empty, print the message We need to find some users!
# # • Remove all of the usernames from your list, and make sure the correct message is printed.

# In[31]:


# users = ["mehul", "bhavik", "admin", "pruthvi", "jay", "jignesh"]
users = []


# In[32]:


if users:
    for user in users:
        print(user.title())
else:
    print("We need to find some users.")

