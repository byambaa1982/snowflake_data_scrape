import pandas as pd
from csv import writer
import json


f = open ('/content/sample.json', "r") 
  
# Reading from file 
data = json.loads(f.read()) 


mydic={'urls':data['urls'], 'date':data['date'], 'question_author':data['question_author'], 'question_title':data['question_title'], 'question_body':data['question_body'], 'answer_count':data['answer_count'], 'question_views':data['question_views'], 'answer_block':data['answer_block'], 'best_answer':data['best_answer']}


df = pd.DataFrame.from_dict(mydic, orient='index')
df1=df.transpose()


df1.to_csv('/data_v2.csv', index=False)