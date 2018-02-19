import psycopg2
import pandas as pd
import numpy as np


'''
conn = psycopg2.connect('dbname=movies user=eric password=950519')
sql = 'select moviename from movieid'
movieid_list = pd.read_sql_query(sql,con=conn)
conn.close()
movieid_list = list(movieid_list['moviename'])
for i in movieid_list:
    print((i.split('[')[0]).split('(')[0])
'''
conn = psycopg2.connect('dbname=movies user=eric password=950519')
sql = 'select movieid.moviename from movieid ,moviereview where movieid.movieid = moviereview.productid and moviereview.productid in (select productid from moviereview group by productid having count(*) >175)'
movieid_list = pd.read_sql_query(sql,con=conn)
movieid_list = list(movieid_list['moviename'])
dummyList = []
for i in movieid_list:
    #if "(" in i or "[" in i:
    #if "--" in i:
    if "-" in i:
        if i not in dummyList:
            dummyList.append(i)
with open('templist','w') as f:
    for i in dummyList:
        f.write(i+'\n')
print(len(dummyList))
print(len(movieid_list))
