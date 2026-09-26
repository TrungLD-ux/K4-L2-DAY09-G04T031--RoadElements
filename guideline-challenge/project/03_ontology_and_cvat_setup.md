# Ontology + CVAT setup

## Schema chuẩn
Class traffic_light: rectangle, một cụm vỏ vật lý.
Attribute state: select, values __undefined__, red, green, yellow, off, unknown; default __undefined__; mutable=false vì dùng ảnh tĩnh và Shape.
Attribute needs_review: checkbox, default false, values ["false"] theo cấu hình checkbox CVAT; giá trị annotation thực tế true hoặc false; mutable=false.
JSON triển khai: 03_cvat_labels.json. Hai attribute thuộc traffic_light, không phải class màu riêng. Default undefined giúp phát hiện quên chọn; mọi unknown phải review. Không dùng tag ảnh trong schema hiện tại; issue cả ảnh được ghi riêng và giải quyết trước bàn giao.

## Bằng chứng setup
thai.zip là CVAT XML 1.1, job 25, mode annotation, 6 ảnh, 18 rectangle; schema trong meta khớp JSON. File export lúc 2026-09-26 04:57:45 UTC. XML không xác nhận phiên bản server hoặc nội dung Guide. Repo trước đó ghi server 2.75.1 và đã dán Guide; đây là thông tin nhóm tự khai, chưa xác minh trực tiếp trên server.

## Tạo/chạy task
1. Gom đúng BDD15, BDD17, BDD20, BDD21, BDD25, LISA03 (split calibration).
2. Mỗi người tạo task riêng G04T031-calib-<ten>, dán toàn bộ JSON vào Raw labels; kiểm rectangle và hai attribute.
3. Upload cùng ảnh gốc, không resize/đổi tên. Dán 02_guideline.md vào Guide và ghi phiên bản đang dùng.
4. Dùng Shape. Thử chọn đủ state; bật/tắt review, Save rồi mở lại kiểm tra. Đây là checklist cho task mới, không phải thao tác đã thực hiện trong lần rà soát repo.
5. Annotate độc lập, Save; export CVAT for images 1.1, tắt Save images; lưu <ten>.zip vào 06_calibration_exports.
6. Chạy python lab9.py calib project/06_calibration_exports/thai.zip project/06_calibration_exports/trung.zip từ guideline-challenge; phân tích kết quả rồi cập nhật report và revision log.

## Kiểm tra export
Giữ nguyên bản gốc. Kiểm đủ 6 ảnh, class/attribute/geometry hợp lệ; không undefined, không box dưới 10 px mỗi chiều, unknown phải review. Cả hai bản export gốc còn lỗi nội dung so với guideline; xem 06_calibration_report.csv. Nếu thay ontology, tạo task mới; không sửa export gốc để làm bằng chứng đồng thuận.
## Calibration đã thực hiện
Người dùng xác nhận job 25 là Thái, job 18 là Trung. Job 18 export lúc 2026-09-26 04:58:19 UTC, cùng 6 ảnh và schema, có 19 box. Đã chạy lab9.py calib trên hai ZIP gốc: count 5/6 (83.3%), attribute/tag 9/12 (75.0%). Tool không kiểm sự tương ứng geometry. Phiên bản Guide tại thời điểm gán không được lưu trong XML; v2 hiện tại là bản sau rà soát calibration.

## Bảng ontology đối chiếu JSON

| Name | Geometry | Type | Allowed values | Default | Mutable | Rationale |
|---|---|---|---|---|---|---|
| traffic_light | rectangle | class | một cụm đèn vật lý | không áp dụng | không áp dụng | Giữ định danh đối tượng độc lập với trạng thái |
| state | thuộc rectangle | select attribute | __undefined__, red, green, yellow, off, unknown | __undefined__ | false | Buộc chọn màu; undefined không được bàn giao |
| needs_review | thuộc rectangle | checkbox attribute | false hoặc true trong annotation; values cấu hình ["false"] | false | false | Đánh dấu bất định về scope, màu hoặc geometry |