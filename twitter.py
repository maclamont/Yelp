from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "10457942-K9G7Z4UJbXYCIQi90g1XaZYB8EQpdQAj8PDaqHoEg"
access_token_secret = "fLNETXveVFUMLwphkQ8yzdgwM3NhpRzSX2zz0xmdG2jvV"
consumer_key = "oc2jPGD9KD4giDXEannDplMX3"
consumer_secret = "dCsHX4RBC9MKzEm9wLU34NDfKutjIdBJ23aq8MXJLRYB3xiEhc"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['Middlesbrough', 'Downing', '#Believe'])
    stream.filter(track=['restaurant vegas', 'restaurant pittsburgh', 'restaurant edinburgh', 'restaurant montreal', 
    	'restaurant waterloo', 'restaurant karlsruhe', 'restaurant urbana', 'restaurant phoenix', 
    	'restaurant charlotte', 'restaurant madison'])
