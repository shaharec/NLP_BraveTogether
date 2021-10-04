import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(
        sntwitter.TwitterSearchScraper('from:@HolohoaxExposed').get_items()):
    if i > 5000:
        break
    #tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
    tweets_list2.append([tweet.date, tweet.id, tweet.content])

# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text'])
tweets_df2.to_csv('fake.csv')