| Name | Geometry | Class/Attribute | Allowed values | Default | Mutable? | Rationale |
|---|---|---|---|---|---|---|
| traffic_light | Bounding Box | Class | - | - | - | Đơn vị đo lường chính là cụm vỏ đèn |
| state | - | Attribute | red, green, yellow, off, unknown | `__undefined__` | False | Xác định màu hiện tại của đèn. Ép annotator tự chọn |
| needs_review | - | Attribute | true, false | false | False | Dùng để đánh dấu các ca khó |