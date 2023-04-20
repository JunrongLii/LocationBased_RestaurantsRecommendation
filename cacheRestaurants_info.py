import json
import pandas as pd
from IPython.display import display

CACHE_FILENAME = "cacheRestaurants_info.json"

def open_cache():
    try:
        cache_file = open(CACHE_FILENAME, 'r')
        cache_contents = cache_file.read()
        cache_dict = json.loads(cache_contents)
        cache_file.close()
    except:
        cache_dict = {}
    return cache_dict

def save_cache(cache_dict):
    dumped_json_cache = json.dumps(cache_dict)
    fw = open(CACHE_FILENAME,"w")
    fw.write(dumped_json_cache)
    fw.close()



def main():
    local_cache = open_cache()
    data1 = local_cache
    for i in range(20):
        data1[i]['city'] = []
    for i in range(20):
        j = 0
        while j < 50 :
            data1[i]['city'].append('New York City')
            j += 1
    ids = []
    name = []
    rating = []
    category = []
    pricing = []
    num_reviews = []
    street_address = []
    reviews = []
    city = [] 
    url = []
    for i in data1:
        ids += i['id']
        print(len(ids))
        name += i['name']
        rating += i['rating']
        category += i['category']
        pricing += i['pricing']
        num_reviews += i['num_reviews']
        street_address += i['street address']
        reviews += i['reviews']
        city += i['city']
        url += i['url']
    df = {'id':ids, 'name':name, 'rating':rating, 'category':category, 
          'pricing': pricing,'num_reviews':num_reviews, 'street address':street_address, 
          'reviews':reviews,'city':city,'url':url}
    results = pd.DataFrame(df)
    display(results)
    results.to_csv('results_info.csv')
    print("The basic information about the restaurants was cached in to csv format named 'results_info.csv'")


main()