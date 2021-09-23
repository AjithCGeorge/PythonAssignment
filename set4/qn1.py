import re
from PIL import Image
from bs4 import BeautifulSoup
import requests

def img_url(data):
    img = str(data.find('img'))
    img = re.search('src=.+"', str(img)).group()
    img = re.search('".+"', img).group()
    img = re.sub('"', '', img)
    # im = Image.open(requests.get(img,stream=True).raw)
    return img


def job_title(data):
    job_title = data.find('h2', class_='title is-5')
    job_title=job_title.get_text()
    return job_title


def company_name(data):
    company = data.find('h3', class_='subtitle is-6 company')
    company=company.get_text()
    return company


def company_location(data):
    location = data.find('p', class_='location')
    location=location.get_text()
    location=location.strip()
    return location


def find_date(data):
    date=data.find('time').get_text()
    return date


def learn_apply_url(data):
    learn = re.search('href=.+target', str(data)).group()
    learn = re.search('".*"', learn).group()
    learn = re.sub('"', '', learn)
    return learn



html_doc=requests.get('https://realpython.github.io/fake-jobs/')
# print(html_doc)
# html_doc='http://example.webscraping.com/'
soup = BeautifulSoup(html_doc.content, 'html.parser')
#
# print(soup.prettify())

content=list(soup.children)
x= soup.find_all('div',class_='column is-half')
# print(x[0])
data=x[0]

# print(data)
vacancy={}
job_id=1
for data in x:

    # Find the image URL
    imgUrl=img_url(data)

    # Find The Job Title
    job=job_title(data)

    # Find the company Name
    company=company_name(data)

    # Find the company location
    location=company_location(data)

    # Find Date
    date=find_date(data)

    # Find learn and apply links
    y=(data.find_all('a'))
    learn=y[0]
    apply=y[1]
    learn=learn_apply_url(learn)
    apply=learn_apply_url(apply)
    # print(imgUrl)
    # print(job)
    # print(company)
    # print(location)
    # print(date)
    # print(learn)
    # print(apply)
    img= Image.open(requests.get('https://files.realpython.com/media/real-python-logo-thumbnail.7f0db70c2ed2.jpg?__no_cf_polish=1', stream=True).raw)
    vacancy['Job Id {}'.format(job_id)]={'Position':job,'img':img,'Company':company,'Location':location,'Date':date,'Link to apply':apply,'Link to Learn':learn}
    job_id+=1


for i,k in vacancy.items():
    print(i,':',k)