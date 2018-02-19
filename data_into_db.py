import io
import requests
import psycopg2
import time
from threading import Thread
import re


file = '/home/eric/Data/movies.txt'

global sql
sql = ''


def execute(sql):
    conn = psycopg2.connect('dbname=movies user=eric password=950519')
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()



count = 0
def read_line(line):
    if(line.split(' ')[0]=="product/productId:"):
        global sql
        sql = "INSERT INTO moviereview (productid,reviewfelphulness,reviewscore,reviewsummary,reviewtext) VALUES ("
        sql = sql + "'"+ line.split(' ')[1].strip('\n')+"',"
    if(line.split(' ')[0]=="review/helpfulness:"):
        sql = sql + "'"+ line.split(' ')[1].strip('\n')+"',"
    if(line.split(' ')[0]=="review/score:"):
        sql = sql + "'"+ line.split(' ')[1].strip('\n')+"',"
    if(line.split(' ')[0]=="review/summary:"):
        content = line[15:].strip('\n')
        content = ("''").join(content.split("'"))
        if len(content) > 200:
            content = 'overflow'
        sql = sql +"'"+ content +"',"
    if(line.split(' ')[0]=="review/text:"):
        content = line[12:].strip('\n')
        content = ("''").join(content.split("'"))
        if len(content) > 5000:
            content = 'overflow'
        sql = sql +"'"+ content+"')"
        execute(sql)
        sql =''
    


#with codecs.open(file, "r",encoding='utf-8', errors='ignore') as in_file:
with open(file,encoding="latin-1") as in_file:
    for line in in_file:
        read_line(line)
        count = count+1
        if count % 100000 ==0:
            print(count)



