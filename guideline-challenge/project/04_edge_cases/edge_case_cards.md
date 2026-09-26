# Edge-case library — nội bộ

Rà soát từ ảnh local và thai.zip ngày 2026-09-26. Card blind không đưa vào Guide cho peer. Gold theo từng quyết định/vùng, không mặc định mô tả toàn bộ số đèn trong ảnh. Calibration đã so hai export; xem FREEZE.txt và tag gold-freeze để xác minh mốc gold.

CASE ID: EC-01
Sample: LISA08 (blind)
Scene: Ngã tư có tín hiệu tròn và mũi tên.
Observation: Cụm trên trái có mũi tên rẽ; cụm trên giữa hiển thị đỏ tròn.
Decision: IGNORE mũi tên; LABEL cụm tròn đi thẳng.
Expected: Không vẽ cụm khoảng (747,164); cụm khoảng (940,170) có state=red.
Rationale: Guideline 1, 4; sai hướng điều khiển là critical.
Common mistake: Vẽ mọi cụm nhìn thấy vì đều là đèn giao thông.
Diversity: critical;conflict

CASE ID: EC-02
Sample: BDD15 (calibration)
Scene: Tín hiệu nhỏ ở xa.
Observation: Hai box Thái rộng 5.08 và 7.58 px.
Decision: IGNORE các box này theo ngưỡng.
Expected: Không giữ hai box dưới 10 px chiều rộng; không nới box.
Rationale: Guideline 5 đo cả hai chiều trên ảnh gốc.
Common mistake: Chỉ kiểm chiều cao hoặc nhầm kích thước khi zoom.
Diversity: small_far

CASE ID: EC-03
Sample: BDD17 (calibration)
Scene: Kính ướt, giá đỡ trong xe che một phần cảnh.
Observation: Export có 4 box; 3 box rộng dưới 10 px; box còn lại 10.71×21.99 px cần kiểm biên và scope.
Decision: IGNORE box dưới ngưỡng; review box còn lại nếu biên không chắc.
Expected: Không coi cả ảnh là zero chỉ vì mưa; không coi mọi nguồn sáng là đèn hợp lệ.
Rationale: Guideline 3, 5, 6 tách visibility khỏi inclusion.
Common mistake: Khoanh cả vệt nhòe hoặc loại cả ảnh mà không kiểm từng cụm.
Diversity: low_visibility;occlusion

CASE ID: EC-04
Sample: BDD20 (calibration)
Scene: Đèn xa trong cảnh có vật che trên kính.
Observation: Box Thái 6.09×8.77 px, state unknown.
Decision: IGNORE box dưới ngưỡng.
Expected: Không giữ box dưới ngưỡng chỉ để bật review.
Rationale: Guideline 5 ưu tiên inclusion trước state/review.
Common mistake: Dùng unknown để hợp thức hóa mọi đối tượng quá nhỏ.
Diversity: small_far;ambiguity

CASE ID: EC-05
Sample: BDD21 (calibration)
Scene: Hai cụm đèn ở những vị trí và kích thước khác nhau.
Observation: Thái gán green và unknown; cả hai needs_review=false.
Decision: ESCALATE cụm unknown.
Expected: unknown phải needs_review=true; QA kiểm trực tiếp cụm đó trước khi chốt màu.
Rationale: Guideline 4, 7; màu cụm khác không phải bằng chứng.
Common mistake: Sao chép green từ cụm dễ nhìn sang cụm khó nhìn.
Diversity: ambiguity;escalation

CASE ID: EC-06
Sample: BDD25 (calibration)
Scene: Đường ướt ban đêm có nhiều nguồn sáng.
Observation: Có phản chiếu dưới mặt đường; một box Thái rộng 9.87 px.
Decision: IGNORE phản chiếu và box dưới ngưỡng; đánh giá các cụm thật riêng.
Expected: Không thêm instance cho vùng sáng dưới đường; không làm tròn 9.87 lên 10.
Rationale: Guideline 2, 5, 6.
Common mistake: Đếm mọi đốm xanh hoặc nới box để qua ngưỡng.
Diversity: low_visibility;conflict

CASE ID: EC-07
Sample: BDD18 (blind)
Scene: Đêm, nhiều đèn xe và tín hiệu phía xa.
Observation: Bên phải có tín hiệu bàn tay sáng.
Decision: IGNORE tín hiệu đi bộ và đèn xe.
Expected: Không gán traffic_light cho vùng bàn tay; các ứng viên còn lại kiểm scope/kích thước riêng.
Rationale: Guideline 1; không dùng màu đỏ làm tiêu chí duy nhất.
Common mistake: Đổi tín hiệu đi bộ thành đèn đỏ của xe.
Diversity: critical;low_visibility

CASE ID: EC-08
Sample: BDD26 (blind)
Scene: Cụm gần trên trái có lõi xanh và halo mạnh.
Observation: Nhận ra màu xanh trực tiếp; khó xác định biên vỏ.
Decision: LABEL + ESCALATE.
Expected: state=green, needs_review=true; box theo vỏ thấy được hoặc lõi sáng, không halo.
Rationale: Guideline 3, 4; độ chắc chắn màu khác độ chắc chắn hình học.
Common mistake: Ép unknown chỉ vì không thấy vỏ, hoặc khoanh toàn quầng.
Diversity: ambiguity;escalation

CASE ID: EC-09
Sample: BDD02 (example)
Scene: Đèn gần mép trên phải của ảnh.
Observation: Vật thể sát biên ảnh không đủ phần ngoài ảnh để suy hình đầy đủ.
Decision: LABEL phần nhìn thấy nếu đủ ngưỡng và đúng scope; review khi không rõ.
Expected: Box không vượt ảnh, không dựng lại phần vỏ ngoài ảnh.
Rationale: Guideline 3, 5 về truncation.
Common mistake: Vẽ amodal theo kích thước cụm đèn khác.
Diversity: truncation

CASE ID: EC-10
Sample: BDD11 (example)
Scene: Khu dân cư ban ngày.
Observation: Tín hiệu bàn tay phía phải dễ bị nhầm với đèn đỏ.
Decision: IGNORE tín hiệu đi bộ.
Expected: Không tạo traffic_light cho tín hiệu hình bàn tay.
Rationale: Guideline 1 phân biệt đối tượng theo công năng trước màu.
Common mistake: Thấy tín hiệu đỏ thì gán traffic_light.
Diversity: conflict