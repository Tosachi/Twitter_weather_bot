# お天気お姉さんbot  
  
リプライで対応する地域の今日または明日または明後日の天気を尋ねると返信してくれるbot。  
また、対応している都市をランダムに選んで朝6時に今日の、夜23時に明日の天気を呟く。  
情報はlivedoorのWeather Hacksから。 
日と都市は複数選択することができるが、文字数の関係でそれぞれ2個まで、合計で3個までしか指定できない。  

(成功する反応リプライ例)  
『大阪の明日の天気を教えて』  
『大阪と東京の今日の天気は？』  
『東京の明日と明後日の天気が知りたい』  

## 環境  
MacBook Air  
Python 3.6.4  

## サーバー
raspberry pi 3  
  
## 使用したライブラリ  
tweepy (Twiiterに接続)  
random (絵文字を選ぶ)  
urllib (livedoorのWeather Hacksに接続)  
apscheduler (定期ツイートのためのスケジューラ)  
datetime (現在時刻を取得)  
os (ディレクトリの移動)  
sys (エラーが出た時処理を終了)  
json (サイトから情報を取ってくる時使う)  
  
## ディレクトリ構造  

```
.  
├── texts/ 
│     ├── area_codes.txt  
│     ├── weather_emoji.txt      
│     ├── good_emoji.txt         
│     ├── bad_emoji.txt          
│     ├── morning_msgs.txt       
│     └── evening_msgs.txt       
│                                
├── run.py (実行ファイル)    
│                       
├── get_weather.py  
│                       
├── streaming.py  
│                
├── get_auth.py  
│                         
├── env.py(ignore) 
│  
├── .gitignore  
│  
└──README.md  
```

## ファイルの呼び出し関係
(呼び出す側) <- - - (呼び出される側)  

### リプライ時
```
run.py <- - - streaming.py <- - - get_weather.py <- - - texts/
              streaming.py <- - - get_auth.py <- - - env.py

```

### 定期ツイート時
```
get_weather.py - - -> run.py (実行ファイル) <- - - get_auth.py <- - - env.py(ignore)  
```

## それぞれのファイル・ディレクトリの説明
### texts/
必要なテキストを入れているファイル。get_weather.pyで呼び出して配列やディレクトリに格納する。  
それぞれのファイルは次のようになっている。  
・area_codes.txt・・・対応都市名と都市コード。  
・weather_emoji.txt・・・天気とそれに対応する天気の絵文字。  
・good_emoji.txt・・・語尾につける絵文字。  
・bad_emoji.txt・・・申し訳ない時語尾につける絵文字。  
・morning_msgs.txt・・・朝の定期ツイートの最後につけるメッセージ。　　
・evening_msgs.txt・・・夜の定期ツイートの最後につけるメッセージ。  

### run.py
実行ファイル。定期ツイートのためのスケジューラーを設定している。  
定期ツイートの時はこのファイルを直接Twitterに繋いでいる。  
リプライの時はstreaming.pyから呼び出す。

### streaming.py
Tweepyを用いてTwitterに接続し、UserStreamを使ってタイムラインを取得、ツイート本文を解析して該当ツイート(botへのリプライ)があればそれに対してリプライを返す。下記に示す[条件分岐](#条件分岐)の1と2はここで行われる。  
ツイート内容はget_weather.pyのmake_tweet()にツイートのテキスト本文を渡して解析してリプライを読み込み、ツイートする。  

### get_weather.py
テキストを開いて配列に格納したり、livedoorのWeather Hacksに接続して天気の情報を取得するファイル。実はこのファイルが一番重要。  
下記に示す[条件分岐](#条件分岐)の3と4はこのファイル内で行われる。  

### get_auth.py
Twitterに接続するために必要な情報を作成。env.pyから各種APIキーを読み込む。  

### env.py
[Twitter Application Management](https://apps.twitter.com/)から取得した各種APIキーを返り値とする関数を書いているファイル。個人情報なのでgitignoreしている。get_auth.pyで呼び出される。  
  

## 条件分岐  
1.リプライに対して反応  
2.リプライに'天気'という単語が含まれている場合ツイート内容を解析  
3.対応する地域名が入っていなかった場合、入れてからやり直すよう返す  
4.対応する地域名が入っていた場合、対応する日が入っているかチェック  
　入っていなかった場合今日の天気を返す  
　入っていた場合その日の天気を返す  

## 参考  
[Pythonで天気予報をLINE通知する](https://qiita.com/kutsurogi194/items/6b9c8d37b2b83fc2ce87)  
[Tweepyでたこ焼きbotを作った](https://moko-freedom.hatenablog.com/entry/2018/06/24/210112)
