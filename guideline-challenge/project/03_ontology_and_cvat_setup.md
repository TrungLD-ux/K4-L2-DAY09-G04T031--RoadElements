# Ontology + CVAT setup

Bảng ontology là **source of truth** cho schema CVAT: `03_cvat_labels.json` phải khớp từng dòng ở đây. Thay mọi
placeholder mới là xong (gate G2).

## Ontology table

| Name | Geometry | Type (class / attribute) | Allowed values | Default | Mutable? | Rationale |
|---|---|---|---|---|---|---|
| traffic_light | Bounding Box | class | - | - | - | Đối tượng chính cần gắn nhãn là cụm đèn giao thông |
| state | - | attribute | `__undefined__`, red, green, yellow, off, unknown | `__undefined__` | False | Ghi trạng thái hiện tại của đèn và buộc annotator phải tự chọn |
| needs_review | - | attribute | true, false | false | False | Đánh dấu các trường hợp khó hoặc chưa chắc để xem lại |

## Class hay attribute

`traffic_light` là class vì đây là đối tượng chính cần vẽ bounding box.

`state` là attribute vì red, green, yellow, off, unknown chỉ là trạng thái của cùng một đối tượng `traffic_light`, không phải các class riêng.

`needs_review` là attribute vì chỉ dùng để đánh dấu đối tượng cần kiểm tra lại.

Default `state = __undefined__` giúp tránh bias do annotator quên đổi trạng thái. Default `needs_review = false` có thể khiến annotator quên đánh dấu ca khó, nên guideline phải ghi rõ khi nào cần bật.

## CVAT

- **Phiên bản CVAT** (`make cvat-status`): 2.75.1
- **Tên task calibration**: `T031-calibration`
- **Guide của task đã dán `02_guideline.md`?** có
- **Nhóm dùng Track hay Shape, vì sao:** Shape, vì dữ liệu là ảnh tĩnh, không phải video.

## Setup test

Nhóm có 3 thành viên và cả 3 đều đã tham gia setup, nên chưa có thành viên độc lập để thực hiện setup test theo đúng yêu cầu.

Khi mở task, nhóm xác định:
- Label: `traffic_light`
- Tool: Rectangle / Bounding Box
- Attribute cần gán: `state`
- Bật `needs_review` khi đèn bị che, quá nhỏ, khó xác định màu hoặc không chắc cách gán nhãn.