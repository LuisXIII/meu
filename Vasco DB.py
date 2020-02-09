
import pandas as pd
from datetime import datetime
import sqlite3 as sql
print('tá ok!!')


list_test = pd.read_html('https://www.worldfootball.net/teams/vasco-da-gama/2020/2/')
vasco = pd.DataFrame(list_test[1])
vasco['Goalkeeper'][0] = 'Goalkeeper'


#the table is upload a dataframe with some issues, like a empty column this code fix the 'Position' of players
n = 0
for i in vasco['Goalkeeper']:
    if pd.isnull(vasco['Goalkeeper'][n]):
        vasco['Goalkeeper'][n] = vasco['Goalkeeper'][n-1]
    n = n + 1
vasco



#this drop some rows with useless data
vasco.drop(labels = [36, 5, 18, 29], inplace = True)
vasco = vasco.reset_index()


#other with no avaliable data
vasco.drop(columns = ['Goalkeeper.3', 'index'], inplace = True)



#changing the columns' name to the right name
vasco.columns = ['Position','Number', 'Name', 'Nationality', 'Birth Date', 'Age']

D = datetime.today().year
n = 0

#calculing the age 
for i in vasco.index:
    d = datetime.strptime((vasco['Birth Date'][n]), '%d/%m/%Y').year
    p = D - d
    vasco['Age'][n] = p
    n = n + 1



#create a database file
vascodb = sql.connect('vasco_crvg.db')
c = vascodb.cursor()


#testing if the table already exist, if it's true then will overwrite it
c.execute('DROP TABLE IF EXISTS players')


#c.execute('CREATE TABLE PLAYERS (NUMBER integer, NAME varchar(30), NATIONALITY varchar(30), BIRTH DATE date, POSITION varchar(30), AGE integer)')
vascodb.commit()



vasco.to_sql('players', vascodb, if_exists='replace', index = False)
#this line show the database file 
"""c.execute('''  
SELECT * FROM PLAYERS
          ''')

for row in c.fetchall():
    print (row)"""






