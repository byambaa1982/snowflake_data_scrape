from bs4 import BeautifulSoup as BS 
import requests
# from fake_useragent import UserAgent
import sys
import re
from csv import writer
from selenium import webdriver
import time
import json


# driver = webdriver.Chrome()

a='https://snowflakecommunity.force.com/s/question/0D50Z00006uSiSdSAK/user-defined-function-udf-to-return-a-value'
b='https://snowflakecommunity.force.com/s/question/0D50Z000081KgLqSAK/how-do-privileges-impact-the-results-of-querying-views-in-informationschema'
c='https://snowflakecommunity.force.com/s/question/0D50Z00008MpXgpSAF/does-snowflake-support-pass-through-authentication-from-3rd-party-tool'
urls=[a,b,c]



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
	data['urls']=[]
	data['date']=[]
	data['question_author']=[]
	data['question_title']=[]
	data['question_body']=[]
	data['answer_count']=[]
	data['question_views']=[]
	data['answer_block']=[]
	data['best_answer']=[]
	with open("data_v4.txt", "w") as file:
		for url in urls:
			soup = get_page_html(url)
			data['urls'].append(url)
			data['date'].append(soup.find('div', class_='cuf-subPreamble slds-text-body--small').text)
			data['question_author'].append(soup.find('div', class_='cuf-preamble slds-grid slds-grid--align-spread slds-has-flexi-truncate').text)
			data['question_title'].append(soup.find('div', class_='cuf-body cuf-questionTitle forceChatterFeedBodyQuestionWithoutAnswer').text)
			data['question_body'].append(soup.find('div', class_='cuf-body cuf-questionBody forceChatterFeedBodyQuestionWithoutAnswer').text)
			data['answer_count'].append(soup.find('li', class_='slds-item qe-commentCount').text)
			data['question_views'].append(soup.find('li', class_='slds-item cuf-viewCount qe-viewCount').text)
			answers=soup.find_all('article', class_='forceChatterComment')
			a_bodies=[]
			for i in range(1,len(answers)):
				a_bodies.append(answers[i].text) 
			data['answer_block'].append(a_bodies)
			data['best_answer'].append(answers[0].text)
		file.write(str(data))

def txt_to_csv():
	scrape_json()
	df=pd.read_json('data.txt')
	return df.to_csv('data.csv', index=False)




data={}
data['question_author']=[]
data['question_title']=[]
data['question_body']=[]
data['answer_count']=[]
data['question_views']=[]
data['answer_block']=[]
data['best_answer']=[]


from selenium import webdriver
 
driver = webdriver.Firefox()

def get_links():
	for i in range(len(links)):
		time.sleep(2)
		driver.get(links[i])
		time.sleep(3)
		driver.quit()


url = links[0]
soup = BeautifulSoup(requests.get(url).content, "html.parser")
time.sleep(5)
total_answer=(soup.find('li', 'slds-item qe-commentCount').get_text())
print(total_answer)


