import psycopg2
import pandas as pd
import numpy as np
from amazon.api import AmazonAPI
import requests
import time

def crawl_movie(id):
    amazon = AmazonAPI("AKIAILGCGSOAJBIYFIQA", 
        "xz53Hn0stSpZ2LpqRejomhnZflsqNt/Yhq58VOAK", "ericpan2018-20")
    movie = amazon.lookup(ItemId = id)
    with open('/home/eric/Data/poster/'+id+'.jpg','wb') as f:
        f.write(requests.get(movie.large_image_url).content)
    print(movie.title)
    return movie.title

conn = psycopg2.connect('dbname=movies user=eric password=950519')
sql = 'select productid from moviereview group by productid having count(*) >175'
movieid_list = pd.read_sql_query(sql,con=conn)
conn.close()
movieid_list = list(movieid_list['productid'])



for id in movieid_list:
    try:
        conn = psycopg2.connect('dbname=movies user=eric password=950519')
        cur = conn.cursor()
        sql = "insert into movieid (movieid, moviename) values ('"
        sql = sql+id+"','"+crawl_movie(id)+"')"
        cur.execute(sql)
        time.sleep(1)
        conn.commit()
        cur.close()
        conn.close()
    except:
        continue
