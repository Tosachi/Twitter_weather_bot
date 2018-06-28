import tweepy
import get_auth
import get_weather


class Listener(tweepy.StreamListener):

  def __init__(self, api):
    super().__init__(api)
    self.me = self.api.me()
    print("weather bot streaming!")

    # 特定の文字列に対してリプを返す処理
  def on_status(self, status):
    tweet_text = status.text

    if (not status.retweeted) and ("RT @" not in tweet_text) and not(str(status.user.screen_name) == "WeatherGirlBot"):
      if "@WeatherGirlBot" in tweet_text:
        if "天気" in tweet_text:
          weather = get_weather.GetWeather(tweet_text)
          tweet = "@" + str(status.user.screen_name) + "\n" + weather.make_tweet()        

        else:
          tweet = "@" + str(status.user.screen_name) + "\n" + "やっほー❗️お天気お姉さんです✨"
          tweet += "\nリプライで対応している都市名と知りたい日(今日か明日か明後日)の天気を聞かれたら答えます♪"
          # tweet += "\n対応している都市名はこちら👇\n"

        try:
          api.update_status(tweet, status.id)  # ツイート！
          # if "対応" in tweet:
          #   api.update_with_media(filename='./texts/areas.png',status=text)
        except:
          print("Tweet Error…")
          
        print(status.user.name + " @" + str(status.user.screen_name))
        print(tweet_text)
        print("-> " + tweet)
        print("-------------------")
            
    return

  def on_event(self, event):
    # 自動フォロー
    try:
      if event.event == "follow":
        if self.me.id != event.source["id"]:
          source_user = event.source
          event._api.create_friendship(source_user["id"])
          print("-- {0} {1} にフォローされました！".format(source_user["name"], source_user["screen_name"]))
    except:
      print("Follow Error…") 

  def on_error(self, status_code):
      print('Got an error with status code: ' + str(status_code))
      return True

  def on_timeout(self):
      print('Timeout…＞＜')
      return True

def tweet_streaming():

  
  auth = get_auth.auth()
  global api
  api = tweepy.API(auth)

  listener = Listener(api)

  stream = tweepy.Stream(auth, listener, secure=True)
  stream.userstream(async=True)