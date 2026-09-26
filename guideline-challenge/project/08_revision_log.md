# Revision log

Guideline v1 = bản nháp đầu; v2 = sau calibration nội bộ; v3 = sau blind handoff. Mỗi lần tăng `Version` trong
`02_guideline.md`, thêm một hoặc nhiều dòng vào bảng: đổi gì và vì sao, kèm bằng chứng (sample_id, dòng
calibration report, câu hỏi trong clarification log, feedback của peer).

Cột Version ghi dạng `v1`, `v2`, `v3` — `make status` tìm dòng bảng có `v2` và dòng có `v3`.

| Version | Đổi gì | Vì sao | Bằng chứng |

| v2 | 2026-09-26| Sau calibration | Làm rõ quy tắc xác định `state = unknown`, phân biệt `off` và `unknown`; làm rõ mỗi cụm đèn vật lý là một instance riêng; bổ sung cách xử lý khi có nhiều cụm đèn và khi không xác định được cụm trực tiếp điều khiển ego-vehicle. |
