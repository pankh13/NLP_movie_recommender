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

sql = 'select productid from moviereview where productid in (select productid from moviereview group by productid having count(*) >175)'
movieid_list = pd.read_sql_query(sql,con=conn)
with open('/home/eric/Data/idlist','w',encoding = 'utf-8') as f:
    for i in list(movieid_list['productid']):
        f.write(i+'\n')


sql = 'select reviewtext from moviereview where productid in (select productid from moviereview group by productid having count(*) >175)'
movieid_list = pd.read_sql_query(sql,con=conn)

with open('/home/eric/Data/reviewlist','w',encoding = 'utf-8') as f:
    for i in list(movieid_list['reviewtext']):
        f.write(i+'\n')
