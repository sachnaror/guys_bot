import tweepy
import time


# Authenticate to Twitter

# API_KEY="XxUAkAiKE0FqCfpFBDvXDzDZ2"
# API_SECRET="OIMYimUCKPmbCUTNf3mnfAWzRW75kssEjJcVs45FKTxwmF5ZI1"
# ACCESS_TOKEN = "48283064-iyf4zKODSjU0RvEgakLWTgNp1kPnea7TOzSI2AU2Q"
# ACCESS_SECRET = "bNtmMOQpCfnN5H1rZWIqL4e5Wa8Ee4YIaorCvgZN3Ow9H"

API_KEY="KU2at7JyMXIU2JuGBXLJmMLWG"
API_SECRET="sZTsoVPD5nr6K6T9VEqznWBJ0QMVZgtvdf2L7Y4OM2Cic6fpSd"
ACCESS_TOKEN = "1075083604353564672-cLflZ6xF9eip3ed30sH0ZtWPWlQu2c"
ACCESS_SECRET = "V806nMVgfY4y47WGRwOnu4L0tYxgfSQWZEx4bkaRfcUER"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

# list
def like(id):
    try:
        api.create_favorite(id)
    except Exception as ex:
        print(ex)

# Create API object

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.replied_tweets = []
        self.api = api

    def on_status(self, status):
        print("==========================================================")
        message="Hey I liked this tweet of yours. We have an active opening for fullstack Engineers. Please DM me; will provide all details t.ly/4diY,and/or if you can support me by retweeting this or spread the word I will be thankful.Show your support pls."
        tweet_id=status.id
        if tweet_id in self.replied_tweets:
            print("already seen this tweet: ", status.text)
        else:
            like(tweet_id)
            time.sleep(30*60)

            self.api.update_status(message,in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)
            
            print("replied to tweet: {}\n".format(status.text))
            print("==========================================================")
            self.replied_tweets.append(tweet_id)
        
        if len(self.replied_tweets) >= 1000:
            self.replied_tweets = []
    
# tweets = api.mentions_timeline()
# for tweet in tweets:
#     tweet.favorite()
#     tweet.user.follow()
if __name__ == "__main__":
    tweets_listener = MyStreamListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    print("streaming...")
    stream.filter(track=['javatype','typescript', 'vue', 'vuejs', 'vue3', 'tailwindcss', 'javascript'], languages=["en"])
    print("after stream...")