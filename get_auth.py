import tweepy
import env

def auth():

  CK = env.CONSUMER_KEY()
  CS = env.CONSUMER_SECRET()
  AT = env.ACCESS_TOKEN()
  AS = env.ACCESS_TOKEN_SECRET()

  auth = tweepy.OAuthHandler(CK, CS)
  auth.set_access_token(AT, AS)

  return auth
