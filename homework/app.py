from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name = request.form['name_give']
    count = request.form['count_give']
    address = request.form['address_give']
    phone = request.form['phone_give']

    dict = {'name': name, 'count': count, 'address': address, 'phone': phone}
    db.orders.insert_one(dict)

    return jsonify({'msg': '저장완료'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.orders.find({}, {'_id': False}))
    return jsonify({'all_orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
