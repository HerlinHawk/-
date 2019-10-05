#!/usr/bin/env python
# coding: utf-8

# In[38]:


import requests


# In[45]:


response = requests.get('https://sf6-ttcdn-tos.pstatp.com/obj/temai/Fv422XBuqidP_2l1xQkHlkHfyx9Twww750-750')


# In[4]:


path = 'D:/jupyterworkspace/img'
import os
#python 反斜杠：去转移字符的麻烦


# In[5]:


os.getcwd()


# In[6]:


img = response.content


# In[7]:


os.makedirs(path)


# In[46]:


with open(path+'/1.jpg','wb') as f:
    f.write(img)


# In[39]:


import pandas as pd


# In[40]:


data = pd.read_csv('D:/jupyterworkspace/goods.csv')


# In[41]:


data.head()


# In[52]:


df = pd.DataFrame([data.img_url,data.cid,data.first_cid,data.second_cid])


# In[53]:


df = df.T
#df.head()
df.axes
import time


# pandas 的切片操作

# In[60]:


for i in range(1000):
    #print(i)
    a= [df.img_url[i+233],df.cid[i+233],df.first_cid[i+233],df.second_cid[i+233]]
    print(a,df.index)
    response = requests.get(a[0])
    img = response.content
    with open(path+'/'+str(i+233)+'_'+str(a[1])+'_'+str(a[2])+'_'+str(a[3])+'.jpg','wb') as f:
        f.write(img)
        time.sleep(1)


# In[36]:


a[0]
type(str(a[1]))
a


# In[26]:


df.iloc[0,:]


# In[137]:


df[0:2]


# In[63]:


res = requests.get('https://outlook.live.com/mail/inbox')


# res.headers

# 生成标签和文件路径
# 顺序为
# 路径 + 第一类目 + 第二类目 + 第三类目

# In[105]:


data = []
for a in os.listdir(path):
    #print(a.split('_'))
    k = a.split('_')
    #print(a)
    k[3] = k[3].split('.')[0]
    data.append([path+'/'+a,k[1],k[2],k[3]])
        #data.append([a[1],a[2],i[0]])
        #print(data)


# In[107]:


data.pop()


# In[ ]:




