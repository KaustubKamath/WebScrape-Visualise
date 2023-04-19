#Imports
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
#Scraping HTML content from the page.
page = requests.get(URL)
#print(page.text)
#Parsing HTML code using Beautiful Soup. 
soup = BeautifulSoup(page.content, "html.parser")
#Finding elements by id.
results = soup.find(id = "ResultsContainer")
#print(results.prettify())
#Find elements by HTML class and extract text from it.
jobs = results.find_all("div", class_="card-content")
for job_element in jobs:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

