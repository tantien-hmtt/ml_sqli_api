from flask import Flask, jsonify, request
import sqlite3
from modelLoad import predict_sqli_attack
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def get_user_by_uid(uid):
    # Kết nối đến cơ sở dữ liệu SQLite
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Truy vấn dữ liệu của user dựa trên uid
    cursor.execute('SELECT * FROM users WHERE uid = ?', (uid,))
    user_data = cursor.fetchone()

    # Đóng kết nối đến cơ sở dữ liệu
    conn.close()
    return user_data

def get_user_by_username(username):
    # Kết nối đến cơ sở dữ liệu SQLite
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Truy vấn dữ liệu của user dựa trên username
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user_data = cursor.fetchone()

    # Đóng kết nối đến cơ sở dữ liệu
    conn.close()

    return user_data
@app.route('/get_user_by_id', methods=['GET'])
def get_user():
    # Nhận giá trị uid từ tham số truy vấn
    uid_to_query = request.args.get('uid')

    # Kiểm tra xem uid có hợp lệ hay không
    if not uid_to_query or not uid_to_query.isdigit():
        return jsonify({'error': 'Invalid UID parameter'}), 400

    if ( predict_sqli_attack(request.url)): 
        return jsonify({'error': 'Detect malicious url,call api failed'}), 400
    uid_to_query = int(uid_to_query)

    # Gọi hàm để lấy thông tin user
    user_info = get_user_by_uid(uid_to_query)

    # Kiểm tra xem có dữ liệu hay không và trả về thông tin nếu có
    if user_info:
        response_data = {
            'uid': user_info[0],
            'username': user_info[1],
            # 'password': user_info[2],
            'phone': user_info[3]
        }
        return jsonify(response_data)
    else:
        return jsonify({'message': 'Không tìm thấy thông tin cho UID {}.'.format(uid_to_query)}), 404
@app.route('/get_user_by_username', methods=['GET'])
def get_user_by_username_route():
    # Nhận giá trị username từ tham số truy vấn
    username_to_query = request.args.get('username')

    # Kiểm tra xem username có hợp lệ hay không
    if not username_to_query:
        return jsonify({'error': 'Invalid username parameter'}), 400

    if ( predict_sqli_attack(request.url)): 
        return jsonify({'error': 'Detect malicious url, call api failed'}), 400
    # Gọi hàm để lấy thông tin user
    user_info = get_user_by_username(username_to_query)

    # Kiểm tra xem có dữ liệu hay không và trả về thông tin nếu có
    if user_info:
        response_data = {
            'uid': user_info[0],
            'username': user_info[1],
            # 'password': user_info[2],
            'phone': user_info[3]
        }
        return jsonify(response_data)
    else:
        return jsonify({'message': 'Không tìm thấy thông tin cho username {}.'.format(username_to_query)}), 404
@app.route('/users', methods=['GET'])
def get_all_users():
    try:
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        
        user_list = []
        for user in users:
            user_dict = {
                'uid': user[0],
                'username': user[1],
                'phone': user[3]
            }
            user_list.append(user_dict)

        conn.close()

        return jsonify({'users': user_list})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
