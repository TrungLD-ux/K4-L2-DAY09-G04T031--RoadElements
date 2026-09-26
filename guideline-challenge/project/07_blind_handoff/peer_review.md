# Đối chiếu export team03 với frozen gold

Nguồn: peer_output/peer_output.zip do người dùng cung cấp. CVAT XML 1.1, job 17, owner username Dai, 5 ảnh và 11 box. Username owner không tự chứng minh người trực tiếp gán; cần peer xác nhận tên người làm. Export ghi 2026-09-26 13:59:43 UTC, sau mốc freeze 08:34:41 UTC. Version Guide lúc peer làm không có trong XML.

Đã chạy lab9.py score, khớp tên/kích thước 5 ảnh và schema. Sau đó đối chiếu tọa độ trên ảnh gốc; chấm thủ công 12 decision trong transfer_score.csv. Không sửa gold, sample pack hoặc ZIP peer.

## Kết quả theo đúng phạm vi gold
- Decision: 8/10 (80%).
- Critical: 2/3 (66.7%); một critical escape ở LISA08: vẽ đèn mũi tên rẽ trái.
- Geometry: 0/2. BDD26 khoanh halo; LISA08 box giữa bỏ phần vỏ/chụp nhô bên trái phía dưới. Đây là đánh giá thị giác của owner từ ảnh gốc, không phải IoU với gold box số học. Gold không cung cấp tọa độ chuẩn; reviewer có thể kiểm lại crop trước chốt.
- Số câu hỏi ước lượng 5–20 do người dùng cung cấp tương ứng I=0 và GTS=61.3. Chi tiết nguồn trong clarification_count.json; chưa có bản ghi từng câu hỏi. Điểm gold không phải accuracy toàn bộ annotation.

## Lỗi ngoài/phụ thêm so với các dòng chấm
BDD18 có một state __undefined__ tại box (656.06;301.90;669.37;314.91), dù needs_review=true. Review không thay thế việc chọn state hợp lệ.
BDD22 có hai box 7.43×11.42 và 7.70×12.32 px; đều state unknown, needs_review=false. Có 2 vi phạm ngưỡng và 2 vi phạm unknown/review. Không nới box để đủ ngưỡng.
BDD26 state green/review true đạt, nhưng geometry còn rộng theo halo; hai khía cạnh được chấm riêng.
LISA08 cần loại cụm mũi tên. Việc các box khác đều red không bù được lỗi scope.

## Xử lý
Giữ ZIP peer làm bằng chứng lượt đầu. Ghi rõ các phát hiện vào owner response và guideline v3. Nếu peer rework thì dùng tên export khác; không ghi đè lượt đầu hoặc chấm lại làm tăng điểm chuyển giao ban đầu.
Hình đối chiếu tại build/peer_review (ảnh gốc phủ box magenta và crop phóng nearest-neighbor). Không gửi gold/crop nội bộ cho peer trước khi hoàn tất lượt blind.
Đã tổng hợp 5 nhận xét từ export dưới tên nhóm owner trong peer_feedback.md. Người dùng cung cấp khoảng 5–20 câu hỏi; chưa có nội dung từng câu. Tên tài khoản Dai lấy từ XML, không tự suy thành họ tên người gán.