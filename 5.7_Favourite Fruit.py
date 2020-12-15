#!/usr/bin/env python
# coding: utf-8

# # 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
# # • Make a list of your three favorite fruits and call it favorite_fruits.
# # • Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like bananas!

# In[1]:


fav_fruits = ["pineapple", "apple", "kiwi", "banana"]


# In[2]:


if "guava" in fav_fruits:
    print("You really like Guava.")

if "pineapple" in fav_fruits:
    print("You really like Pineapples.")

if "banana" in fav_fruits:
    print("Banana is healthy.")

