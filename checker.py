# coding: UTF-8
import json
import urllib.request
# import twitter

USER_ASK_FILE = "user.ask.json"
USER_BID_FILE = "user.bid.json"
TWITTER_KEY_FILE = "twitter_key.json"
RATE_URL = "https://bitflyer.jp/api/echo/price"

def get_bitcoin_rate():
    """
    Bitcoinの現在レート取得
    """
    request = urllib.request.urlopen(RATE_URL)
    return json.loads(request.read())

def get_user_data(file_name):
    """
    ローカル保存データ取得（ユーザごとレート情報）
    """
    file = open(file_name, "r")
    user_list = json.load(file)
    return user_list

def save_user_data(file_name, user_list):
    """
    ローカル保存
    """
    file = open(file_name, "w")
    json.dump(user_list, file)

def create_ask_messgage(user):
    """
    買い時通知メッセージの作成
    """
    msg = "@" + user["name"] + " BitcoinのASKが%s以下になりました" % user["ask"]
    return msg

def create_bid_messgage(user):
    """
    売り時通知メッセージの作成
    """
    msg = "@" + user["name"] + " BitcoinのBIDが%s以上になりました" % user["bid"]
    return msg

def get_twitter_key():
    """
    ローカルのtwitterの各種Keyを取得
    """


if __name__ == "__main__":
    rate = get_bitcoin_rate()

    user_list = get_user_data(USER_ASK_FILE)
    # 通知対象者の取得（登録askと現在レートのaskを比較）
    target_user_list = list(filter(lambda user: rate["ask"] <= user["ask"], user_list))
    # 通知
    for user in target_user_list:
        print(create_ask_messgage(user))
    # 今回通知対象ではなかったユーザのみ取得
    remain_user_list = [user for user in user_list if user["name"] not in [target["name"] for target in target_user_list]]
    # ローカルファイルを上書きする
    save_user_data(USER_ASK_FILE, remain_user_list)


    user_list = get_user_data(USER_BID_FILE)
    # 通知対象者の取得（登録bidと現在レートのbidを比較）
    target_user_list = list(filter(lambda user: rate["bid"] >= user["bid"], user_list))
    # 通知
    for user in target_user_list:
        print(create_bid_messgage(user))
    # 今回通知対象ではなかったユーザのみ取得
    remain_user_list = [user for user in user_list if user["name"] not in [target["name"] for target in target_user_list]]
    # ローカルファイルを上書きする
    save_user_data(USER_BID_FILE, remain_user_list)

