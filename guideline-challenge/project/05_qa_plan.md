# QA plan + quality gates

## Flow và trách nhiệm
Lê Danh Trung tổng hợp issue; Nguyễn Lê Thế Anh review gold và ca khó; Nguyễn An Thái kiểm schema/export. Người gán không tự đóng lỗi của mình. Quy trình: gán độc lập → so calibration → sửa guideline → rework trên bản sao task → self-check → người khác review → xuất bản mới. Giữ nguyên export calibration ban đầu làm bằng chứng.

Với bộ nhỏ hiện tại: kiểm 100% của 6 ảnh calibration, 5 ảnh blind và tất cả box; bắt buộc rà negative để tìm false positive/false negative. Nếu mở rộng: review 100% unknown/review, đèn rẽ/đi bộ, box có cạnh trong [8,12] px và ca đêm; thêm mẫu ngẫu nhiên 20% ảnh còn lại của từng annotator, seed 31, lưu danh sách sample được chọn. Có critical trong phần ngẫu nhiên thì mở rộng kiểm 100% lô đó.

## Issue và đóng lỗi
Ghi sample, tọa độ, annotator, lỗi, severity, người xử lý và bằng chứng sửa vào báo cáo hoặc CVAT issue. Người review kiểm lại ảnh và export sửa, ghi kết quả rồi mới đóng. Geometry/scope chưa rõ chuyển Lab Coach. Bất đồng lượt đầu nằm trong 06_calibration_report.csv; đây là chẩn đoán và hướng xử lý, không phải bằng chứng đã sửa annotation.

## Severity
- Critical: đỏ thành xanh; lấy đèn rẽ/đi bộ làm tín hiệu cho hướng đi thẳng. Dừng bàn giao lô, kiểm 100% và sửa trước tiếp tục.
- Major: thiếu/thừa cụm hợp lệ, gộp/tách sai cụm, dưới ngưỡng, undefined, unknown không review, biên rõ lệch quá 2 px. Rework và kiểm lại mọi object liên quan.
- Minor: lỗi mô tả/định dạng không đổi nhãn, hình học hoặc quyết định. Sửa trước bản nộp cuối.
- Question: scope hoặc biên ảnh không đủ bằng chứng. Ghi câu hỏi và review; không ép thành đáp án chắc chắn.

## Metrics và thresholds nội bộ
Count agreement = số ảnh count giống nhau / tổng ảnh. Attribute agreement = số dòng multiset attribute giống nhau / tổng dòng attribute. Chỉ dùng để tìm bất đồng, không thay precision/recall hay accuracy theo từng object.
Defect rate = object lỗi / object đã review; missing object tính riêng theo ảnh. Critical escape = số lỗi critical còn sót khi reviewer kiểm bản sau self-QC / số object reviewer kiểm; khi mẫu bằng 0 thì ghi N/A.

PASS khi đủ sample/schema, không undefined, không critical/major chưa đóng, không issue scope/geometry chưa xử lý, và 100% ca rủi ro được review. REWORK nếu có lỗi sửa được. ESCALATE nếu không có đủ bằng chứng thị giác để chốt. Mục tiêu count/attribute agreement sau rework là 100% trên bộ nhỏ, nhưng chỉ công bố nếu đã chạy lại trên export mới; không sửa số liệu lượt đầu.

Đây là ngưỡng nội bộ cho bài học, không phải chuẩn ngành. Kiểm toàn bộ bộ nhỏ tốn ít công hơn chi phí để lọt lỗi critical; khi mở rộng mới dùng lấy mẫu kèm mở rộng review khi fail.

## Quản lý phiên bản
v2 chứa sửa đổi sau calibration. Trước peer test: freeze gold, sample pack, guideline và schema. Sau peer test: ghi feedback/câu hỏi thực, sửa guideline thành v3, giữ gold đã freeze để chấm trung thực; ghi gold sai nếu phát hiện lỗi. Chưa có peer thì không tạo feedback hoặc tuyên bố v3.