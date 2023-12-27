import sqlite3

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

if __name__ == "__main__":
    # Nhập uid từ người dùng hoặc từ một nguồn nào đó
    uid_to_query = int(input("Nhập uid cần truy vấn: "))

    # Gọi hàm để lấy thông tin user
    user_info = get_user_by_uid(uid_to_query)

    # Kiểm tra xem có dữ liệu hay không và in ra thông tin nếu có
    if user_info:
        print("Thông tin của user với uid {}:".format(uid_to_query))
        print("uid:", user_info[0])
        print("username:", user_info[1])
        print("password:", user_info[2])
        print("phone:", user_info[3])
    else:
        print("Không tìm thấy thông tin cho uid {}.".format(uid_to_query))
