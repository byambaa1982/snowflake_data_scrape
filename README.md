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

index|Urls|Date   | Author of question| Question Title| Question body| count | views |answer| Best Anser 
-----| ---| ------| ---|-------------------|---------------|--------------|-------|-------|------|-----------
0   | www.url1.com| date1| name 1          | title 1       | question body | 123  | 2345  | ans1 | best anwer
1   | www.url2.com| date2| name 2          | title 2       | question body | 123  | 2345  | ans2 | best anwer 
2   | www.url3.com| date3| name 3          | title 3       | question body | 123  | 2345  | ans3 | best anwer        

### Code explained 

```python  
from bs4 import BeautifulSoup as BS 
import requests
```


If you have anything to ask, please contact me clicking following link?


You can hire me [here](https://www.fiverr.com/coderjs)

Thank you