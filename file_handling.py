#!/usr/bin/env python
# coding: utf-8

# In[1]:


help("modules")


# In[4]:


import sys

sys.version_info


# In[ ]:


# to get list of all the functions in module
import math
print(dir(math))


# In[6]:


#shift-tab or gooogle ->math module in python
math.floor(2)


# # file handling
# types
# 1. binary files
# 2. text files---> don't have any specific encoding {web standards, source code, document, tabular 
# 
# # operations
# open
# read 
# write
# close
# 
# other operations
# rename
# delete
# 
# 
# dedfault mode is read(r) and text format
# 
# 1. r   = open the file read-only.Start from the beginning
# 2. rb  = open and read-only binary file
# 3. r+  = read+write
# 4. w = write only
# 5. wb = write-only binary file
# 6. w+ = writing and reading
# 7. wb+ = writing and reading binary
# 8. a = open file for appending
# 9. a+ = append and read
# 10. ab+= append and read binary
# 11. x= for creating file
# 

# In[19]:


# create a file
# syntax->   open(filename,mode='r',buffering=-1,encoding=None,errors=None,newline=None,closefd=True,Opener=None)



# opening a file using relative path
fp = open("testing.txt","r",encoding="utf-8")
#res=fp.read()
res=fp.read(8)
print(res)
fp.close()


# In[20]:


# helper-function readline()
fp = open("testing.txt","r",encoding="utf-8")
res=fp.readline()
print(res)
fp.close()


# In[21]:


fp = open("testing.txt","r",encoding="utf-8")
#res=fp.read()
res=fp.readline(5)
print(res)
fp.close()


# In[23]:


# readlines()
fp = open("testing.txt","r",encoding="utf-8")
#res=fp.read()
res=fp.readlines()
print(res)
print(type(res))
fp.close()


# In[26]:


#alternative of readlines is using loop
fp = open("testing.txt","r",encoding="utf-8")
#res=fp.read()
for lines in fp:
    print(lines)
fp.close()


# In[28]:


# read from specific line from file
line_number = 3
fp = open("testing.txt","r")
currentline = 1


for line in fp:
    if(currentline == line_number):
        print(line)
        break
    currentline = currentline+1

