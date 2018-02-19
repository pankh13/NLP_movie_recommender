from amazon.api import AmazonAPI
import requests

def crawl_movie(id):
    amazon = AmazonAPI("AKIAILGCGSOAJBIYFIQA", 
        "xz53Hn0stSpZ2LpqRejomhnZflsqNt/Yhq58VOAK", "ericpan2018-20")
    movie = amazon.lookup(ItemId = id)
    print(movie.title)
    with open('./poster/'+id+'.jpg','wb') as f:
        f.write(requests.get(movie.large_image_url).content)


id = 'B003AI2VGA'

crawl_movie(id)


