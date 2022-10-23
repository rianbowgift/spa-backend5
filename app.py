from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.hes4dp3.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)



@app.route('/')
def home():


    return render_template('index.html')


@app.route("/bucket", methods=["POST"])
def bucket_post():




    target_receive = request.form['target_give']

    bucket_users = list(db.bucket.find({}, {'_id': False}))
    count = len(bucket_users) +1


    doc = {
        'target' : target_receive,
        'id' : count,
        'complete' : 0
    }
    db.bucket.insert_one(doc)

    return jsonify({'msg': '등록 완료'})


@app.route("/bucket/done", methods=["POST"])
def bucket_done():


    id_receive = request.form['id_give']

    db.bucket.update_one({'id': int(id_receive)}, {'$set': {'complete': 1}})

    return jsonify({'msg': '달성 완료!'})



@app.route("/bucket", methods=["GET"])
def bucket_get():

    buckets = list(db.bucket.find({}, {'_id': False}))


    return jsonify({'bucket': buckets})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
