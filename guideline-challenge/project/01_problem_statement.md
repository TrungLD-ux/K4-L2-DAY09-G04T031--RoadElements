# Problem statement + downstream contract

Tối đa nửa trang, viết **trước khi mở CVAT**. Đây là bằng chứng của gate G1 (topic lock). 

## Bài toán

Phát hiện và phân loại trạng thái (màu sắc) của các cụm đèn giao thông điều khiển trực tiếp hướng đi thẳng của xe (ego-vehicle) trong các điều kiện môi trường phức tạp (chói sáng, ban đêm, ảnh mờ, khoảng cách xa).

## Downstream contract

1. **Downstream task / model / user là ai?** 
   Mô hình thị giác máy tính (Perception Model) của hệ thống xe tự lái; Kỹ sư phát triển hệ thống ADAS.
2. **Output annotation nào thực sự cần?** 
   Hình học (`geometry` là Bounding Box dạng rectangle), nhãn (`class` là `traffic_light`), và các thuộc tính (`state`: red, green, yellow, off, unknown; `needs_review`: true/false).
3. **Failure nào gây hậu quả lớn nhất?** 
   Vẽ nhầm đèn rẽ trái/phải thành đèn đi thẳng, hoặc nhận diện sai trạng thái (ví dụ: đèn đỏ nhưng gán nhãn xanh hoặc không label). Điều này khiến model học sai, xe tự lái sẽ vượt đèn đỏ và gây tai nạn nghiêm trọng (lỗi `critical`).
4. **Khi ambiguity không resolve được, ai / ở đâu là escalation path?** 
   Người gán nhãn sẽ tick chọn `needs_review = true` (chọn `state = unknown`), sau đó đưa lên cho QA Owner (Nhóm trưởng) hoặc Lab Coach quyết định cuối cùng.

## Scope

- **Trong scope (bắt buộc label):** Các cụm đèn giao thông vật lý dành cho xe cơ giới, nằm trên hướng đi thẳng của ego-vehicle, có thể nhìn thấy rõ vỏ đèn hoặc tín hiệu đủ lớn (>= 10px).
- **Ngoài scope (ignore):** Đèn tín hiệu cho người đi bộ, đèn điều khiển hướng rẽ không liên quan, đèn quá nhỏ tít chân trời (dưới 10px), hoặc biển báo giao thông phản quang.
- **Geometry tolerance:** Bounding box ôm khít phần vỏ cụm đèn vật lý nhìn thấy được (không bao gồm cột sắt, dây điện hay giá đỡ), lệch ≤ 2 px mỗi cạnh là đạt. Trừ trường hợp trời tối đen chỉ thấy quầng sáng thì ôm khít quầng sáng tín hiệu.

## Output chấm được

Quyết định trong blind test sẽ bao gồm:
- **LABEL:** Tạo bounding box hợp lệ kèm class `traffic_light` và thuộc tính `state` chính xác.
- **IGNORE:** Không tạo bất kỳ annotation nào cho các đối tượng out-of-scope (đèn cho người đi bộ, đèn rẽ, biển báo).
- **UNKNOWN:** Gán `state = unknown` cho trường hợp đèn bị chói lóa mù màu không thể xác định bằng mắt thường.
- **ESCALATE:** Đánh dấu `needs_review = true`.

## Dữ liệu và giới hạn

- **Nguồn ảnh:** Trích xuất từ bộ dữ liệu `bdd100k` và `lisa` nằm trong thư mục `data/`.
- **Giới hạn đã biết:** Dữ liệu có nhiều khung hình ban đêm bị lóa sáng mạnh khiến đèn chập vào nhau, hoặc kính xe đọng nước gây nhòe mờ tín hiệu. Với tập `lisa`, một số ảnh trích từ clip liên tiếp nên có bối cảnh rất giống nhau.
