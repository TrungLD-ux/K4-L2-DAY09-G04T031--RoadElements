# Nhận xét blind test và hướng xử lý

- Nhóm peer: team03.
- Tài khoản owner trong export: Dai, job 17.
- Nguồn đánh giá: peer_output.zip và đối chiếu guideline v2 đã freeze.
- Người tổng hợp nhận xét: nhóm owner G04T031. Nội dung dưới đây là đánh giá từ kết quả gán nhãn, không phải trích lời peer.

## 1. Nhận xét
1. **Điểm rõ:** Một cụm đèn là một box; trạng thái màu được chọn bằng thuộc tính state.
2. **Điểm cần nhấn mạnh:** Cách khoanh đèn bị lóa và ngưỡng 10 px cần có bước kiểm tra riêng trước export.
3. **Ảnh khó:** BDD26 khó xác định biên do lóa; LISA08 có đèn mũi tên dễ bị đưa nhầm vào phạm vi đi thẳng.
4. **Thao tác dễ sai:** Bỏ sót state ở __undefined__; chọn unknown nhưng chưa bật needs_review.
5. **Cải tiến:** Dùng checklist ngắn để kiểm state, kích thước, review, đèn rẽ và biên box.

## 2. Phân loại và xử lý
- **BDD18 — execution_error:** Một state chưa chọn. Yêu cầu kiểm hết dropdown; review=true không thay thế state hợp lệ.
- **BDD22 — execution_error:** Hai box dưới ngưỡng, đều unknown nhưng review=false. Loại box dưới ngưỡng; không kéo rộng box để đủ 10 px.
- **LISA08 — execution_error, critical:** Khoanh đèn mũi tên rẽ trái. Loại cụm này khỏi phạm vi đi thẳng; kiểm hình tín hiệu trước kiểm màu.
- **BDD26 — data_ambiguity:** Lóa gây khó xác định biên. Giữ màu quan sát được, dùng review và tránh khoanh cả halo.
- **Geometry — guideline_gap:** Cần checklist rõ hơn về phần vỏ/chụp nhô ra và biên lõi sáng. Đã bổ sung mục 11 trong guideline v3.

## 3. Kết quả sửa guideline
V3 bổ sung kiểm đủ state, ngưỡng cả hai chiều, unknown/review, phân biệt mũi tên và kiểm biên. Giữ export lượt đầu và gold freeze để đánh giá chuyển giao; chưa có lượt gán lại để đo hiệu quả v3.

## 4. Mức độc lập
Người dùng cung cấp khoảng ước lượng 5–20 câu hỏi trong lúc làm. Toàn bộ khoảng thuộc mức I=0 theo rubric. Xem clarification_count.json và gts_notes.md; chưa có bản ghi nội dung từng câu hỏi.