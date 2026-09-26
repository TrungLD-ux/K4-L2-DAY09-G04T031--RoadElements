# G04T031 — Road Elements: Traffic Light Guideline

## Kết quả
Hồ sơ guideline-challenge đã qua kiểm tra cấu trúc G1–G6. Guideline cuối v3; 10 edge-case cards; 12 gold decisions gồm 3 critical và 2 geometry. Calibration có hai export độc lập của Thái và Trung. Blind test dùng export team03, job 17.

Calibration: count agreement 83.3%, attribute/tag 75.0%.
Blind: D=80.0, C=66.7, G=0.0, I=0.0; GTS=61.3/100. Một critical escape được phân tích và xử lý trong guideline v3. Điểm thấp được giữ đúng theo export, không sửa bằng chứng để nâng điểm.

## Đọc bài
1. 00_team.md và 01_problem_statement.md: phạm vi và phân công.
2. 02_guideline.md và 03_*: guideline v3, ontology, schema và setup.
3. sample_pack.csv và 04_edge_cases/: bộ ảnh và quyết định gold.
4. 05_qa_plan.md và 06_*: QA, export calibration, phép đo và chẩn đoán.
5. 07_blind_handoff/: export peer, bảng chấm, nhận xét owner, số câu hỏi và GTS.
6. 08_revision_log.md, 09_cvat_export_or_task_reference.txt và FREEZE.txt: phiên bản và nguồn bằng chứng.

## Phạm vi bằng chứng
Nhận xét blind do nhóm owner tổng hợp từ output thực tế. Khoảng câu hỏi 5–20 là ước lượng người dùng cung cấp; tất cả các giá trị trong khoảng đều cho I=0. Nội dung từng câu hỏi không có bản ghi. Hai thông tin này được ghi rõ trong hồ sơ, không tạo hội thoại hoặc trích lời peer.

Gold và sample pack giữ nguyên ở tag gold-freeze; guideline v2 được lưu trong tag, v3 dùng cho cải tiến sau review. Các ZIP export giữ nguyên byte. Các file evidence_before_review là lịch sử trước rà soát, không phải đáp án hiện hành.

Bản nộp không tuyên bố đã hoàn tất chiều nhóm mình làm đề team03: exam.zip chỉ có ảnh, chưa có guideline/schema của họ. Không có export rework nên chưa đo hiệu quả annotation sau v3.

## Kiểm tra
Từ repo đã clone, mở guideline-challenge và chạy:

    python -m unittest discover -s tests
    python lab9.py check
    python lab9.py verify

Mã scoring bổ sung đọc clarification_count.json: khoảng phải có nguồn và nằm hoàn toàn trong một mức Independence. Công thức, trọng số và gate giữ nguyên. Đã chạy 5 test và tất cả đạt.