#Importing required libraries. 
from bs4 import BeautifulSoup
import requests
import pandas as pd

#Covid -19 data from Ministry of Health and Family Welfare website.
#URL = 'https://www.mohfw.gov.in/'
URL = 'https://www.worldometers.info/coronavirus/'
page = requests.get(URL)

#Checking the return code, expects to be 200. 
print(page) 


soup = BeautifulSoup(page.content, 'lxml')

'''
#Data stored under the table with class "statetable".
results = soup.find('div', class_= 'data-table')
table_data = soup.find('table', class_='statetable table table-stripped')
print(table_data)

#obtains column names
header = []
for column in results.find_all('th'):
    title = column.text
    header.append(title)
print(header)

#As the table under contains multi-level column hierarchy for "Active Cases", "Cured/Discharged/Migrated" and "Deaths". 
#Removing the multi-level hierarchy. 
header.remove('Active Cases')
header.remove('Cured/Discharged/Migrated')
header.remove('Deaths')

#Appending the columns names to reflect the multi-level. 
header[2] = 'Active Cases - Total'
header[3] = 'Active Cases - Change since yesterday'
header[4] = 'Cured/Discharged/Migrated - Cumulative'
header[5] = 'Cured/Discharged/Migrated - Change since yesterday'
header[6] = 'Deaths - Cumulative'
header[7] = 'Deaths - Death During Day'

print(f'This is header after removing unnecessary columns: {header}')


mydata = pd.DataFrame(columns = header)
print(f'This is my Data Frame: {mydata}')



for j in table_data.find_all('tr')[1:]:
    print(f'This is j: {j}')
    row_data = j.find_all('td')
    print(f'This is my row data: {row_data}')
    row = [i.text for i in row_data]
    length = len(mydata)
    print(f'This is the length of my data: {length}')
    #mydata.loc[length] = row
'''

table1 = soup.find('table', id='main_table_countries_today')
headers = []
for i in table1.find_all('th'):
 title = i.text
 headers.append(title)
headers[13] = 'Tests/1M pop'
mydata = pd.DataFrame(columns = headers)
for j in table1.find_all('tr')[1:]:
 row_data = j.find_all('td')
 row = [i.text for i in row_data]
 length = len(mydata)
 mydata.loc[length] = row
 print(length)
 # Drop and clearing unnecessary rows
 
mydata.drop(mydata.index[0:7], inplace=True)
mydata.drop(mydata.index[222:229], inplace=True)
mydata.reset_index(inplace=True, drop=True)
# Drop “#” column
mydata.drop('#', inplace=True, axis=1)  
# Export to csv
mydata.to_csv('covid_data.csv', index=False)
# Try to read csv
mydata2 = pd.read_csv('covid_data.csv')                 
