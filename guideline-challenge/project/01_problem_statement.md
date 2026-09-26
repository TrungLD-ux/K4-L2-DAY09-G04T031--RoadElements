# Problem statement + downstream contract

## Bài toán
Gán bounding box và trạng thái của cụm đèn giao thông dành cho xe cơ giới điều khiển hướng đi thẳng của xe mang camera. Đầu ra dùng huấn luyện/đánh giá mô hình perception nghiên cứu ADAS; annotation ảnh tĩnh không đủ để quyết định điều khiển xe thực tế.

## Output và scope
- Một cụm vỏ vật lý = một rectangle `traffic_light`; `state`: red, green, yellow, off, unknown; `needs_review`: true/false. Không bàn giao giá trị `__undefined__`.
- Chỉ gán cụm hướng về dòng xe đi thẳng có chiều rộng VÀ chiều cao phần nhìn thấy đều ≥10 px trên ảnh gốc. Không đoán ý định rẽ.
- Loại đèn đi bộ, đèn rẽ chuyên dụng, đèn quay lưng/cắt ngang, phản chiếu, đèn xe/đường và cụm dưới ngưỡng.
- Box ôm phần vỏ nhìn thấy, kể cả chụp che nắng; không chứa cột/dây/halo/vệt nhòe, không nội suy phần bị che. Không thấy vỏ nhưng xác định được cụm thật: khoanh lõi tín hiệu, bật review. Biên rõ có dung sai mục tiêu ≤2 px mỗi cạnh; biên không rõ phải review.

## Quyết định và rủi ro
LABEL = tạo box; IGNORE = không tạo box; UNKNOWN = state unknown kèm review; ESCALATE = needs_review true. Nếu không thể xác định một vùng để vẽ có căn cứ, ghi CVAT issue để QA xử lý trước export.
Sai đỏ thành xanh hoặc nhầm đèn rẽ với đèn đi thẳng là critical. QA owner Lê Danh Trung phối hợp Gold owner Nguyễn Lê Thế Anh chốt ca khó; không giải quyết được thì chuyển Lab Coach.

## Dữ liệu và giới hạn
Ảnh BDD100K/LISA từ data/catalog.csv, chia trong sample_pack.csv. BDD có mưa, đêm, đèn xa và phản chiếu. LISA cùng chuỗi gần giống nhau: blind test đo chuyển giao guideline trong bài học, không chứng minh tổng quát hóa theo scene độc lập.