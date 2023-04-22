#Importing required libraries. 
from bs4 import BeautifulSoup
import requests
import pandas as pd

#Covid -19 data from World O Meters website.
URL = 'https://www.worldometers.info/coronavirus/'
page = requests.get(URL)

#Checking the return code, expects to be 200. 
#print(f'The page response is: {page}') 

soup = BeautifulSoup(page.content, 'lxml')

#Data stored under the table with class "main_table_countries_today".
table_data = soup.find('table', id='main_table_countries_today')
#print(f'The table data is: {table_data}')

#obtains column names
headers = []
for columns in table_data.find_all('th'):
 column = columns.text
 headers.append(column)
#print(f'The header is: {headers}')

#Two columns names have garabge value.
headers[10] = 'TotalCases/1M pop'
headers[13] = 'Tests/1M pop'
#print(f'The new header is: {headers}')

mydata = pd.DataFrame(columns = headers)

#Getting the data.
for j in table_data.find_all('tr')[1:]:
 row_data = j.find_all('td')
 row = [i.text for i in row_data]
 length = len(mydata)
 mydata.loc[length] = row
 #print(length)

# Drop and clearing unnecessary rows.
mydata.drop(mydata.index[0:7], inplace=True)
mydata.drop(mydata.index[222:229], inplace=True)
mydata.reset_index(inplace=True, drop=True)
#print(f'My data frame is: {mydata}')

# Drop “#” column.
mydata.drop('#', inplace=True, axis=1)  
#print(f'Printing the data frame after dropping #: \n{mydata}')

# Creating a CSV and exporting to it.
mydata.to_csv('covid_data.csv', index=False)

# Try to read the csv.
mydata2 = pd.read_csv('covid_data.csv')         
#print(f'This is printing the data from the created CSV: \n{mydata2}')




