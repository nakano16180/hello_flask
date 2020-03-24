# encoding: utf-8
from flask import Flask, render_template
import os

app = Flask(__name__)

# Bind to PORT if defined, otherwise default to 5000.
port = int(os.environ.get('PORT', 5000))

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/ja')
def hello_world_ja():
    return 'こんにちは 世界！'

@app.route("/index")
def index():
    return render_template('index.html') #/indexにアクセスが来たらtemplates内のindex.htmlが開きます

@app.route("/string")
def string():
    message = 'sample_string'
    return render_template('string.html', message=message)

@app.route("/list")
def list():
    num_list = [1, 2, 3, 4, 5]
    return render_template('list.html', message=num_list)

@app.route("/dictionary")
def dictionary():
    my_dic = {}
    my_dic['name'] = 'fugafuga'
    my_dic['univ'] = 'hogehoge University'
    return render_template('dictionary.html', message=my_dic)

if __name__ == '__main__':
    # webサーバー立ち上げ
    app.run(host='0.0.0.0', port=port)
