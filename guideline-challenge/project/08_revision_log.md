# Revision log

| Version | Đổi gì | Vì sao | Bằng chứng |
|---|---|---|---|
| v2 | 2026-09-26: thống nhất ngưỡng hai chiều, unknown cần review, tách màu khỏi geometry | BDD15/17/20 có lỗi cùng mắc; BDD21 khác state; BDD25 khác count và biên | Hai ZIP gốc, 06_calibration_measure.csv, 06_calibration_report.csv |
| v2 | Bổ sung kiểm instance theo vị trí, không chỉ count; loại ví dụ ID giả và gold ngoài blind | LISA03 cùng count=5 và 5 red nhưng các vị trí/nhóm box khác nhau; gold cũ không đúng split | XML job 25 và job 18; evidence_before_review/gold_decisions.csv |

Đã đo lượt calibration đầu, chưa đo lại sau rework. V2 là bản sửa từ các phát hiện này. Đã có v3 từ review export peer; nhận xét do owner tổng hợp, số câu hỏi dùng khoảng 5–20 do người dùng cung cấp. Gold và sample pack giữ nguyên sau freeze; xác minh bằng lab9.py verify.
| v3 | Bổ sung checklist trước export: undefined, hai chiều 10px, unknown/review, loại mũi tên, biên vỏ và halo | Lỗi thực trong peer output: BDD18 undefined; BDD22 dưới ngưỡng và thiếu review; LISA08 đèn rẽ; hai geometry chưa đạt | 07_blind_handoff/peer_output/peer_output.zip; transfer_score.csv; peer_review.md; chưa có feedback tự thuật |

GTS cuối hồ sơ: 61.3/100; I=0 theo khoảng 5–20 câu hỏi. Nguồn lưu trong clarification_count.json, cách tính trong gts_notes.md. Không thay gold sau freeze.
