from bs4 import BeautifulSoup as BS 
import requests
# from fake_useragent import UserAgent
import sys
import re
from csv import writer
from selenium import webdriver
import time
import json

def space_to_dash(a_str):
	a_str=re.sub(" ", "-", a_str.lower())
	return a_str

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

def fetch_links():
	soups=[]
	for url in urls:
		soup = get_page_html(url)
		soups.append(soup)
		print(url)
	return soups



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
	outfile.write(json_object )



