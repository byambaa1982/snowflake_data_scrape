from bs4 import BeautifulSoup as BS 
import requests
# from fake_useragent import UserAgent
import sys
import re
from csv import writer
from selenium import webdriver
import time
import json
import pandas as pd


f = open ('link_v4.txt', "r") 
  
# Reading from file 
data = json.loads(f.read()) 
  
# Iterating through the json 
# list 
for i in data['full_url']: 
    print(i) 
  
# Closing file 
f.close()

a='https://snowflakecommunity.force.com/s/question/0D50Z00006uSiSdSAK/user-defined-function-udf-to-return-a-value'
b='https://snowflakecommunity.force.com/s/question/0D50Z000081KgLqSAK/how-do-privileges-impact-the-results-of-querying-views-in-informationschema'
c='https://snowflakecommunity.force.com/s/question/0D50Z00008MpXgpSAF/does-snowflake-support-pass-through-authentication-from-3rd-party-tool'






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


def fetch_links():
	soups=[]
	for url in urls:
		soup = get_page_html(url)
		soups.append(soup)
		print(url)
	return soups

def scrape_data():

	soups = fetch_links()
	# soups = BS(open("output1.html"), "html.parser")
	print("scraping data now...")
	print(len(soups))
	data={}
	data['urls']=[]
	data['question_author']=[]
	data['question_title']=[]
	data['question_body']=[]
	data['answer_count']=[]
	data['question_views']=[]
	data['answer_block']=[]
	data['best_answer']=[]
	with open('data.txt', 'w') as file:
		for soup in soups:

			try:
				questioner=(soup.find('div', class_='cuf-preamble slds-grid slds-grid--align-spread slds-has-flexi-truncate').text)
				question=(soup.find('div', class_='cuf-body cuf-questionTitle forceChatterFeedBodyQuestionWithoutAnswer').text)
				question_body=(soup.find('div', class_='cuf-body cuf-questionBody forceChatterFeedBodyQuestionWithoutAnswer').text)
				total_answer=(soup.find('li', class_='slds-item qe-commentCount').text)
				total_view=(soup.find('li', class_='slds-item cuf-viewCount qe-viewCount').text)

				answers=soup.find_all('article', class_='forceChatterComment')
				a_bodies=[]
				for i in range(1,len(answers)):
					a_bodies.append(answers[i].text)    
				print(len(a_bodies))
				data['urls'].append(url)
				data['question_author'].append('questioner')
				data['question_title'].append('question')
				data['question_body'].append('question_body')
				data['answer_count'].append('total_answer')
				data['question_views'].append('total_view')
				data['answer_block'].append('a_bodies')
				data['best_answer'].append('answers[0].text')
			except: 
				print("no page found!!!")


		file.write(str(data))


def test_soup():
	soups = BS(open("output1.html"), "html.parser")
	for i in soups:
		print(i)

def txt_to_csv():
	# scrape_json()
	data=pd.read_csv('link_v4.txt')
	df=pd.DataFrame('link_v4.txt', columns=data.keys())
	return df.to_csv('link_v4.csv', index=False)

# txt_to_csv()
# fetch_questions_overview_links()
# scrape_data()
# test_soup()

