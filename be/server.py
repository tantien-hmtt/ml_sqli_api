# import  pymongo 
# from flask import Flask 
# from flask import request,jsonify
# from flask_cors import CORS

# myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
# mydb = myclient['task4']
# mycul = mydb['users']

# app = Flask(__name__)
# cors = CORS(app)
# app.config["CORS_HEADERS"] = "Content-Type"

# @app.route("/Push", methods = )
from dataConfig import get_data
from predict import predict_sqli_attack
from flask import Flask, request, jsonify

app = Flask(__name__)



data = get_data() 

@app.route('/api', methods=['GET'])
def api_endpoint():
    try:
        # Lấy URL từ request
        client_url = request.url
        print("url call by client: " + client_url)
        # Thực hiện validation trước khi xử lý API
        ####################
        
        ####################
        result = predict_sqli_attack(client_url)
        print( "result of redict: " + str((result)))
        if (result): 
            return "message :API call failed"
        else: 
            return jsonify(data)
        # Thực hiện các công việc cụ thể của API tại đây
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400

if __name__ == '__main__':
    app.run(debug=True)
