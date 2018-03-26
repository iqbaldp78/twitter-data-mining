from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


access_token = "273774576-LOL4953DUWMz62XZhZqdKH8IGXFacCnD2hyi7xwh"
access_token_secret = "ezDHV9MHnP4Yc8YMeZY7LwAPOgZTBONxyqx5MAvZ4CeM0"
consumer_key = "eDmm8YP3zw6LW2tQm5UvzQiSB"
consumer_secret = "WMlHYOI2F09u1RvxThnEr9Rmmt6fkObAxGY022FKZXEWX5E1ci"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print ("data",data)
        return True

    def on_error(self, status):
        print ("status",status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    # print("stream",stream)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
    # print("stream.filter", stream.filter)