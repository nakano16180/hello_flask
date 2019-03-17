# encoding: utf-8
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/ja')
def hello_world_ja():
    return 'こんにちは 世界！'

@app.route("/index")
def index():
    return render_template('index.html') #/indexにアクセスが来たらtemplates内のindex.htmlが開きます

if __name__ == '__main__':
    # webサーバー立ち上げ
    app.run()
