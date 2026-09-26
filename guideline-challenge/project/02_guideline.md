# Annotation guideline — Nhận diện và phân trạng thái đèn giao thông trực tiếp điều khiển Ego-vehicle

**Version:** v1

<!--
v0 = chưa có bản nháp. Đổi dòng Version ở trên thành v1 khi xong bản nháp đầu, v2 sau calibration, v3 sau blind
handoff; mỗi lần tăng version ghi một dòng vào 08_revision_log.md. `make freeze` đòi v2 trở lên.

File này là thứ nhóm peer nhận nguyên văn trong blind pack và là Guide dán vào CVAT. Peer KHÔNG nhận
edge_case_cards.md, gold_decisions.csv hay sample_pack.csv. Rule nào peer cần biết phải nằm ở đây.
No hidden rules: rule chỉ giải thích bằng miệng thì coi như không tồn tại.
Ví dụ trong guideline chỉ dùng ảnh split example hoặc calibration, không dùng ảnh blind.
-->

## 1. Objective + scope

* **Mục tiêu (Objective):** Khoanh vùng và xác định trạng thái màu của các cụm đèn giao thông **đang trực tiếp điều khiển hướng đi thẳng của chiếc xe đang mang camera (ego-vehicle)**. Kết quả này phục vụ tác vụ ra quyết định đi/dừng cho xe tự lái.
* **Trong phạm vi (In scope):** Các cụm vỏ đèn giao thông hướng về phía camera, áp dụng cho làn đường mà xe ego-vehicle đang chạy hoặc dự định đi thẳng tới.
* **Ngoài phạm vi (Out of scope - KHÔNG vẽ):** 
  * Đèn tín hiệu dành riêng cho người đi bộ.
  * Đèn quay lưng lại với camera (đèn của làn ngược chiều).
  * Đèn của các ngã rẽ cắt ngang.
  * Đèn mũi tên điều khiển rẽ trái/phải chuyên dụng (trong khi xe ego-vehicle đang ở làn đi thẳng).

## 2. Annotation unit

* **Đơn vị:** Ảnh tĩnh (Image).
* **Instance:** Mỗi cụm vỏ đèn giao thông vật lý (thường chứa 3 bóng Xanh/Đỏ/Vàng) được tính là **1 instance**. Nếu tại ngã tư có 2 cụm đèn cùng điều khiển làn đi thẳng của xe mình (ví dụ: 1 cái trên cột bên phải, 1 cái treo ngang trên vươn), phải vẽ **2 khung bounding box riêng biệt** cho 2 cụm đèn đó.

## 3. Geometry rule

* **Công cụ:** Khung chữ nhật (Bounding Box).
* **Quy tắc vẽ (Tightness):** Khung chữ nhật phải ôm sát **chu vi của cụm vỏ đèn** (visible portion - bao gồm cả phần lưỡi trai che nắng của bóng đèn nếu nhìn rõ).
* **Tuyệt đối KHÔNG:** 
  * Không vẽ bao trùm luôn cả cột đèn, dây điện hoặc cần vươn của đèn.
  * Không chỉ khoanh mỗi cái bóng đèn đang sáng. Phải khoanh toàn bộ cụm vỏ chứa cả 3 bóng.
* **Quy tắc khi bị che khuất (Occlusion):** Chỉ khoanh ôm sát phần cụm vỏ đèn còn nhìn thấy được, tuyệt đối không tự nội suy (amodal) và vẽ tràn khung ra phần bị che bởi vật cản (biển báo, cây cối, xe tải).

## 4. Taxonomy

Bảng đầy đủ nằm ở `03_ontology_and_cvat_setup.md`. Dưới đây là taxonomy áp dụng trong CVAT:
* **Class:** `traffic_light`
* **Attribute 1 - `state` (Trạng thái màu):** 
  * `red`: Đang sáng Đỏ.
  * `green`: Đang sáng Xanh.
  * `yellow`: Đang sáng Vàng.
  * `off`: Không bóng nào sáng (đèn tắt / mất điện).
  * `unknown`: Thấy rõ cụm đèn nhưng bị lóa nắng, mờ sương, hoặc quá chói không thể phân biệt được màu.
  * *Default:* `__undefined__` (Bắt buộc người vẽ phải tự chọn, không được để trống).
* **Attribute 2 - `needs_review` (Đánh dấu cần xem xét):** 
  * `false` (Mặc định): Chắc chắn đèn này điều khiển làn của xe mình.
  * `true`: Dùng khi có sự mơ hồ, phân vân (xem mục 7).

## 5. Inclusion / exclusion

* **Bắt buộc label (Inclusion):** Bất kỳ cụm đèn đi thẳng nào dành cho xe mình, dù sáng hay tắt, miễn là kích thước cụm vỏ đèn **≥ 10 pixel** ở cả chiều ngang và dọc.
* **Trường hợp ignore (Exclusion - KHÔNG VẼ):**
  * Kích thước cụm đèn quá nhỏ, < 10 pixel (thường ở chân trời).
  * Cụm đèn hậu màu đỏ của ô tô phía trước (dễ nhầm vào ban đêm).
  * Các loại đèn đường, đèn chiếu sáng, đèn trang trí, biển quảng cáo LED.

## 6. Visibility / occlusion

* **Bị che khuất một phần (Occlusion):** Nếu đèn bị cành cây che mất một phần, vẽ khung bounding box bám sát rìa của phần vỏ đèn/bóng đèn còn hở ra.
* **Nhỏ / Xa:** Dưới 10 pixel thì bỏ qua hoàn toàn.
* **Loá nắng / Phản chiếu / Nhòe do ban đêm:** Vẫn vẽ Bounding box ôm sát quầng sáng của đèn (nếu không thấy vỏ đèn do đêm tối). Ở thuộc tính `state`, tuyệt đối không tự đoán màu. Bắt buộc chọn giá trị `unknown`.

## 7. Ambiguity / escalation

* **IGNORE (Bỏ qua):** Bằng chứng rõ ràng ngã tư có đèn rẽ trái và đèn đi thẳng, nhưng xe mình đang đè lên vạch rẽ trái $\rightarrow$ Ignore đèn đi thẳng, lúc này đèn đi thẳng là Out of scope.
* **ESCALATE (Báo cáo ca khó):** Đường không có vạch kẻ làn, xe đang đứng giữa đường, phía trước có 4 cụm đèn (vừa đi thẳng vừa rẽ) và không rõ đèn nào thực sự điều khiển xe mình $\rightarrow$ **Vẽ Bounding Box cho tất cả đèn**, chọn `state` hiện tại của đèn, đồng thời bắt buộc tick chọn **`needs_review = true`**.
* **UNKNOWN (Không rõ màu):** Khung cảnh sáng lóa, thấy vỏ đèn nhưng không rõ bóng nào đang sáng $\rightarrow$ Vẽ Bounding Box, chọn `state` = `unknown`.

## 8. Temporal rule

Không áp dụng — task ảnh tĩnh.

## 9. Examples

| sample_id | Thấy gì | Expected output | Rule áp dụng |
|---|---|---|---|
| BDD_example_01 | Ngã tư có 3 cụm đèn: 2 cụm đi thẳng màu xanh, 1 cụm mũi tên rẽ trái màu đỏ. Xe đang đi thẳng. | Vẽ 2 bounding box cho 2 cụm đèn xanh. `state` = `green`, `needs_review` = `false`. Bỏ qua cụm đèn rẽ trái. | Mục 1 (Out of scope) và Mục 4. |
| BDD_example_02 | Đèn treo ngang giữa trời nắng gắt, chói lóa trắng xóa, vỏ đèn bị cây che khuất một nửa. | Vẽ khung chữ nhật tight sát phần vỏ đèn còn thò ra khỏi cành cây. `state` = `unknown`, `needs_review` = `false`. | Mục 3 (Occlusion) và Mục 6 (Loá). |
| BDD_example_03 | Đèn mờ tít xa ở đường chân trời, zoom hết cỡ thấy kích thước khoảng 5 pixel. | Không vẽ gì cả (Ignore). | Mục 5 (Exclusion < 10 pixel). |
| BDD_example_04 | Trời tối đen, không thấy vỏ đèn, chỉ thấy một quầng sáng màu đỏ mờ mờ trên cao đúng vị trí ngã tư. | Vẽ bounding box ôm sát quầng sáng màu đỏ. `state` = `red`, `needs_review` = `false`. | Mục 6 (Visibility ban đêm). |

## 10. Common mistakes

* **Khoanh nhầm đèn mũi tên rẽ (Critical error):** Xe đang ở làn đi thẳng, nhưng người vẽ lại vẽ bounding box ôm lấy cụm đèn hình mũi tên rẽ trái/phải chuyên dụng. Hậu quả: AI học nhầm tín hiệu rẽ thành tín hiệu đi thẳng, gây tai nạn. $\rightarrow$ *Cách tránh:* Nhìn kỹ phần bóng đèn xem có hình mũi tên không, nếu có mũi tên mà xe mình đang đi thẳng thì BỎ QUA.
* **Vẽ bounding box quá lỏng (Geometry error):** Người vẽ khoanh lấn bao gồm cả không gian bầu trời, cột đèn và dây cáp treo đèn. $\rightarrow$ *Cách tránh:* Phóng to (Zoom) ảnh để canh các góc của Bounding box chạm sát các mép nhựa (vỏ) của cụm đèn.
* **Tự nội suy màu sắc (Hallucination):** Ảnh lóa nắng hoặc nhiễu không thể phân biệt được màu, nhưng người vẽ tự nhìn đèn xe bên cạnh để suy luận màu đèn hiện tại. $\rightarrow$ *Cách tránh:* Mắt người không thấy rõ thì máy cũng không thấy, nghiêm ngặt tuân thủ chọn `state` = `unknown`.
