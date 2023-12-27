from pymongo import MongoClient 
from bson import ObjectId
from flask import jsonify
client = MongoClient("mongodb://127.0.0.1:27017/")
db = client['task4']
def get_data():
    # Chọn collection
    collection = db['users']  # Thay 'ten_collection' bằng tên collection thực tế

    users = list(collection.find({}, {'_id': 0}))
    # Lấy dữ liệu từ collection
    #data = list(collection.find())
    return users


