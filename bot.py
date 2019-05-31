from dotenv import load_dotenv
import os
import tweepy
import time
import random

load_dotenv()

consumer_key = os.environ.get('API_KEY')
consumer_secret = os.environ.get('API_SECRET_KEY')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# plural for status?
stati = [
    'but at what cost?',
    'but at what cost?',
    'but at what cost?',
    'but at what cost?',
    'but at what Aaron',
    'bUt At WhAt CoSt?',
    'BUT AT WHAT COST!?',
    'but at what COST?',
    'Aar-- ...I mean - but at what cost?',
    'But. At. What. Cost?',
    'しかし、いくら？'
]

last_tweet_id = 0
with open('last_tweet_id') as f:
    last_tweet_id = int(f.readline())

while True:
    aaron_timeline = api.user_timeline(
        user_id=14761655, since_id=last_tweet_id)

    for result in aaron_timeline:
        if result.id > last_tweet_id:
            print('Found a new Tweet')
            with open('last_tweet_id', 'w') as f:
                f.write(str(result.id))
            last_tweet_id = result.id
            if result.in_reply_to_status_id == None:
                try:
                    print('Replying...')
                    status = random.choice(stati)
                    api.update_status(
                        status=status,
                        in_reply_to_status_id=result.id,
                        auto_populate_reply_metadata=True
                    )
                    print('Done.')
                except Exception as e:
                    print('Something went wrong.')
            else:
                print("It's a reply, ignoring...")
            
    time.sleep(10)