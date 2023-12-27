# Sử dụng ảnh chứa Python
FROM python:3.10

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy mã nguồn vào container
COPY . /app

# Cài đặt các dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose cổng mà Flask sẽ chạy
EXPOSE 5000

# Chạy ứng dụng khi container được khởi động
CMD ["python", "app.py"]