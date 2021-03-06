from apscheduler.schedulers.blocking import BlockingScheduler
import get_weather
import streaming
import tweepy
import get_auth

# スケジューラー
sched = BlockingScheduler()

@sched.scheduled_job("cron", hour="6,23")
def scheduled_job():
  weather = get_weather.GetWeather("")
  tweet = weather.regular_tweet()
  # Twitterに接続
  auth = get_auth.auth()
  api = tweepy.API(auth)
  # ツイート
  api.update_status(tweet)
  
if __name__ == "__main__":
  streaming.tweet_streaming()
  sched.start()