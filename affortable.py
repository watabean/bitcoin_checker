# coding: UTF-8
import json
import urllib.request
# import twitter

USER_TEST_FILE = "users.test.json"
USER_FILE = "users.json"
TWITTER_KEY_FILE = "twitter_key.json"
RATE_URL = "https://bitflyer.jp/api/echo/price"

def get_bitcoin_rate():
    """
    Bitcoinの現在レート取得
    """
    request = urllib.request.urlopen(RATE_URL)
    return json.loads(request.read())

def get_user_data():
    """
    ローカル保存データ取得（ユーザごとレート情報）
    """
    file = open(USER_TEST_FILE, "r")
    user_list = json.load(file)
    return user_list

def save_user_data(user_list):
    """
    ローカル保存
    """
    file = open(USER_FILE, "w")
    json.dump(user_list, file)

def create_messgage(user):
    """
    通知メッセージの作成
    """
    msg = "@" + user["name"] + " Bitcoinのレートが%s以下になりました" % user["ask"]
    return msg

def get_twitter_key():
    """
    ローカルのtwitterの各種Keyを取得
    """


if __name__ == "__main__":
    user_list = get_user_data()
    rate = get_bitcoin_rate()
    # 通知対象者の取得（登録askと現在レートのaskを比較）
    target_user_list = list(filter(lambda user: rate["ask"] <= user["ask"], user_list))

    # 通知
    for user in target_user_list:
        print(create_messgage(user))
    
    # 今回通知対象ではなかったユーザのみ取得
    remain_user_list = [user for user in user_list if user["name"] not in [target["name"] for target in target_user_list]]
    # ローカルファイルを上書きする
    save_user_data(remain_user_list)
