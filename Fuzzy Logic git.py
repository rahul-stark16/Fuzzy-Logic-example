#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import skfuzzy as fuzzy
import matplotlib.pyplot as plt


# In[2]:


x_qual = np.arange(0, 11, 1)
x_serv = np.arange(0, 11, 1)
x_tip = np.arange(0, 26, 1)


# In[3]:


# Generate fuzzy membership function
qual_lo = fuzzy.trimf(x_qual, [0, 0, 5]) # trimf -> Triangle membership function
qual_md = fuzzy.trimf(x_qual, [0, 5, 10]) # trimf(Left leg, Mid leg, Right leg)
qual_hi = fuzzy.trimf(x_qual, [5, 10, 10])

serv_lo = fuzzy.trimf(x_serv, [0, 0, 5]) # trimf -> Triangle membership function
serv_md = fuzzy.trimf(x_serv, [0, 5, 10])
serv_hi = fuzzy.trimf(x_serv, [5, 10, 10])

tip_lo = fuzzy.trimf(x_tip, [0, 0, 13]) # trimf -> Triangle membership function
tip_md = fuzzy.trimf(x_tip, [0, 13, 25])
tip_hi = fuzzy.trimf(x_tip, [13, 25, 25])


# ### Visualize these usiverses and membership functions

# In[4]:


fig, (ax0, ax1, ax2) = plt.subplots(nrows = 3, figsize = (8, 9))
ax0.plot(x_qual, qual_lo, 'b', linewidth = 1.5, label = 'Bad')
ax0.plot(x_qual, qual_md, 'g', linewidth = 1.5, label = 'Decent')
ax0.plot(x_qual, qual_hi, 'r', linewidth = 1.5, label = 'Great')
ax0.set_title('Food Quality')
ax0.legend()


ax1.plot(x_serv, serv_lo, 'b', linewidth = 1.5, label = 'Poor')
ax1.plot(x_serv, serv_md, 'g', linewidth = 1.5, label = 'Acceptable')
ax1.plot(x_serv, serv_hi, 'r', linewidth = 1.5, label = 'Amazing')
ax1.set_title('Service Quality')
ax1.legend()


ax2.plot(x_tip, tip_lo, 'b', linewidth = 1.5, label = 'Low')
ax2.plot(x_tip, tip_md, 'g', linewidth = 1.5, label = 'Mid')
ax2.plot(x_tip, tip_hi, 'r', linewidth = 1.5, label = 'High')
ax2.set_title('Tip Graph')
ax2.legend()


# In[ ]:




