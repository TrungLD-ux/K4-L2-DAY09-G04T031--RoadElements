# Annotation guideline — Traffic lights cho hướng đi thẳng

**Version:** v2

Bản v2 sau calibration ngày 2026-09-26: đã so export độc lập của Thái và Trung trên cùng 6 ảnh. Các quy tắc dưới đây xử lý bất đồng và lỗi cùng mắc trong lượt gán ban đầu; không có tuyên bố đã gán lại hoặc đo đồng thuận sau sửa.

## 1. Objective + scope
Gán cụm đèn dành cho xe cơ giới điều khiển hướng đi thẳng của xe mang camera. Chỉ dùng ảnh hiện tại. Loại đèn đi bộ, đèn mũi tên rẽ chuyên dụng, đèn quay lưng, đèn rõ ràng phục vụ đường cắt ngang, đèn xe/đường/quảng cáo và phản chiếu.
Đèn rẽ rõ ràng vẫn bị loại dù không thấy vạch làn. Nếu chưa rõ cụm nào điều khiển hướng đi thẳng, giữ các ứng viên không bị loại trừ rõ ràng, đủ kích thước và bật review. Không đoán ý định xe rẽ.

## 2. Annotation unit
Một cụm vỏ vật lý = một instance, kể cả cụm nằm ngang. Hai cụm cùng điều khiển một hướng phải có hai rectangle riêng. Dùng Shape trên ảnh tĩnh; không Track, không gộp nhiều cụm.

## 3. Geometry rule
Ôm sát vỏ nhìn thấy và chụp che nắng; loại cột, dây, giá đỡ, nền, quầng loang và vệt nước. Không chỉ khoanh bóng sáng nếu nhìn thấy vỏ. Biên rõ: mục tiêu lệch ≤2 px mỗi cạnh.
Bị che/cắt biên: box giới hạn phần nhìn thấy của cùng cụm, không đoán phần bị che/ngoài ảnh. Bật thuộc tính CVAT occluded nếu có vật che; không tách một vỏ thành nhiều instance. Hình học không chắc phải review.
Ban đêm không rõ vỏ nhưng xác nhận được cụm thật: khoanh lõi phát sáng, không halo; bật review vì dùng hình học thay thế. Không xác định được cả nguồn sáng thật thì ghi issue theo mục 7, không tạo box tùy tiện.

## 4. Taxonomy
Class: traffic_light, rectangle.
- red/green/yellow: màu nhìn trực tiếp trong chính cụm. Không thấy vỏ hoặc bị lóa không tự động đồng nghĩa unknown.
- off: thấy rõ cụm và đủ chi tiết xác nhận không bóng nào sáng.
- unknown: chưa đủ bằng chứng phân biệt màu hoặc off; không đoán theo vị trí bóng/xe/đèn khác.
- __undefined__: mặc định nhắc chọn, không hợp lệ khi bàn giao.
- needs_review=false: scope, geometry và màu đều rõ. true: bất kỳ thành phần nào chưa chắc, mọi unknown hoặc khi dùng lõi sáng thay vỏ.

## 5. Inclusion / exclusion
Đo tọa độ ảnh gốc: width=xbr-xtl, height=ybr-ytl. Chỉ gán khi CẢ HAI ≥10 px. Một chiều <10 thì IGNORE; zoom không đổi kích thước thật. Không làm tròn 9.87 thành 10, không nới box để vượt ngưỡng. Ngưỡng áp dụng phần nhìn thấy hoặc lõi sáng trong ngoại lệ mục 3. Cụm dưới ngưỡng không tạo box chỉ để review.

## 6. Visibility / occlusion
Phản chiếu trên đường/kính/nắp xe không phải instance thứ hai. Mưa/đêm không mặc định unknown; đánh giá màu trực tiếp. Che khuất không đồng nghĩa off. Đủ kích thước nhưng màu không rõ: unknown và review. Mất toàn bộ đối tượng: không vẽ amodal.

## 7. Ambiguity / escalation
Trình tự: xác định nguồn tín hiệu thật → scope → kích thước → geometry → state → review.
Chưa rõ hướng điều khiển: giữ ứng viên đủ ngưỡng và chưa bị loại trừ rõ, chọn state trực tiếp, bật review. Không thể tạo geometry có căn cứ: ghi CVAT issue gồm sample_id, vị trí và câu hỏi. QA owner Lê Danh Trung cùng Gold owner chốt; không giải quyết được thì hỏi Lab Coach. Không export final khi còn issue này. Issue không nằm trong XML nên lưu nội dung xử lý trong báo cáo.

## 8. Temporal rule
Mỗi ảnh độc lập. Không dùng frame trước/sau để suy màu hoặc ý định xe. LISA cùng chuỗi có nguy cơ ghi nhớ bối cảnh.

## 9. Examples từ example/calibration
- BDD11 (example): tín hiệu bàn tay bên phải dành cho người đi bộ, không gán traffic_light.
- BDD15 (calibration): hai box Thái rộng 5.08 và 7.58 px, không đạt inclusion; không nới box.
- BDD20 (calibration): box Thái 6.09×8.77 px, IGNORE dù đã chọn unknown.
- BDD21 (calibration): export có green và unknown; không đổi unknown thành green chỉ vì box khác xanh. Unknown phải review và kiểm ảnh gốc.
- BDD25 (calibration): tách cụm thật trên cao khỏi phản chiếu dưới đường. Box 9.87×12.12 px chưa đạt ngưỡng rộng.
- LISA03 (calibration): cụm trên trái có mũi tên rẽ, loại cụm đó. Các cụm tròn xử lý riêng, không gộp cả ngã tư.

## 10. Common mistakes và self-check
Không còn undefined; mọi unknown có review; mọi box đủ hai chiều; không gộp cụm; không gán đèn rẽ/đi bộ/phản chiếu; không suy màu; kiểm lại biên bất định. Đỏ thành xanh và nhầm hướng điều khiển là critical.
Chênh count cần kiểm từng vị trí, không mặc định người vẽ nhiều hơn đúng. Tool calibration so count và multiset thuộc tính, không chứng minh geometry hay khớp đúng từng object.