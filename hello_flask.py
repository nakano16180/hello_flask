# encoding: utf-8
from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

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

@app.route('/api/test')
def get_foobar():
    return 'you got\n'

@app.route('/api/test/<int:baz>', methods=['POST'])
def post_foobar(baz):
    return 'you posted {}\n'.format(baz)

@app.route('/api', methods=['GET'])
def get_json_from_dictionary():
    dic = {
        'foo': 'bar',
        'ほげ': 'ふが'
    }
    return jsonify(dic)  # JSONをレスポンス

@app.route('/api', methods=['POST'])
def post_json():
    json = request.get_json()  # POSTされたJSONを取得
    return jsonify(json)  # JSONをレスポンス

if __name__ == '__main__':
    # webサーバー立ち上げ
    app.run(host='0.0.0.0', port=port)
