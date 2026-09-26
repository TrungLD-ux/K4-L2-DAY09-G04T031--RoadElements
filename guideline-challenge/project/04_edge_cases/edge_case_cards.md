# Edge-case library

Tối thiểu **8 card**, khuyến nghị 10–12. Một edge case tốt là case mà hai annotator hợp lý có thể làm khác nhau nếu
guideline chưa rõ. Tám ảnh dễ có label rõ ràng không được tính là edge-case library.

Cần có đủ độ đa dạng: occlusion / truncation / small-far · ambiguous semantics · conflicting road elements · **một case
critical-risk** · **một case guideline cho phép escalation**.

File này là kho nội bộ của nhóm, **không gửi cho peer**. Card dùng ảnh example/calibration thì chép rule + ví dụ sang
`02_guideline.md` (mục 7 và 9) để peer đọc được. Card về ảnh blind chỉ nằm ở đây, và decision của nó phải có trong
`gold_decisions.csv` trước `make freeze`.

`make status` đếm số dòng `CASE ID:` đã điền (đã thay placeholder). Copy khối dưới cho mỗi case.

---

CASE ID: EC-01
Sample: LISA08
Scene: Ngã tư có đèn đi thẳng và đèn rẽ trái chuyên dụng.
Observation: Có 3 cụm đèn ở ngã tư, cụm đèn giữa và phải đang Đỏ, cụm ngoài cùng bên trái (đèn rẽ trái) đang Đỏ.
Decision: LABEL (đèn đi thẳng) và IGNORE (đèn rẽ trái)
Expected: Vẽ bounding box 2 cụm đèn đi thẳng, `state` = `red`, `needs_review` = `false`. Tuyệt đối KHÔNG vẽ cụm đèn rẽ trái.
Rationale: Lỗi hậu quả lớn (Critical-risk). Việc vẽ nhầm đèn rẽ thành đèn đi thẳng sẽ khiến xe tự lái học sai tín hiệu. Ở các frame sau (LISA26-30) đèn rẽ sẽ chuyển Xanh, nếu thói quen khoanh nhầm được duy trì sẽ gây tai nạn.
Common mistake: Annotator khoanh tất cả các cụm đèn giao thông nhìn thấy trong ảnh.
Diversity: critical

---

CASE ID: EC-02
Sample: BDD20
Scene: Ảnh chụp qua kính chắn gió có hiện tượng phản chiếu hình ảnh nội thất xe.
Observation: Ngã tư phía trước có cụm đèn nhỏ, nhưng trên mặt kính lái có bóng phản chiếu mờ mờ đè lên tầm nhìn gây nhiễu.
Decision: ESCALATE
Expected: Vẽ bounding box ôm cụm đèn thực tế trên đường, chọn `state` hiện tại, và đánh dấu `needs_review` = `true`.
Rationale: Sự phản chiếu gây mập mờ (ambiguity) về tính hợp lệ của tín hiệu. Việc đánh dấu cờ giúp QA kiểm tra lại độ nhiễu của ảnh đối với model.
Common mistake: Annotator không chú ý đến bóng phản chiếu hoặc tự ý bỏ qua cụm đèn do cho rằng ảnh bị lỗi hỏng.
Diversity: escalation

---

CASE ID: EC-03
Sample: BDD17
Scene: Đường phố trời mưa, kính xe đọng nước.
Observation: Nước đọng trên kính làm cụm vỏ đèn bị nhòe và biến dạng một phần, nhưng vẫn phân biệt được màu Đỏ.
Decision: LABEL
Expected: Vẽ bounding box bám sát phần quầng sáng và vỏ đèn còn nhận diện được. `state` = `red`.
Rationale: Trong điều kiện thời tiết xấu, xe tự lái vẫn phải nhận diện được tín hiệu. Không được tự ý mở rộng bounding box theo chiều dài của vệt nhòe của nước.
Common mistake: Annotator khoanh khung quá rộng, bao gồm cả vệt nước nhòe chảy dài trên kính.
Diversity: occlusion

---

CASE ID: EC-04
Sample: BDD22
Scene: Đường cao tốc lúc hoàng hôn, ngã tư nằm ở rất xa.
Observation: Các cụm đèn giao thông nằm tít ở đường chân trời, kích thước hiển thị trên ảnh rất bé (dưới 10 pixel).
Decision: IGNORE
Expected: Không vẽ gì cả.
Rationale: Đặc trưng hình ảnh (features) dưới 10 pixel không đủ để mô hình deep learning trích xuất thông tin đáng tin cậy. Nếu cố vẽ sẽ sinh dữ liệu rác gây nhiễu cho model.
Common mistake: Annotator cố gắng zoom hết cỡ và chấm một bounding box siêu nhỏ xíu vì "sợ sót nhãn".
Diversity: small_far

---

CASE ID: EC-05
Sample: BDD26
Scene: Đường tối, ánh sáng đèn giao thông xanh bị lóa (chói) mạnh.
Observation: Cụm đèn bên trái cực to, lóa sáng xanh rực rỡ thành một quầng lớn, hoàn toàn không nhìn thấy viền vỏ nhựa của đèn.
Decision: UNKNOWN
Expected: Vẽ bounding box bao quanh quầng sáng chính, chọn `state` = `unknown`, `needs_review` = `false`.
Rationale: Khi lóa mạnh làm mất chi tiết hình học của đèn, tuân thủ luật "chói không thấy vỏ thì unknown". Model cần học cách đẩy quyền quyết định cho cảm biến khác khi camera bị "mù".
Common mistake: Tự tin chọn `green` thay vì tuân thủ luật `unknown` của guideline.
Diversity: ambiguity

---

CASE ID: EC-06
Sample: LISA01
Scene: Ngã tư rộng, đường có nhiều làn nhưng không rõ vạch kẻ trên mặt đường.
Observation: Xe đang đứng ở vị trí có thể đi thẳng hoặc rẽ trái, ngã tư có cả cụm đèn rẽ trái và đi thẳng, không đủ ngữ cảnh để chốt làn hiện tại.
Decision: ESCALATE
Expected: Vẽ bounding box cho cả đèn rẽ trái và đèn đi thẳng. Gán `state` cho từng cụm và bắt buộc tick chọn `needs_review` = `true` ở cả hai.
Rationale: Conflicting semantics. Khi không rõ xe sẽ đi theo làn nào do vạch kẻ không rõ ràng, phải đánh dấu để QA can thiệp.
Common mistake: Annotator tự suy diễn xe đi thẳng và lờ đi cụm đèn rẽ, hoặc ngược lại.
Diversity: conflict

---

CASE ID: EC-07
Sample: BDD18
Scene: Ảnh ban đêm cực tối, đường không có đèn cao áp chiếu sáng.
Observation: Chỉ nhìn thấy một quầng sáng đỏ lơ lửng ở vị trí ngã tư, hoàn toàn KHÔNG nhìn thấy cụm vỏ nhựa màu đen bao bọc bóng đèn.
Decision: LABEL
Expected: Vẽ bounding box ôm vừa khít quầng sáng đỏ đang phát ra (blooming effect). `state` = `red`.
Rationale: Ban đêm, hình thái (morphology) của đèn chính là quầng sáng. Nếu bỏ qua sẽ khiến AI mù đèn đỏ vào ban đêm.
Common mistake: Annotator không vẽ do áp dụng luật "phải khoanh vỏ nhựa ôm trọn 3 bóng" một cách quá máy móc.
Diversity: low_visibility

---

CASE ID: EC-08
Sample: BDD25
Scene: Trời mưa ban đêm, mặt đường nhựa ướt sũng phản chiếu ánh đèn giao thông.
Observation: Trên mặt đường ướt có bóng phản chiếu cực lớn màu xanh, trong khi cụm đèn thật nằm trên cao và bé hơn.
Decision: IGNORE (đối với bóng phản chiếu dưới đường)
Expected: Chỉ vẽ bounding box cho cụm đèn thật trên cao. Tuyệt đối không khoanh vào vùng bóng lấp loáng dưới mặt đường.
Rationale: Model dễ bị nhầm lẫn (False Positive) bởi các vật thể phát sáng trên mặt đường ướt, cần dạy model phân biệt đèn thật và hình phản chiếu.
Common mistake: Annotator khoanh nhầm hoặc khoanh bounding box bao trọn cả vệt sáng xanh dưới mặt đường.
Diversity: ambiguity

---

CASE ID: EC-09
Sample: LISA26
Scene: Ảnh tĩnh thuộc chuỗi video nhưng được giao nhãn độc lập (trạng thái đèn rẽ trái chuyển từ Đỏ sang Xanh).
Observation: Đèn mũi tên rẽ trái đang chuyển màu Xanh, đèn đi thẳng vẫn Đỏ. Annotator biết xe sắp rẽ trái vì đã nhìn thấy các frame LISA kế tiếp.
Decision: IGNORE (đèn rẽ trái)
Expected: Dù "biết" xe chuẩn bị rẽ thông qua trí nhớ về ngữ cảnh chuỗi ảnh, đây là task ảnh tĩnh (xử lý độc lập từng ảnh), xe hiện tại vẫn đang đối diện làn đi thẳng. Bắt buộc bỏ qua đèn rẽ.
Rationale: Lỗi vi phạm tính chất task (Temporal illusion). Annotator tự mang kiến thức tương lai vào để ra quyết định cho frame ảnh tĩnh hiện tại.
Common mistake: Vẽ và gán nhãn cụm đèn rẽ trái vì "biết trước" xe chuẩn bị đi theo hướng đó.
Diversity: critical

---
