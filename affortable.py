# coding: UTF-8
import json
import urllib.request

USER_FILE = "users.json"
RATE_URL = "https://bitflyer.jp/api/echo/price"

def getBitCoinRate():
    """
    Bitcoinの現在レート取得
    """
    request = urllib.request.urlopen(RATE_URL)
    return json.loads(request.read())

def getUserData():
    """
    ローカル保存データ取得（ユーザごとレート情報）
    """
    file = open(USER_FILE, "r")
    userList = json.load(file)["users"]
    return userList

def createMessgage(user):
    """
    通知メッセージの作成
    """
    msg = "@" + user["name"] + " Bitcoinのレートが%s以下になりました" % user["ask"]
    return msg


if __name__ == "__main__":
    userList = getUserData()
    rate = getBitCoinRate()
    
    # 通知対象者の取得
    targetUserList = list(filter(lambda user: user["ask"] >= rate["ask"], userList))
    # 通知
    for user in targetUserList:
        print(createMessgage(user))