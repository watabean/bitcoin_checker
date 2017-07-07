# ビットコインチェッカー
# きっかけ
- 販売所しか使ってないけど、指値注文いれておきたい（指値できない）
- 価格さがったときに、軽くチャート見てから買いたい

# 仕様
- twitterbotアカウント
- ユーザはアカウントに対し、メンションを投げる（ビットコインのレート）e.g. ~~@bitcoin 250000~~
- やっぱ売り時も知りたいのでメンションの投げ方は @bitcoin ask 250000 や @bitcoin bid 250000 みたいな感じにする
- アカウントはフォロワーからメンションきたときは、フォロワーのユーザ名とレートをセットで保存（JSON形式などでローカル保存？）
- 1分おきとかでレートをAPIにより取得し、指定されたレートを下回った場合にユーザに対し、メンションを投げる
- 1度通知を投げるとそのユーザ名とレートのセットを削除する
- すでにそのユーザがレートを保存していた場合は上書きする

# 考えること
- メンションorダイレクトメッセージ？
	- 自分の買いたいレートがみんなに見えて大丈夫か？
- データ削除に対応するか否か？
	- @bitcoin delete などで削除する？

# bitflyer
- api仕様 https://bitflyer.jp/corporate/echo
- レート取得 https://bitflyer.jp/api/echo/price

# twitter
- メンション取得 https://syncer.jp/Web/API/Twitter/REST_API/GET/statuses/mentions_timeline/
- ツイート投稿 https://syncer.jp/Web/API/Twitter/REST_API/POST/statuses/update/

# botの作り方
- http://qiita.com/yuki_bg/items/96a1608aa3f3225386b6
- http://qiita.com/yubais/items/dd143fe608ccad8e9f85

# 機能
- ユーザごとのレート保存
	- メンションを取得
	- 最終取得位置保存
	- 文字列が数値か判定
	- 同一ユーザのレートは変更
	- 新規ユーザのレートは登録
- ユーザへの通知
	- レートを取得する
	- ユーザのデータ取得
	- 該当ユーザを抽出
	- tweetする（e.g. ~~@user ビットコインの価格が～となりました~~）
	- 価格を直接出すのはよくなさそうなので、「登録価格を下回りました」とかのメッセージにする
	- jsonファイルから該当ユーザを削除する

