import tweepy, json, pandas as pd, matplotlib.pyplot as plt, seaborn as sns, re
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")
    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        if self.num_tweets < 1000:
            return True
        else:
            return False
        self.file.close()
    def on_error(self, status):
        print(status)
            

access_token = "user_acess_token" 
access_token_secret = "user_access_token_secret"
consumer_key = "user_consumer_key"
consumer_secret = "user_consumer_secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


l = MyStreamListener()
stream = tweepy.Stream(auth,l)


stream.filter(track=['argentina','bolivia','brasil'])


tweets_data_path= 'tweets.txt'
tweets_data=[]
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    tweet=json.loads(line)
    tweets_data.append(tweet)
tweets_file.close()
print(tweets_data[0].keys())



# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=["text","lang","created_at","place","geo"]) # or other parameters view api.twitter


def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True
    return False


[argentina, bolivia, brasil] = [0, 0, 0]

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    argentina += word_in_text('argentina', row['text'])
    bolivia += word_in_text('bolivia', row['text'])
    brasil += word_in_text('brasil', row['text'])

# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['argentina','bolivia', 'brasil']

ax = sns.barplot(cd,[argentina, bolivia, brasil])
ax.set(ylabel="count")
plt.show()