import tweepy

ACCESS_TOKEN = "1115463269735653377-FNDF3x6irJ6Pzjc3zj3HzSXqbNKXvA"
ACCESS_TOKEN_SECRET = "0ahplhRefK3Oa7VjuIKqrtEPFc1zC3DFVoExXDk8Stk2A"
CONSUMER_KEY = "XMdcwozYFOlZh66BGVfd1Ukf3"
CONSUMER_SECRET = "cTKsO4vGfyuLtCw3sdqHsbJSGqRpD62b5Rij8yE77F4GHLpqqG"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

print("Fetching tweets...")

text_file = open("tweets.txt", "w", encoding="utf-8")

places = api.geo_search(query="Trinidad and Tobago", granularity="country")
place_id = places[0].id


for tweet in tweepy.Cursor(api.search, lang="en", geocode="10.4576,-61.2414,90km", q="place:%s" % place_id).items(1000):
    text_file.write(tweet.text + "\n")

text_file.close()

print("Done!\n", "Saved in tweets.txt")