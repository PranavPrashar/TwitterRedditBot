import praw
import tweepy
import time

from credentials import *

tw_auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
tw_auth.set_access_token(twitter_access_token, twitter_access_token_secret)
tw_api = tweepy.API(tw_auth)


my_reddit = praw.Reddit(client_id=reddit_client_id, client_secret=reddit_client_secret, user_agent=reddit_user_agent)
sub_name = 'Coronavirus'
max_posts = 10




for submission in my_reddit.subreddit(sub_name).new(limit=max_posts):
    	
	# print(submission.title)
	# # print(submission.id)
	# print('Link to article' , str(submission.url))
	# # print('Author',str(submission.author))
	# print("\n")
	output = submission.title 
	output2 = "Link to article:" + str(submission.url)
	outputFinal = submission.title + "\n" + str(submission.url) + "\n"
	# print(output , '\n' , output2)
	print(outputFinal)
	tw_api.update_status(status=outputFinal) 

	

	

