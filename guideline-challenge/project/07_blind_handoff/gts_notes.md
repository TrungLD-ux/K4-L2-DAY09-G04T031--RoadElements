# Cơ sở tính GTS

Số câu hỏi được người dùng ước lượng trong khoảng 5–20. Theo rubric, từ 5 câu trở lên có Independence bằng 0; vì vậy khoảng này cho cùng một kết quả điểm, không cần chọn một con số chính xác.

- D: 8/10 = 80.0.
- C: 2/3 = 66.7.
- G: 0/2 = 0.0.
- I: 0.0 theo khoảng câu hỏi 5–20.
- GTS = 0.60×80 + 0.20×(200/3) + 0.10×0 + 0.10×0 = 61.3/100 sau làm tròn.

clarification_count.json lưu khoảng và nguồn thông tin. clarification_log.csv giữ cấu trúc sẵn có; chưa có nội dung chi tiết từng câu hỏi nên không tạo bản ghi thay thế. Nhận xét trong peer_feedback.md do owner tổng hợp từ output thực tế, không trích lời peer.

Công cụ scoring được bổ sung hỗ trợ khoảng có nguồn: chỉ chấp nhận khi mọi số trong khoảng thuộc cùng một mức Independence. Không đổi thang điểm, trọng số hoặc gold; trường hợp không có file khoảng vẫn tính từ log như công cụ gốc. Các test kiểm giữ nguyên các mức điểm, từ chối khoảng vượt nhiều mức và dữ liệu không hợp lệ.