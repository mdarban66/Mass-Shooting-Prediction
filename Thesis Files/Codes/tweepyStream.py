#!/usr/bin/python3
from socket import error as SocketError
import errno
import csv
from tweepy import Stream
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import API, Cursor
import tweepy
import json
import codecs
import datetime
import time
#import httplib2
import http.client

# authentication data- get this info from twitter after you create your application
ckey = 'RJV3xIuafaKHJJkSHHN9e6VOg'               
csecret = 'anuaG514244rHSci0gkAhArDVlXWPawUoEtxAsVSe2nCc917Fz'             
atoken = '2448058249-a26wuiSGM1vShfGa30ykjvxlM1kM9mvEO8VUVcj'  
asecret = 'TXKysvOo74tnyeFBWkWIZF7StukQTYrfu4EBLtbrtViy0'     

count = 0
#x=time.strftime("%d-%m-%Y")+'streamResult'
file1 = open('StreamTestTextFile.txt', 'a', encoding = 'utf-8')

#csvFile = open(x+'.csv', 'a')
#csvFile = open('streamResult    .csv', 'a')
#csvWriter = csv.writer(csvFile)

#csvWriter.writerow(["User ID", "Screen Name", "Language", "Statuses Count", "Friends Count", "User Name", "Time Zone", "Location", "Following", "Followers Count", "Listed Count", "Follow Req Sent", "Status ID", "Text", "Created At", "Geo", "Coordinates", "Place", "In Reply to UID", "Source", "Is Quote Status", "Favorite Count", "In Reply to UID", "In Reply to SID", "In Reply to ScreenName", "Retweeted", "Retweet Count", "Hashtags", "URLs", "User Mentions"])

class listener(StreamListener): 

	
	def on_data(self, data):
		global count
		decoded = json.loads(data)
		x=time.strftime("%d-%m-%Y")+'streamResult'
		
		#x=time.strftime("%d-%m-%Y %H:%M")+'streamResult'
		csvFile = open(x+'.csv', 'a')
		csvWriter = csv.writer(csvFile)
		
		
		#fileWhole = open('wholeTweets.txt', 'a')
		##with open('%s_tweets.csv' % screen_name, 'a') as f:

		
		try:						
			##writer = csv.writer(f)
			#csvWriter.writerow([data])
			#csvWriter.writerow([str(data.source)])

			
			file1.write("\n\n______________________________________________________________\n\n")
			file1.write("\n ***************************"+str(count)+"****************************")
			file1.write(data)

			csvWriter.writerow(["UID:"+str(decoded['user']['id']), "ScrName:"+str(decoded['user']['screen_name']), "Lang:"+str(decoded['user']['lang']), "StatsCnt:"+str(decoded['user']['statuses_count']), "FriendsCnt:"+str(decoded['user']['friends_count']), "UName:"+str(decoded['user']['name']),"TimeZone:"+str(decoded['user']['time_zone']), "Location:"+str(decoded['user']['location']), "Following:"+str(decoded['user']['following']), "FollowersCnt:"+str(decoded['user']['followers_count']), "ListedCnt:"+str(decoded['user']['listed_count']), "FollowReqSent:"+str(decoded['user']['follow_request_sent']), "SID:"+str(decoded['id']), "Text:"+str(decoded['text'].encode('ascii', 'ignore')), "CreatedAt:"+str(decoded['created_at']), "Geo:"+str(decoded['geo']), "Coordinates:"+str(decoded['coordinates']), "Place:"+str(decoded['place']), "InReplyToUID:"+str(decoded['in_reply_to_user_id']), "Src:"+str(decoded['source']), "IsQuoteStat:"+str(decoded['is_quote_status']), "FavoriteCnt:"+str(decoded['favorite_count']), "InReplyToSID:"+str(decoded['in_reply_to_status_id']), "InReplyToScrName:"+str(decoded['in_reply_to_screen_name']), "Retweeted:"+str(decoded['retweeted']), "RetweetCnt:"+str(decoded['retweet_count']), "Hashtags:"+str(decoded['entities']['hashtags']), "URL:"+str(decoded['entities']['urls']), "UsrMentions:"+str(decoded['entities']['user_mentions'])])


			#fileWhole.write('***************************\n')
			#fileWhole.write(data)
				
			
			##writer.writerows(outtweets)
				#fileWhole.write('\n***************************')
				#fileWhole.write(str(count))
				#fileWhole.write('***************************\n')
				#fileWhole.write(data)
			
			
			print ('_______________________',str(count),'____________________________')
			print (data)   
			count += 1
			return True
			csvWriter.close()
			
		except tweepy.TweepError:
			#filewhole.write('\n\nfailed on data, waiting for 15 minutes...\n')
			print ('failed on data, waiting for 15 minutes...')  
			time.sleep(60*15)  

		except StopIteration:
			#fileWhole.write('\nBreak...\n')
			print('break')
#			break

		#except:
		#	print("Error!!!")
		#	print("waiting for 2 minutes....")
		#	fileWhole.write("\n waiting for 15 minutes")
		#	fileWhole.flush()
		#	time.sleep(60*15)

	def on_error(self, status):
		print (status)
		print("waiting for 60 seconds...")
		time.sleep(60)


# authenticate yourself
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
while True:
	try:
		
		twitterStream = Stream(auth, listener())
		twitterStream.filter(locations=[-180,-90,180,90])
	
	except KeyboardInterrupt:
		twitterStream.disconnect()
		break
	
	except:
		#fileWhole.write('\n\nIncompleteRead Error!!!\n')
		print('IncompleteRead Error!!!')
		#time.sleep(60)
		continue
