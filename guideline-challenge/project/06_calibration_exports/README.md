# Bằng chứng calibration — Thái và Trung

Người dùng xác nhận thai.zip của Nguyễn An Thái, job 18 của Lê Danh Trung. Hai ZIP gốc được giữ nguyên nội dung; trung.zip là tên ngắn của job_18_annotations_2026_09_26_04_56_05_cvat for images 1.1.zip.

- Thái: job 25; 18 box; SHA256 d4d7283475b89a679b804236a1e634d29825a17c7dea20a7c2232c3ec8235a0d.
- Trung: job 18; 19 box; SHA256 35a8569c9c9c987422023a2678fb15bdad001a5a4f9482d825ebeda4c6f3c0d3.
- Cùng 6 ảnh: BDD15, BDD17, BDD20, BDD21, BDD25, LISA03. Schema traffic_light/state/needs_review khớp.

## Lệnh đã chạy từ guideline-challenge

    py -3.11 lab9.py calib project/06_calibration_exports/thai.zip project/06_calibration_exports/trung.zip

Kết quả gốc: count 5/6 = 83.3%; attribute/tag 9/12 = 75.0%, ghi trong 06_calibration_measure.csv. BDD21 khác state; BDD25 khác count dẫn tới khác multiset state và needs_review. Không diễn giải 75% là accuracy theo object.

Tool không so geometry. Audit từng box: Thái có 7/18 box dưới ngưỡng, 4 unknown không review; Trung có 8/19 box dưới ngưỡng, 3 unknown không review. Xem thai_box_audit.csv và trung_box_audit.csv. LISA03 cùng count 5 và multiset red nhưng vị trí/tách-gộp khác; phải kiểm ảnh trước kết luận.

06_calibration_report.csv chứa bất đồng thực, lỗi cùng mắc và hướng xử lý. Guideline v2 sửa từ các phát hiện này. Chưa gán lại trên CVAT hoặc export lại sau sửa; không có số liệu đồng thuận sau rework. Không sửa ZIP gốc để làm tăng điểm.

Báo cáo trước khi có đủ export và gold/cards cũ được giữ trong evidence_before_review. ZIP lớn tên repo không phải export thứ ba. Hai export calibration không được dùng thay peer blind output.