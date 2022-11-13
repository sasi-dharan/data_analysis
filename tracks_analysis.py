#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df_tracks= pd.read_csv('C:/Users/HP/Downloads/spotify_analysis/tracks.csv')
df_tracks.head()


# In[4]:


#null_values
pd.isnull(df_tracks).sum()


# In[3]:


df_tracks.info()


# In[4]:


sorted_df = df_tracks.sort_values('popularity', ascending= True)
sorted_df.head(10)


# In[5]:


df_tracks.describe().transpose()


# In[6]:


most_popular = df_tracks.query('popularity>90', inplace= False).sort_values('popularity', ascending= False)
most_popular.head(10)


# In[7]:


df_tracks.set_index('release_date', inplace=True)
df_tracks.index=pd.to_datetime(df_tracks.index)
df_tracks.head()


# In[8]:


df_tracks[['artists']].iloc[18]


# In[9]:


df_tracks['duration']= df_tracks['duration_ms'].apply(lambda x: round(x/1000))
df_tracks.drop('duration_ms', inplace= True, axis=1)
df_tracks.duration.head()


# In[10]:


corr_df=df_tracks.drop(['key','mode','explicit'],axis=1).corr(method='pearson')
plt.figure(figsize=(14,6))
heatmap=sns.heatmap(corr_df,annot=True,fmt='.1g',vmin=-1,vmax=1,center=0,cmap='inferno',linewidths=1,linecolor='Black')
heatmap.set_title('Correlation Heat Map')
#heatmap.set_xticklables(heatmap.get_xticklables(),rotation=90)


# In[11]:


sample_df=df_tracks.sample(int(0.004*len(df_tracks)))
print(len(sample_df))


# In[12]:


plt.figure(figsize=(20,6))
sns.regplot(data = sample_df, y='loudness', x='energy',color ='c').set(title='Loudness vs Noise Corr')


# In[13]:


plt.figure(figsize=(20,6))
sns.regplot(data = sample_df, y='popularity', x='acousticness',color ='c').set(title='popularity vs acousticnes Corr')


# In[2]:


df_tracks['dates']=df_tracks.index.get_level_values('release_date')
df_tracks.dates= pd.to_datetime(df_tracks.dates)
years=df_tracks.dates.dt.year


# In[14]:


sns.displot(years, discrete=True,aspect=2, height=5, kind='hist').set(title='num of songs per year')


# In[15]:


total_dr = df_tracks.duration
fig_dims= (18,7)
fig, ax= plt.subplots(figsize= fig_dims)
fig= sns.barplot(x= years , y=total_dr ,ax=ax, errwidth = False).set(title='years vs duration')
plt.xticks(rotation=90)


# In[1]:


total_dr = df_tracks.duration
sns.set_style(style='whitegrid')
fig_dims= (10 ,5)
fig, ax= plt.subplots(figsize= fig_dims)
fig= sns.barplot(x= years , y=total_dr ,ax=ax).set(title='years vs duration')
plt.xticks(rotation=90)


# In[16]:


df_genre=pd.read_csv('C:/Users/HP/Downloads/spotify_analysis/SpotifyFeatures.csv')
df_genre.head()







