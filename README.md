---
title: "Data Scrape: snowflake Q&A"
date: 2020-04-20 11:33:00 +0800
categories: [Data Scrape, Python]
tags: [pandas, lambda, scraping]
---


All code is in [my github](https://github.com/byambaa1982/snowflake_data_scrape/blob/master/)

## Goal

I am asked to scrape and extract data [this website](https://snowflakecommunity.force.com/s/global-search/%40uri#q=snowflake&t=All&sort=relevancy&f:Type=[Answers]) 


### Data that we need to scape

index| Urls       |Date  |Author of question| Question Title| Question body| count| views |answer| Best Anser 
-----| -----------| -----| ----------------|---------------|---------------|------|-------|------|-----------
0   | www.url1.com| date1| name 1          | title 1       | question body | 123  | 2345  | ans1 | best anwer
1   | www.url2.com| date2| name 2          | title 2       | question body | 123  | 2345  | ans2 | best anwer 
2   | www.url3.com| date3| name 3          | title 3       | question body | 123  | 2345  | ans3 | best anwer        

### Code explained 

#### File 1


```python  
from bs4 import BeautifulSoup as BS 
import requests
```

```python
def space_to_dash(a_str):
	a_str=re.sub(" ", "-", a_str.lower())
	return a_str
```

```python
def get_page_html(url):

    try:
        browser = webdriver.Chrome()
        browser.get(url)
        htmlContent = browser.page_source
        time.sleep(6)
        # browser.quit()
    except Exception as e:
        print('[!] Network error...')
        print(e)
        sys.exit()
    soup = BS(htmlContent, 'html.parser')
    return soup
```

```python
def fetch_links():
	soups=[]
	for url in urls:
		soup = get_page_html(url)
		soups.append(soup)
		print(url)
	return soups
```

```python 
data={}
data["full_url"]=[]
with open("the_links.json", "w") as outfile:
	for i in range(4,100):
		try:
			url='https://snowflakecommunity.force.com/s/global-search/%40uri#q=snowflake&first='+str(i*10)+'&t=All&sort=relevancy&f:Type=[Answers]'
			soup=get_page_html(url)
			all_links=soup.find_all("a", class_="CoveoResultLink")
			for i in range(len(all_links)):
				data["full_url"].append("https://snowflakecommunity.force.com"+all_links[i].get("href")+"/"+space_to_dash(all_links[i].text))
		except: 
				print("no page found!!!")
	print("Total scraped links are {}".format(len(data["full_url"])))
	# Serializing json  
	json_object = json.dumps(data, indent = 1) 
```
#### File 2

```python
f = open ('the_links.json', "r")  
# Reading from file 
data = json.loads(f.read()) 
urls=data['full_url']


def get_page_html(url):

    try:
        browser = webdriver.Chrome()
        browser.get(url)
        htmlContent = browser.page_source
        time.sleep(9)
        browser.quit()
    except Exception as e:
        print('[!] Network error...')
        print(e)
        sys.exit()
    soup = BS(htmlContent, 'html.parser')
    return soup


def fetch_questions_overview_links():
	data={}
	data["urls"]=[]
	data["date"]=[]
	data["question_author"]=[]
	data["question_title"]=[]
	data["question_body"]=[]
	data["answer_count"]=[]
	data["question_views"]=[]
	data["answer_block"]=[]
	data["best_answer"]=[]
	with open("data_v1.json", "w") as outfile:
		for url in urls:
			try:
				soup = get_page_html(url)
				data["urls"].append(url)
				data["date"].append(soup.find('div', class_='cuf-subPreamble slds-text-body--small').text)
				data["question_author"].append(soup.find('div', class_='cuf-preamble slds-grid slds-grid--align-spread slds-has-flexi-truncate').text)
				data["question_title"].append(soup.find('div', class_='cuf-body cuf-questionTitle forceChatterFeedBodyQuestionWithoutAnswer').text)
				data["question_body"].append(soup.find('div', class_='cuf-body cuf-questionBody forceChatterFeedBodyQuestionWithoutAnswer').text)
				data["question_views"].append(soup.find('li', class_='slds-item cuf-viewCount qe-viewCount').text)
				answers=soup.find_all('article', class_='forceChatterComment')
				a_bodies=[]
				for i in range(1,len(answers)):
					a_bodies.append(answers[i].text) 
				data["answer_block"].append(a_bodies)
				data["best_answer"].append(answers[0].text)
			except: 
				print("no page found!!!")
		json_object = json.dumps(data, indent = 9) 
		outfile.write(json_object)
```


If you have anything to ask, please contact me clicking following link?


You can hire me [here](https://www.fiverr.com/coderjs)

Thank you