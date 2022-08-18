stringo="""
import snscrape.modules.twitter as sntwitter
import pandas as pd
import argparse
import sys
import os

parser = argparse.ArgumentParser(description='This tool use for tweeter keyword analyse', epilog='Enjoy the program! :)' )
parser.version = '1'
parser.add_argument("-t", "--tag", help = "Tag must be string", required=True)
#parser.add_argument("-c", "--country", help = "Tag must be string", required=True)

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
args = parser.parse_args()
tag = args.tag 
#country = args.country if args.country else " " 


def scrapetweet(tag):
    # On peut récupérer plusieurs attributs du tweet
    tag=tag
    tweets = []
    limit = 60

    #for tweet in sntwitter.TwitterSearchScraper(str(tag+" "+'near:'+'"'+country+'"')).get_items():
    for tweet in sntwitter.TwitterSearchScraper(tag).get_items():

        # print(vars(tweet))
        # break
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date, tweet.user.username, tweet.renderedContent, 
						   tweet.user.description, tweet.content, tweet.user.followersCount, 
						   tweet.likeCount, tweet.retweetCount, tweet.replyCount, 
						   tweet.user.friendsCount, tweet.user.location])

    df = pd.DataFrame.from_records(tweets, columns=['Date', 'User', 'Rendered Content', 'Description', 
													'Tweet', 'Number of followers', 'Count of likes', 
													'Count of retweets', 'Count of replies', 
													'Number of friends', 'Location'])
    df.to_csv(tag+'.csv', mode='a', index=False)

sleep=1 #(1 seconde)
while True:
    try:
        scrapetweet(tag)
        time.sleep(sleep*60)
    except:
        pass
"""

