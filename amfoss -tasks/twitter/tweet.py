
# we import the module of name tweepy after installing the tweepy at terminal 
import tweepy 
import time
  
# fill the details yu which get after the app created in twitter 
consumer_key ="jPdB3iTvcv9raxM097ODdY0Al"
consumer_secret ="00xPjk8EEcGGn5liESiMjpLu4NgXZUWASGGmU9IFt73khVN4Nb"
access_token ="1052903707187150848-niDarVMptJiyqcfSoVBqeYfGL0SPQO"
access_token_secret ="ilTblRX7MloDOM6CjPkz8kMzfFt708gslCfvFqN5sJL1v"

print("welcome to twitter...")
time.sleep(2)
print("you already loged in named AJAY PRABHAKAR account")


#getting authentication of Aouth. 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 
  
string = str(raw_input("enter tweet: "))

# update the status because we are tweeting so it has to update so give update_status  
api.update_status(status =string) 
print("sending your tweet....")
time.sleep()
print("updated your tweet")
