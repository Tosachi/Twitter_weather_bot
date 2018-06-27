#お天気お姉さんbot

リプライで対応する地域の今日または明日または明後日の天気を尋ねると返信してくれるbot。
情報はlivedoorのWeather Hacksから。

#環境
Python 3.6.4

#使用したライブラリ
tweepy (Twiiterに接続)
random (絵文字を選ぶ)
urllib (livedoorのWeather Hacksに接続)
apscheduler (定期ツイートのためのスケジューラ)
datetime (現在時刻を取得)
os (ディレクトリの移動)
sys (エラーが出た時)
json (サイトから情報を取ってくる時)

#ディレクトリ構造

ファイルの呼び出し関係: (呼び出される側) - -> (呼び出す側)

.
├── texts/   - - - - - - - - - - - - - -
│     ├── area_codes.txt               |
│     ├── weather_emoji.txt            |
│     ├── good_emoji.txt               |
│     ├── bad_emoji.txt                |
│     ├── morning_msgs.txt             | 
│     └── evening_msgs.txt             |    
│                                      |
├── get_weather.py  - - - - - -   <- - -                   
│                           |  |
├── run.py (実行ファイル) <- -   | 
│                              |
├── streaming.py  <- - -    <- -
│                      |                         
├── get_auth.py  - - - -   <- - -                
│                               |
├── env.py(ignore)  - - - - - - - 
│
├── .gitignore
│
└──README.md


#条件分岐
・リプライに対して反応
・リプライに'天気'という単語が含まれている場合ツイート内容を解析
・対応する地域名が入っていなかった場合、入れてからやり直すよう返す
・対応する地域名が入っていた場合、対応する日が入っているかチェック
　入っていなかった場合今日の天気を返す
　入っていた場合その日の天気を返す

#参考
[Pythonで天気予報をLINE通知する](https://qiita.com/kutsurogi194/items/6b9c8d37b2b83fc2ce87)
[Tweepyでたこ焼きbotを作った](https://moko-freedom.hatenablog.com/entry/2018/06/24/210112)

