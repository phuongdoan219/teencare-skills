# Thư viện text và icon có mã

Ảnh gốc do người dùng gửi ngày 13/10/2026 lưu trong `assets/text-library/`. [Xem thư viện](../assets/text-library/library.html); [catalog có cấu trúc](../assets/text-library/catalog.json). Giữ mã ổn định, mẫu mới dùng mã tiếp theo. Giá/số lượng/lời cam kết trong ảnh chỉ là tham khảo hình thức; không sao chép vào nội dung TeenCare nếu kịch bản không có.

| Mã | Mẫu | Thành phần chính |
| --- | --- | --- |
| TC-T01 | Thẻ trắng + tick xanh | Nền trắng bo góc, chữ đen; ý/số chính đỏ; tick xanh. |
| TC-T02 | Sticker mint | Chữ mint, viền đen, trắng ngoài, glow mint. |
| TC-T03 | Box đen viền trắng | Chữ vàng, box đen bo góc, viền trắng dày. |
| TC-T04 | CTA đỏ + tay chỉ | Chữ trắng condensed trên box đỏ viền đen, tay chỉ. |
| TC-T05 | Chữ vàng ba lớp viền | Fill vàng, stroke đen dày, trắng ngoài, halo vàng; không box. |
| TC-T06 | Hai tầng vàng–đỏ | Dòng chính vàng có stroke; dòng phụ đỏ nghiêng viền trắng. |
| TC-T07 | Chữ trắng halo vàng | Chữ trắng viền đen, halo vàng mỏng. |
| TC-T08 | Dải đỏ hai đường trắng | Chữ trắng đậm, nền đỏ, đường trắng trên/dưới. |
| TC-FX01 | Cảnh báo đỏ/vàng | Ảnh thứ 9: halo/icon cảnh báo, thuộc overlay, không phải mẫu text. |
| TC-T09 | Tick + chữ vàng nghiêng | Ảnh thứ 10: tick xanh, chữ vàng hơi nghiêng, stroke đen/trắng. |

Icon dùng kèm: **TC-I01** khoanh đỏ vẽ theo nét SVG; **TC-I02** mũi tên draw-on rồi chuyển động nhẹ; **TC-I03** tick xanh vẽ nét trong thẻ. TC-FX01 chỉ dùng khi kịch bản có ý cảnh báo; không gán chẩn đoán hoặc lỗi cho người trong footage.

## Note trong brief cho AI

Giữ cột C là keyword người xem đọc. Cột D thêm mã và cách dựng: `Text: TC-T05; motion: pop ngắn rồi giữ; vị trí: giữa thân dưới mặt; Icon: TC-I01 khoanh “3 KHÔNG” theo voice`. Cột E vẫn là đường dẫn source, không trộn mã vào path. Nếu có cột Note riêng thì có thể ghi mã ở đó, vẫn mô tả hình và bố cục ở D.

Mỗi video thường chọn 2–3 mẫu chữ; đó là số mẫu, không phải số cue. Manifest ghi `textStyle`, `motion`, `iconStyle`. Ví dụ KB3 revision 3: TC-T05 cho hook/keyword, TC-T01 cho kỹ năng/ý xác nhận, TC-T08 cho CTA. Motion là thuộc tính riêng; không đổi mã mẫu chỉ vì đổi kiểu vào chữ.

Mã giữ cấu trúc mẫu; màu có thể biến thể theo brief, không bắt buộc màu thương hiệu. Ghi thêm `palette` hoặc màu fill/box/viền, ví dụ `TC-T08; box tím #542499; chữ trắng`. Hook nhiều dòng xen chữ rời và một cụm có nền box; frame 1–2 đan xen chữ rời/text box và màu, tránh toàn bộ cụm cùng một màu. KB3 v4: “30 NGÀY” vàng, dòng phụ trắng, “3 KHÔNG” box tím chữ trắng; ba ý “không” lần lượt chữ mint, box đỏ chữ trắng, chữ vàng.

Chỉ chọn **2–3 màu chủ đạo cho một video và giữ palette cố định** qua các frame; đổi giữa các màu đã chọn, không tự thêm màu theo từng cue. Chữ rời, text box và motion tạo nhịp, không cần thêm màu. Icon/tick/viền cũng theo palette; màu trong ảnh mẫu là mặc định, ghi rõ biến thể khi đổi. Chữ đen/viền đen là mực trung tính để giữ tương phản. Nếu hook đã được duyệt riêng thì giữ nguyên hook. KB3 v5 giữ toàn bộ frame 1 và thống nhất overlay frame 2–11 bằng vàng #fff200, trắng #fff, tím #542499.

KB3 v6 sửa phạm vi giữ hook: chỉ ba dòng “30 NGÀY / Trở thành người mẹ / 3 KHÔNG” trong ảnh được giữ nguyên, không giữ màu của cả frame 1. Các ý “không” và “có” thống nhất trắng/vàng/tím; CTA cuối là ngoại lệ nền đỏ #db121b, chữ trắng theo yêu cầu. Khi ảnh duyệt chỉ một cụm text, áp ngoại lệ đúng cụm đó.

## Dựng theo mẫu

Tái tạo bằng text thật, local font có dấu và GSAP seek-safe, không dán screenshot chứa lời quảng cáo khác vào video. Phối 2–3 chuyển động ngắn theo ý: pop/scale settle, trượt ngang, nhấc lên xoay nhẹ, word cascade hoặc mask reveal. Chỉ gọi “word cascade” khi từng từ thực sự vào lần lượt. Giữ đủ thời gian đọc sau motion.

Ưu tiên keyword ở giữa khung dọc, tránh vùng dễ xén của ads. Chỉ đưa lên trên khi giữa che mặt, tay/hành động hoặc UI, hay vị trí phía trên cho bố cục đẹp hơn. Kiểm tra crop/zoom lớn nhất. Chỉ một box overlay cùng lúc; chữ phụ, khoanh và mũi tên không tạo thêm box. Halo và stroke tách chữ, không phủ mờ mặt.

Khoanh phải bao quanh ý hoặc vùng cần xem; mũi tên hướng tới một đối tượng thật. Vẽ nét 0,25–0,5 giây, dịch/nhấp nhẹ rồi giữ, tránh rung liên tục. Dùng Registry `marker-highlight`/`hw-arrow` hoặc recipe SVG draw tương ứng và nạp logic vào composition; cài component chưa phải áp hiệu ứng.
