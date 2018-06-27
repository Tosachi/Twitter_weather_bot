from apscheduler.schedulers.blocking import BlockingScheduler
import get_weather
import streaming
import tweepy
import get_auth

# スケジューラー
sched = BlockingScheduler()

# UTCなのでJSTに変える
@sched.scheduled_job("cron", hour="15,8")
def scheduled_job():
  weather = get_weather.GetWeather("")
  tweet = weather.regular_tweet()
  auth = get_auth.auth()
  api = tweepy.API(auth)
  api.update_status(tweet)
  
if __name__ == "__main__":
  streaming.tweet_streaming()
  sched.start()