from bs4 import BeautifulSoup as BS 
import requests
# from fake_useragent import UserAgent
import sys
import re
from csv import writer
from selenium import webdriver
import time
import json


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


fetch_questions_overview_links()



