# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variables that contains the user credentials to access Twitter API
access_token = "18085421-dEQ1vKhaD1uyyIjQe8vqUwx9LoS5nrjtehW7jIZes"
access_token_secret = "yl7qFnakwlkECs0UK0VgwCpwoDAREIvGjLexGCPGJpBq5"
consumer_key =  "hXmAXvq8X9wbAD7PNdKr0AkZ6"
consumer_secret = "mtWFMPtb3m9Mmpo2Mjqg7spaxaTJubrDesQqqhkLdCJgZgU0MU"


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
