import sqlite3
from faker import Faker

fake = Faker()

# Kết nối đến cơ sở dữ liệu SQLite (nếu không tồn tại, sẽ được tạo mới)
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Tạo bảng trong cơ sở dữ liệu
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        uid INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT,
        phone TEXT
    )
''')

# Tạo đối tượng admin đầu tiên
admin_data = (1, 'admin', fake.password(), fake.phone_number())
cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?)', admin_data)

# Tạo 9 đối tượng khác
for uid in range(2, 11):
    user_data = (uid, fake.user_name(), fake.password(), fake.phone_number())
    cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?)', user_data)

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()

print("File data.db đã được tạo thành công.")
