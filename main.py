import random
import tweepy
import json
import codecs

# トークンとかの情報は機密情報なので、この場所にJSONを置いてください
token_path = 'secret/token.json'

# jsonを取得
json_open = open(token_path, 'r')
# jsonに変換
json_load = json.load(json_open)

#必要なトークンなど取得
BEARER_TOKEN = json_load['BEARER_TOKEN']
CONSUMER_KEY = json_load['CONSUMER_KEY']
CONSUMER_SECRET = json_load['CONSUMER_SECRET']
ACCESS_TOKEN = json_load['ACCESS_TOKEN']
ACCESS_SECRET = json_load['ACCESS_SECRET']

# 認証
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET,
    wait_on_rate_limit=True
)

# tweetlistにツイートしたい内容を入力していきます
# 「,」で区切ることで、複数登録できます
tweetlist=['はじめまして', 'かんざき', 'みみねこ', 'こんにちは', 'う', 'ね', 'おはよう', 'おやすみ', 'みんな', 'あ', 'みみざきです', '愛してる']
# リストに含まれるツイート内容をランダムで2つ繋げてツイート
separate_str = '　'
new_tweet = random.choice(tweetlist) + separate_str + random.choice(tweetlist)

# ファイルに保存
log_path = 'data/log.txt'
with codecs.open(log_path, 'a', 'utf-8') as f:
    print(new_tweet, file=f)

# ツイート作成
client.create_tweet(text=new_tweet)

# コンソールに出力
print(new_tweet)
