# フィボナッチ数列の計算結果を返すREAT APIの開発

私はAWSのEC2でサーバを構築して実行しました。

## 手順１：pythonとFlaskのインストール

ex)
sudo apt install python-is-python3
sudo pip install flask

## 手順２；コードのクローン

ex)
git clone https://github.com/shunyanaka/fibonacci_api.git

## 手順３：実行

ex)
cd fibonacci_api
sudo flask --app app run --port 80 --host 0.0.0.0

sudo: 「Super User DO」の略で、管理者（スーパーユーザー）権限でコマンドを実行するために使用されます。これにより、通常は許可されない操作が可能になる。

flask --app app: この部分はFlaskにどのアプリケーションを実行するかを指示。ここではappという名前のアプリケーションを指定。

run: Flaskアプリケーションを実行するためのコマンド。

--port 80: このオプションで、アプリケーションがリッスンするポートを指定。ポート80はHTTPのデフォルトポート。

--host 0.0.0.0: このオプションで、アプリケーションがどのネットワークインターフェースを使って外部からの接続を受け入れるかを指定。0.0.0.0はすべての利用可能なインターフェースを意味し、外部のどのホストからもアクセスできるようにする。
