#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import calendar
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings 
warnings.filterwarnings('ignore')


# In[5]:


df = pd.read_csv(r'C:\Users\vashi\Downloads\hotel_bookings 2.csv')



# In[6]:


df.head()


# In[7]:


df.tail()


# In[8]:


df.shape


# In[9]:


df.columns


# In[10]:


df.info()


# In[11]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'], format='%d/%m/%Y')


# In[12]:


df.info()


# In[13]:


df.describe(include = 'object')


# In[14]:


for col in df.describe(include='object').columns:
    print(col)
    print(df[col].unique())
    print('-'*80)


# In[15]:


df.isnull().sum()


# In[16]:


df.columns = df.columns.str.strip()


# In[17]:


try:
    df.drop(['company', 'agent'], axis=1, inplace=True)
    print("Columns dropped successfully.")
except KeyError as e:
    print(f"Error: {e}")
    
df.dropna(inplace=True)



# In[18]:


df.isnull().sum()


# In[19]:


df.describe()


# In[20]:


df['adr'].plot(kind='box')


# In[21]:


df=df[df['adr']<5000]
df['adr'].plot(kind='box')


# In[22]:


df.describe()


# In[23]:


is_canceled_perc=df['is_canceled'].value_counts(normalize=True)
print(is_canceled_perc)


# In[24]:


plt.figure(figsize=(5,4))
plt.title('reservation_status_count')
plt.bar(['Not canceled','canceled'],df['is_canceled'].value_counts(),edgecolor ='k',width = 0.8)
plt.show()


# In[25]:


plt.figure(figsize=(8, 4))
ax1 = sns.countplot(x='hotel', hue='is_canceled', data=df, palette='Oranges')
legend_labels, _ = ax1.get_legend_handles_labels()
ax1.legend(legend_labels, ['not canceled', 'canceled'], bbox_to_anchor=(1, 1))
plt.title('Reservation Status in Different Hotels', size=20)
plt.xlabel('hotel')
plt.ylabel('number of Reservations')
plt.show()


# In[26]:


resort_hotel=df[df['hotel']=='Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize=True)


# In[27]:


city_hotel=df[df['hotel']=='City Hotel']
city_hotel['is_canceled'].value_counts(normalize=True)


# In[28]:


resort_hotel=resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel=city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[29]:


plt.figure(figsize=(20, 4))
plt.title('Average Daily Rate in the City and Resort Hotel', fontsize=30)
plt.plot(resort_hotel.index,resort_hotel['adr'],label= 'Resort Hotel')
plt.plot(city_hotel.index,city_hotel['adr'],label= 'City Hotel')
plt.legend(fontsize=20)
plt.show()


# In[30]:


df['month'] = df['reservation_status_date'].dt.month
df['month_name'] = df['month'].apply(lambda x: calendar.month_name[x])

plt.figure(figsize=(16, 8))
ax1 = sns.countplot(x='month_name', hue='is_canceled', data=df, palette='bright')
legend_labels, _ = ax1.get_legend_handles_labels()
ax1.legend(legend_labels, ['not canceled', 'canceled'], bbox_to_anchor=(1, 1))
plt.title('Reservation Status per Month', size=20)
plt.xlabel('Month')
plt.ylabel('Number of Reservations')
plt.show()


# In[31]:


df['month_name'] = df['month'].apply(lambda x: calendar.month_name[x])

plt.figure(figsize=(16, 8))
plt.title('ADR per month', fontsize=30)

# Assuming you have a 'month' column in your DataFrame
sns.barplot(x='month', y='adr', data=df[df['is_canceled'] == 1].groupby('month')[['adr']].sum().reset_index())

plt.show()


# In[32]:


import matplotlib.pyplot as plt
import seaborn as sns

cancelled_data = df[df['is_canceled'] == 1]
top_15_country = cancelled_data['country'].value_counts()[:15]

plt.figure(figsize=(8, 8))
plt.title('Top 15 countries with reservation canceled')

# Assuming you want to visualize the top 15 countries with canceled reservations in a pie chart
plt.pie(top_15_country, labels=top_15_country.index, autopct='%.3f%%' ,colors=sns.color_palette('viridis', n_colors=15))

plt.axis('equal')  

plt.show()


# In[33]:


df['market_segment'].value_counts()


# In[34]:


df['market_segment'].value_counts(normalize=True)


# In[35]:


cancelled_df_adr=cancelled_data.groupby('reservation_status_date')[['adr']].mean()
cancelled_df_adr.reset_index(inplace=True)
cancelled_df_adr.sort_values('reservation_status_date',inplace=True)

not_cancelled_data=df[df['is_canceled']==0]
not_cancelled_df_adr=not_cancelled_data.groupby('reservation_status_date')[['adr']].mean()
not_cancelled_df_adr.reset_index(inplace=True) 
not_cancelled_df_adr.sort_values('reservation_status_date',inplace=True)  

plt.figure(figsize=(20, 6))
plt.title('Average Daily Rate')
plt.plot(not_cancelled_df_adr['reservation_status_date'] ,not_cancelled_df_adr['adr'],label='not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'] ,cancelled_df_adr['adr'],label='cancelled')
plt.legend()


# In[ ]:




