#!/usr/bin/env python
# coding: utf-8

# In[216]:


import pandas as pd
import numpy as np
import seaborn as sns
from datetime import date
from datetime import datetime
import sqlite3 as sql
print('tá ok!!')


# In[217]:


list_test = pd.read_html('https://www.worldfootball.net/teams/vasco-da-gama/2020/2/')
vasco = pd.DataFrame(list_test[1])
vasco['Goalkeeper'][0] = 'Goalkeeper'


# In[218]:



n = 0
for i in vasco['Goalkeeper']:
    if pd.isnull(vasco['Goalkeeper'][n]):
        vasco['Goalkeeper'][n] = vasco['Goalkeeper'][n-1]
    n = n + 1
vasco


# In[219]:


vasco = vasco.drop(labels = [36, 5, 18, 29])
vasco = vasco.reset_index()


# In[220]:


vasco = vasco.drop(columns = ['Goalkeeper.3', 'index'])


# In[221]:


vasco.columns = ['Position','Number', 'Name', 'Nationality', 'Birth Date', 'Age']


# In[222]:


#d = datetime.strptime((vasco['Birth Date'][35]), '%d/%m/%Y').year
D = datetime.today().year
n = 0

#vasco['Age'][0] = 1
for i in vasco.index:
    d = datetime.strptime((vasco['Birth Date'][n]), '%d/%m/%Y').year
    p = D - d
    vasco['Age'][n] = p
    n = n + 1


# In[223]:


vasco


# In[ ]:





# In[224]:


vascodb = sql.connect('vasco_crvg.db')
c = vascodb.cursor()



c.execute('DROP TABLE IF EXISTS players')


#c.execute('CREATE TABLE PLAYERS (NUMBER integer, NAME varchar(30), NATIONALITY varchar(30), BIRTH DATE date, POSITION varchar(30), AGE integer)')
vascodb.commit()



vasco.to_sql('players', vascodb, if_exists='replace', index = False)
 
"""c.execute('''  
SELECT * FROM PLAYERS
          ''')

for row in c.fetchall():
    print (row)"""


# In[ ]:





# In[242]:


#sns.distplot(a =vasco['Age'][0:33] )


# In[ ]:





# In[ ]:




