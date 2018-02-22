
import psycopg2
from gensim.models import Doc2Vec
import pandas as pd
from scipy.spatial import distance
from numpy import linalg as LA

conn = psycopg2.connect('dbname=movies user=eric password=950519')



model = Doc2Vec.load('/home/eric/Data/doc2vec2.model')



def check(char):
    if((ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90)) or (ord(char)>=48 and ord(char)<=57):
        return True
    else:
        return False

def similarity(tag,genre):
    return distance.euclidean( model.wv[genre],model.docvecs[tag])/LA.norm( model.wv[genre])/LA.norm(model.docvecs[tag])

def find_genre(movie):
    genre = []
    genre_list= ['action','romance','epic','political','fiction','comedy','crime','documentary','drama','venture','horror','fantasy']
    for i in genre_list:
        genre.append({'genre':i,'prob':similarity(movie,i)})
    genre = sorted(genre, key=lambda x: x['prob'])
    return [genre[0]['genre'],genre[1]['genre'],genre[2]['genre']]

def out_similar(movieid):
    #print(movieid)
    result = []
    
    movieid = movieid.strip('').strip('\n')
    #print(movieid)
    similar_list = model.docvecs.most_similar(movieid,topn = 70)
    for i in similar_list:
        duplicate = 0
        name = i[0]
       # print(name)
        if len(i[0]) == 10:
        #    print('fail')
            continue
        for index in range(0,len(result)//2):
         #   print(index)
            temp_name = ''.join(filter(check, name)).lower()
            temp_j = ''.join(filter(check, result[2*index])).lower()
            if temp_j in temp_name:
                duplicate = 1
                break
            if temp_name in temp_j:
                result[2*index] = name 
                duplicate = 1
                break
        if duplicate == 1 or len(name) >30:
            continue
        
        result.append(name)
        sql = "select movieid from productname where moviename= '" +name+ "'"
        movieidtemp = pd.read_sql_query(sql, con= conn)
        result.append(list(movieidtemp['movieid'])[0])
    sql = "select movieid from productname where moviename= '" +movieid+ "'"
    movieidtemp = list(pd.read_sql_query(sql, con= conn)['movieid'])[0]
    genre = find_genre(movieid)
    sql = "select reviewtext,reviewsummary from moviereview where length(reviewtext) >500 and length(reviewtext) < 700 and productid= '" +movieidtemp+ "'"
    temp = pd.read_sql_query(sql, con= conn)
    review = list(temp['reviewtext'])[0]
    summary = list(temp['reviewsummary'])[0]
    with open('/home/eric/python/flaskr/flaskr/movielist','r') as f:
        x = f.read().split('\n')
    #print(result)
    output= [movieid]+[movieidtemp]+result[:12]+[genre,review,summary,x]
    return output


result = []
count = 0
with open("/home/eric/python/flaskr/flaskr/movielist") as i:
    for name in i.readlines():
        count= count +1
        movie = name.strip("\n")
        result.append(out_similar(movie))
        if count % 100 ==0:
            print (count)
    df = pd.DataFrame(result)
    df.to_json('/home/eric/Data/result.json')