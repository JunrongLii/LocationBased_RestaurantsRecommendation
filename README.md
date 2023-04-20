# LocationBased_RestaurantsRecommendation

# main
The user would be asked if they want to get their own key from Yelp and personalize the program, if they do, they just need to input the key and 
their location. The user could find the way to create the account here "https://docs.developer.yelp.com/docs/fusion-intro".
The program will help the user to retrieve the data from yelp and cache the data as well. The text in the data will also be processedfor recommendation, 
data would be also be cached after it was processed.

# yelp_api
The program uses default key and location which is NYC to retreive the info about 1000 restaurants. Since there is a rate limit, 5000 calls would be 
the maximum and calls over 5000 might cause error. After the data was retrived, it will be cached into JSON file.

# cacheRestaurants_info
The data will be pre-processed after this program was run, it will also be cached into CSV file. 

# locationBasedRecommendation
The data was processed in this program, after it was processed, it also would be cached into CSV file. The similarity between restaurants and similarity
between restaurants and user's description will be obtained after this program was run.

# dataStructureGraph
Graph was used as data structure. The nodes represent the name of restaurants, the edges represent the similarity between restaurants. After this program was run, there would a HTML file containing network of restaurants was created and added to the path.

# timeout_article
The articles about restaurants would be retrieved from website "https://www.timeout.com/newyork/food-drink" and be cached into JSON file.



