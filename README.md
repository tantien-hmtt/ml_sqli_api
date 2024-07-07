Machine Learning-Based Detection of API Attacks – SQL Injection
Mục lục
Giới thiệu
Phân tích và thiết kế hệ thống
Giải pháp
Triển khai
Kết quả và hướng phát triển
Tài liệu tham khảo
Giới thiệu
1. Lý do chọn đề tài
SQL Injection là một trong những loại tấn công nguy hiểm nhất mà các hệ thống hiện nay thường xuyên phải đối mặt. Đề tài này được chọn nhằm tăng cường nhận thức về tầm quan trọng của việc ngăn chặn và phát hiện các cuộc tấn công vào API, đặc biệt là SQL Injection. Việc áp dụng machine learning trong việc phát hiện các loại tấn công này có thể mang lại khả năng tự bảo vệ cao hơn và giúp bảo vệ thông tin nhạy cảm cũng như duy trì tính toàn vẹn của hệ thống.

2. Ngữ cảnh
Trong bối cảnh phát triển mạnh mẽ của công nghệ thông tin và sự phổ biến của các ứng dụng dựa trên API, việc bảo vệ an ninh thông tin không chỉ đòi hỏi sự cải tiến liên tục mà còn yêu cầu sự sáng tạo và ứng dụng những công nghệ tiên tiến nhất. SQL Injection attacks là một trong những mối đe dọa nguy hiểm nhất đối với an ninh hệ thống, đặc biệt là đối với các hệ thống dựa trên API với việc xử lý dữ liệu và truy vấn cơ sở dữ liệu.

Phân tích và thiết kế hệ thống
1. Các bên liên quan
Data users: Những người có quyền sử dụng dữ liệu trong database, cho phép truy cập và tải xuống dữ liệu để phục vụ trong công việc.
API: Nhận dữ liệu đầu vào từ người dùng, xử lý và tạo các truy vấn SQL để gửi đến database.
Backend Service: Bao gồm nhiều thành phần liên quan đến backend server như backend service, database và mục tiêu chính là dữ liệu từ database.
Attacker: Người truyền vào những câu lệnh truy vấn cho API.
2. Các kịch bản tấn công
Kịch Bản 1: SQL Injection Attacks
Trong kịch bản này, hacker sẽ cố gắng chèn hoặc thay đổi các truy vấn SQL không an toàn thông qua các trường nhập liệu trong các API của hệ thống. Điều này có thể dẫn đến việc truy cập trái phép vào cơ sở dữ liệu hoặc thậm chí làm thay đổi, xóa bỏ hoặc lấy thông tin quan trọng.

Kịch Bản 2: Tampering with API Requests
Kẻ tấn công có thể cố gắng sửa đổi hoặc làm giả các yêu cầu API, thay đổi thông tin gửi đi hoặc lợi dụng lỗ hổng để thực hiện các hành động không mong muốn trong hệ thống.

Kịch Bản 3: Information Disclosure
Kẻ tấn công có thể sử dụng SQL Injection hoặc các kỹ thuật khác để thu thập thông tin nhạy cảm từ cơ sở dữ liệu hoặc từ các yêu cầu API, gây ra rủi ro về việc tiết lộ thông tin cá nhân hoặc dữ liệu quan trọng.

3. Tài sản cần bảo vệ
Dữ liệu cơ sở dữ liệu: Thông tin cá nhân của người dùng, thông tin tài chính, đơn hàng, thông tin y tế và các dữ liệu quan trọng khác được lưu trữ trong cơ sở dữ liệu của hệ thống.
API Endpoints và Dịch Vụ: Các API endpoints và dịch vụ cung cấp truy cập và tương tác với dữ liệu, thông tin của người dùng và chức năng hệ thống.
Hệ Thống và Dịch Vụ Quan Trọng: Bảo vệ hoạt động ổn định của hệ thống, chức năng và dịch vụ quan trọng của ứng dụng dựa trên API khỏi các cuộc tấn công có thể làm mất ổn định hoặc gây ảnh hưởng tiêu cực.
4. Mục tiêu bảo mật
Ngăn chặn cuộc tấn công: Mục tiêu chính của bảo mật là ngăn chặn các cuộc tấn công vào cơ sở dữ liệu hoặc làm thay đổi thông tin, bảo vệ dữ liệu và tính toàn vẹn của hệ thống.
Bảo vệ dữ liệu nhạy cảm: Đảm bảo rằng thông tin cá nhân của người dùng và dữ liệu nhạy cảm khác được lưu trữ và truyền tải một cách an toàn, không bị tiết lộ hay bị sửa đổi bởi kẻ tấn công.
Tăng cường bảo mật hệ thống: Nâng cao khả năng phát hiện và ngăn chặn các cuộc tấn công thông qua việc triển khai các biện pháp bảo mật mạnh mẽ và thường xuyên cập nhật, kiểm tra lại hệ thống để đảm bảo an toàn liên tục.
Giải pháp
1. Kiến trúc hệ thống
Nhóm đề xuất một kiến trúc về Web API có tích hợp module detection vào việc xử lý và phát hiện các request khi API, nhận dạng các request có an toàn hay không trước khi thực hiện các bước tiếp theo như xác thực, phân quyền.

2. Module phát hiện tấn công
Đề xuất xây dựng một module để có thể lọc các API call từ phía user bằng cách sử dụng machine learning để nhận diện các HTTPS request call có chứa SQL injection.

3. Cơ sở lý thuyết
SQL Injection: SQL injection là một lỗ hổng bảo mật trên web cho phép kẻ tấn công can thiệp vào các truy vấn mà ứng dụng thực hiện đối với cơ sở dữ liệu. Điều này có thể cho phép kẻ tấn công xem dữ liệu mà họ thông thường không thể truy xuất được.
API: API là cơ chế cho phép hai thành phần phần mềm giao tiếp với nhau bằng một tập hợp các định nghĩa và giao thức. API gateway là một công cụ quản lý API nằm giữa các máy khách và backend service, hoạt động như một reverse proxy, chấp nhận tất cả các lệnh gọi API, tìm nạp và tổng hợp các tài nguyên thích hợp trước khi gửi phản hồi cho mỗi yêu cầu API.
Triển khai
1. Chuẩn bị dataset
Chuẩn bị dữ liệu từ các nguồn để đào tạo mô hình, bao gồm các mẫu dữ liệu bình thường và dữ liệu có chứa các dấu hiệu của SQL Injection. Các bước này bao gồm:

Thu thập dữ liệu: Từ các nguồn đáng tin cậy và bao gồm cả các dữ liệu được gán nhãn.
Tiền xử lý dữ liệu: Làm sạch dữ liệu, chuẩn hóa các định dạng và chuyển đổi các dạng dữ liệu phù hợp để đưa vào mô hình.
Lưu ý: Hình ảnh về dữ liệu thô và quy trình tiền xử lý

2. Train model và đưa model vào hệ thống
Đào tạo mô hình machine learning bằng cách sử dụng dataset đã chuẩn bị. Các bước bao gồm:

Chọn mô hình: Sử dụng các thuật toán machine learning như Random Forest, SVM, hoặc neural networks.
Đào tạo mô hình: Sử dụng dataset để đào tạo mô hình và tinh chỉnh các siêu tham số.
Đánh giá mô hình: Kiểm thử mô hình với dữ liệu kiểm tra để đánh giá độ chính xác, độ nhạy và các chỉ số khác.
Lưu ý: Hình ảnh về biểu đồ đánh giá hiệu suất mô hình

3. Kiểm thử và Đánh giá
Kiểm thử hệ thống với các dữ liệu mới để đánh giá hiệu suất của mô hình và khả năng phát hiện các tấn công SQL Injection.

Kiểm thử với dữ liệu thực tế: Sử dụng dữ liệu thực tế từ môi trường triển khai để đánh giá mô hình.
Đánh giá và cải thiện: Phân tích kết quả kiểm thử để cải thiện mô hình và hệ thống.
