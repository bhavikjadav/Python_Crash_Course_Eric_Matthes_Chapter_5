#!/usr/bin/env python
# coding: utf-8

# # 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
# # • If the alien is green, print a message that the player earned 5 points.
# # • If the alien is yellow, print a message that the player earned 10 points.
# # • If the alien is red, print a message that the player earned 15 points.
# # • Write three versions of this program, making sure each message is printed for the appropriate color alien.

# In[11]:


alien_color = "blue"


# In[12]:


if alien_color == "green":
    print("Player earned 5 points.")
elif alien_color == "yellow":
    print("Player earned 10 points.")
else:
    print("Player earned 15 points.")

