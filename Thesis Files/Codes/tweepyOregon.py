import tweepy
import io
import time
import json
import csv
#import unicodecsv
#from unidecode import unidecode
#import urllib2

totalCount=0
counter = 0
consumer_key = 'RJV3xIuafaKHJJkSHHN9e6VOg'
consumer_secret = 'anuaG514244rHSci0gkAhArDVlXWPawUoEtxAsVSe2nCc917Fz'
access_token = '2448058249-a26wuiSGM1vShfGa30ykjvxlM1kM9mvEO8VUVcj'
access_token_secret = 'TXKysvOo74tnyeFBWkWIZF7StukQTYrfu4EBLtbrtViy0'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#file1 = open('/media/mona/My Passport/Tweepy-TwitterData/OregonGunShooting/GunTweetsApr27.txt', 'a'  , encoding = 'utf-8')
file1 = open('/home/mona/Desktop/Untitled Folderget/Tweepy-API/Search-API/GunTweetsApr27.txt', 'a'  , encoding = 'utf-8')

#csvFile = open('/media/mona/My Passport/Tweepy-TwitterData/OregonGunShooting/CSV/GunTweetsApr25.csv', 'a')
csvFile = open('/home/mona/Desktop/Untitled Folderget/Tweepy-API/Search-API/GunTweetsApr27.csv', 'a')

csvWriter = csv.writer(csvFile)
csvWriter.writerow(["User ID", "Screen Name", "Language", "Statuses Count", "MetaData", "Contributors", "Friends Count", "User Name", "Time Zone", "Location", "User.Created At", "Following", "Followers Count", "Listed Count", "Follow Req Sent", "Geo Enabled", "Status ID", "Text", "Created At", "Geo", "Coordinates", "Place", "In Reply to UID", "Source", "Is Quote Status", "Favorite Count", "In Reply to SID", "In Reply to ScreenName", "Retweeted", "Retweet Count", "URLs", "User Mentions", "Hashtags"])

#public_tweets = api.home_timeline()
#tweets = []

#for tweet in public_tweets:
#    tweets.append(json.loads(tweet))
language=['en', 'ar']
keyWords=['gun violence', 'mass shooting', 'NRA', 'highschool shooting']

cricTweet = tweepy.Cursor(api.search, q="gun violence OR mass shooting OR NRA OR highschool shooting", since="2016-04-27", until="2016-04-28", lang="en").items(1000000000)

print(str(cricTweet))

while True:
	try:
		for tweet in cricTweet:
			hashtags = ""
			try:

				#placeHolder = []
				#placeHolder.append(tweet.id.encode('utf8'))
				#placeHolder.append(tweet.screen_name.encode('utf8'))
				#placeHolder.append(tweet.created_at)

				#prefix = 'TweetData_lungCancer'
				#wholeFileName = prefix + suffix     
				#with open('newfile.txt', 'a'  , encoding = 'utf-8'): # changeable here
				#	file1.write(placeHolder)
					#writeFile.writerow(placeHolder)

#					counter2 += 1

#					if counter2 == 4000:
#						time.sleep(60*20) # wait for 20 min everytime 4,000 tweets are extracted 
#						counter2 = 0
#						continue
				
				file1.write("\n\n______________________________________________________________\n\n")
				file1.write("\n ***************************"+str(totalCount)+"****************************")
				file1.write(tweet.created_at.strftime("\n\n %Y-%m-%d %H:%M:%S")+"\n")
				file1.write(tweet.text+"\n")
				
				file1.write(tweet.lang+"\n")
				file1.write(str(tweet))

				'''urls = []
				urls_data = tweet.entities.get('urls', None)
				if(urls_data != None):
					for i in range(len(urls_data)):
						urls.append((urls_data[i]['url']))'''				

				csvWriter.writerow([tweet.user.id, tweet.user.screen_name, tweet.user.lang, tweet.user.statuses_count,  tweet.metadata, tweet.contributors, tweet.user.friends_count, tweet.user.name, tweet.user.time_zone, tweet.user.location, tweet.user.created_at, tweet.user.following, tweet.user.followers_count, tweet.user.listed_count, tweet.user.follow_request_sent, tweet.user.geo_enabled, tweet.id, tweet.text.encode('utf-8'), tweet.created_at, tweet.geo, tweet.coordinates, tweet.place, tweet.in_reply_to_user_id, tweet.source, tweet.is_quote_status, tweet.favorite_count, tweet.in_reply_to_status_id, tweet.in_reply_to_screen_name, tweet.retweeted, tweet.retweet_count, tweet.entities['urls'],tweet.entities['user_mentions'],tweet.entities['hashtags']])
#(tweet.entities['user_mentions'][j]["id_str"] for j, val in enumerate(tweet.entities["user_mentions"]))])
    
#(tweet.entities["user_mentions"][0]["id_str"] if len(tweet.entities['user_mentions']) >= 1 else None)])#.hashtags.text, tweet.entities.urls, tweet.entities.user_mentions])
				#csvWriter.writerow([str(decoded['user']['id']), str(decoded['user']['screen_name']), str(decoded['user']['lang']), str(decoded['user']['statuses_count']), str(decoded['user']['friends_count']), str(decoded['user']['name']),str(decoded['user']['time_zone']), str(decoded['user']['location']), str(decoded['user']['following']), str(decoded['user']['followers_count']), str(decoded['user']['listed_count']), str(decoded['user']['follow_request_sent']), str(decoded['id']), str(decoded['text'].encode('ascii', 'ignore')), str(decoded['created_at']), str(decoded['geo']), str(decoded['coordinates']), str(decoded['place']), str(decoded['in_reply_to_user_id']), str(decoded['source']), str(decoded['is_quote_status']), str(decoded['favorite_count']), str(decoded['in_reply_to_user_id']), str(decoded['in_reply_to_status_id']), str(decoded['in_reply_to_screen_name']), str(decoded['retweeted']), str(decoded['retweet_count']), str(decoded['entities']['hashtags']), str(decoded['entities']['urls']), str(decoded['entities']['user_mentions'])])
				counter += 1
				totalCount += 1
				if counter == 2000:
					file1.write("\n\nAlready Got 2000 tweets\n")
					time.sleep(60*2)
					counter = 0
					continue

			except tweepy.TweepError:
				file1.write("waiting for 15 minutes!!!")
				time.sleep(60*15)
				continue

			except IOError:
				file1.write("IO Error Happened!")
				time.sleep(60*2.5)
				continue

			except StopIteration:
				file1.write("Iteration Stopped! Breaking")
				print('break')
				break

			except:
				file1.write("waiting for 15 minutes...")
				time.sleep(60*15)
				continue

	
	except tweepy.TweepError as e:
		#crictweet.next()
		#print(e.args[0][0]['code'])
		#if e.response:
		#print "error response code: " + str(e.response.status)
		#print "error messate: " + str(e.response.reason)
		print(e.response.content)
		print("Errored....")
		file1.write("waiting for 15 minutes")
		#print(str(tweepy.TweepError))
		file1.flush()
		csvFile.flush()
		time.sleep(60*15) 		
