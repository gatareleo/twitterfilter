import pandas as pd
import tweepy
import re

# Set up API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Read in CSV file and create dataframe
df = pd.read_csv('hashtags.csv')

# Search for tweets containing the hashtag
hashtags = []
for tweet in tweepy.Cursor(api.search, q='#hashtag').items(100):
    hashtags.extend(re.findall(r'#\w+', tweet.text))

# Check if hashtag already exists in CSV file
for hashtag in hashtags:
    if not df['hashtags'].str.contains(hashtag).any():
        df = df.append({'hashtags': hashtag}, ignore_index=True)

# Save updated CSV file
df.to_csv('hashtags.csv', index=False)
