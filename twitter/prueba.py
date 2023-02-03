from dotenv import load_dotenv
import os
import tweepy
import json
import csv

load_dotenv()

access_token = os.getenv("ACCESS_TOKEN_twitter")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET_twitter")
consumer_key = os.getenv("CONSUMER_KEY_twitter")
consumer_secret = os.getenv("CONSUMER_SECRET_twitter")

auth = tweepy.OAuthHandler(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
        )

api = tweepy.API(auth)

"""
# datos de mi cuenta
data = api.verify_credentials()
print(json.dumps(data._json, indent=4))
"""

"""
# Obtener información de otro usuario
data = api.get_user(screen_name="riosmauricio")
print(json.dumps(data._json, indent=2))
"""

"""
# Obtener los seguidores de un usuario utilizando cursor
data=api.get_followers(screen_name="nike")
for user in tweepy.Cursor(api.get_followers, screen_name="nike").items(50):
    print(json.dumps(user._json, indent=2))
"""

"""
# Obtener las personas que sigue un usuario utilizando cursor
data=api.get_friends(screen_name="nike")
for user in tweepy.Cursor(api.get_friends, screen_name="nike").items(50):
    print(json.dumps(user._json, indent=2))
"""

"""
# Obtener un timeline (tweets que hizo una personas) de un usuario
for tweet in tweepy.Cursor(api.user_timeline,screen_name="riosmauricio",tweet_mode="extended").items(20):
    print(json.dumps(tweet._json, indent=2))
"""

# Buscar tweets
try:
    specific_tweets = tweepy.Cursor(api.search_tweets, tweet_mode='extended', q="amor", lang='es').items(100)
except tweepy.errors.TweepyException:
    pass
for tweet in specific_tweets:
    extracted_text = tweet.full_text
    if tweet.place is not None:
        geo = tweet.place["bounding_box"]["coordinates"]

    """
    with open('tweets.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([extracted_text, geo])
    """


"""
for tweet in tweepy.Cursor(api.search_tweets, q="Manifiesto Comunista", tweet_mode="extended").items(10):
    #print(json.dumps(tweet._json, indent=2,ensure_ascii=False))
    fullText = tweet.full_text
    text = []
    text.append(fullText)
    print(text)
"""




    





