# Tình trạng hồ sơ nộp

Đã hoàn thiện bộ tài liệu guideline-challenge: team/problem, guideline v3, ontology/schema, sample pack, QA plan, hai export calibration và báo cáo, 10 edge cases, 12 gold decisions, freeze, export peer, bảng chấm, nhận xét owner và GTS.

Kết quả: count agreement calibration 83.3%, attribute/tag 75.0%; blind D=80.0, C=66.7, G=0.0, I=0.0; GTS=61.3/100. I dùng khoảng ước lượng 5–20 câu hỏi do người dùng cung cấp, được lưu kèm nguồn; không có bản ghi chi tiết hội thoại. Nhận xét blind do owner tổng hợp từ export.

Gold/sample pack và các ZIP gốc giữ nguyên. Guideline v3 là bản sửa sau đánh giá; chưa có export rework để tuyên bố kết quả annotation đã tốt hơn. Gói blind v2 vẫn được giữ làm bằng chứng lượt đầu.

Bài nộp tập trung guideline-challenge. exam.zip của team03 là bộ ảnh khác; chưa có guideline/schema để báo cáo hoàn tất chiều nhóm mình làm bài team03. mini-task là bài riêng.

Các lệnh kiểm tra từ guideline-challenge:

    py -3.11 -m unittest discover -s tests
    py -3.11 lab9.py check
    py -3.11 lab9.py verify

File clarification_count.json là phần mở rộng có nguồn để tính Independence theo khoảng, không thay thang điểm hoặc trọng số. Gói nộp kèm mã nguồn và Git bundle để kiểm chứng mốc freeze. Chưa push GitHub.