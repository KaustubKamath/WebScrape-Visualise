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

#To find jobs tagged with python. If string = "python" is directly passed it specifically looks for that text and empty list may be returned.
python_jobs = results.find_all("h2", string = lambda text: "python" in text.lower())
print(python_jobs)
print(len(python_jobs))

#if you directly itierate over python_jobs using the above for loop, it will throw an error, as the h2 element selected contains only the job title and not the other information.
#Hence we will need to identify the parent element in the HTML using the dev console. 
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

    #To obtain the links as well. 
    links = job_element.find_all("a")
    
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")
