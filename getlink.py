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

url='https://snowflakecommunity.force.com/s/global-search/%40uri#q=snowflake&first=40&t=All&sort=relevancy&f:Type=[Answers]'

def get_page_html(url):

    try:
        browser = webdriver.Chrome()
        browser.get(url)
        htmlContent = browser.page_source
        time.sleep(9)
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

# soup = BeautifulSoup(open("output1.html"), "html.parser")
# soup=get_page_html(url)
# data={}
# data["full_url"]=[]
# with open("link_v5.txt", "w") as file:
# 	all_links=soup.find_all("a", class_="CoveoResultLink")
# 	for i in range(len(all_links)):
# 		# data['title'].append(all_links[i].text)
# 		# data['links'].append(all_links[i].get('href'))
# 		data["full_url"].append("https://snowflakecommunity.force.com"+all_links[i].get("href")+"/"+space_to_dash(all_links[i].text))
# 	file.write(str(data))

soup=get_page_html(url)
data={}
data["full_url"]=[]
with open("sample.json", "w") as outfile:
	all_links=soup.find_all("a", class_="CoveoResultLink")
	for i in range(len(all_links)):
		# data['title'].append(all_links[i].text)
		# data['links'].append(all_links[i].get('href'))
		data["full_url"].append("https://snowflakecommunity.force.com"+all_links[i].get("href")+"/"+space_to_dash(all_links[i].text))
	# Serializing json  
	json_object = json.dumps(data, indent = 1) 
	outfile.write(json_object )



