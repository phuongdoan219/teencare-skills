# VPV107: hook trước/sau và các sửa đổi đã chốt

Đọc khi cần một ví dụ thực tế về hook trước/sau, chữ gọn và người thật. Đây là kết quả của brief/source VPV107, không phải template bắt buộc cho mọi TeenCare. Các lựa chọn phong cách hiện hành nằm trong `SKILL.md` và `layout-and-audio.md`; brief/góp ý mới được ưu tiên.

Brief: `E:/Teencare/Video ads/VPV107/Brief AI edit.xlsx`. Bản giao cuối v3: `E:/Teencare/Video ads/VPV107/VPV107-v3.mp4`. Chỉ tham chiếu khi file còn tồn tại; skill không cần project này để dựng video khác và không chứa footage/voice riêng.

## Bố cục hook cuối

Canvas 1080 × 1920, 30fps. Hook dài 3,933333 giây, dùng C8141 với nền gốc; hai source trước/sau vẫn chuyển động.

| Vùng | Bố trí cuối |
| --- | --- |
| Trước/sau | Hai ô 540 × 540, bo góc 28px, y=0, chạm mép trên và hai bên; nhãn chữ trần trắng/vàng có viền tối |
| Tiêu đề | Dải y=540–780, chữ bắt đầu y=550, căn giữa; “1 NGÀY CỦA CON” 110px trắng; “TRƯỚC & SAU TEENCARE” 76px vàng `#ffc843` |
| Chữ | Be Vietnam Pro Black 900, nền xanh đậm `#153b45`, viền/bóng; pop nhẹ hoàn tất trước 0,4 giây; không có text box |
| Chuyên gia | y=780, cao 1140px đến đáy; video giữ nền gốc, `object-position: 50% 68%` phù hợp source này; đầu gần mép trên, thấy thân và cử chỉ |

Preview đầu v3 có khoảng trống 80px phía trên, dải tiêu đề ba dòng cao 520px và vùng chuyên gia chỉ 760px từ y=1160. Người dùng yêu cầu bỏ các vùng trống đã khoanh. Bản cuối đưa hai ô sát mép trên, tiêu đề thành hai dòng gần kín chiều ngang, đẩy vùng chuyên gia lên 380px và tăng diện tích hiển thị 50%. Không đặt tiêu đề cố định tại y=960 rồi tạo khoảng rỗng để giữ tọa độ đó; cân bố cục theo hình và góp ý mới.

## Các sửa đổi còn lại

- Từ sau hook, bỏ dải text/branding kem phía dưới. Caption ở vùng trống gần trung tâm, có effect và tránh mặt. Box vàng chữ đen, padding hẹp; câu phụ/nhãn không có box. Tối đa một box overlay hiển thị cùng lúc.
- Cảnh tự giác phải thấy con thực sự làm việc: quét nhà và sắp sách trên bàn. Đã thay đoạn chọn sai; feedback “giây 16” thuộc v1, sau tăng tốc cảnh này bắt đầu khoảng 12,57s.
- Cảnh tối dùng chuyên gia tách nền nhỏ 620px trên canvas rộng 1080, mép thân chạm đáy, viền trắng silhouette 7px; không che cảnh con học. Feedback “giây 35” thuộc v1, cảnh tối ở v2/v3 bắt đầu 29s. Kích thước này chỉ dành cho overlay đó, khác chuyên gia là hình chính ở hook.
- App dùng đúng `E:/Teencare/Video ads/VPV106/khung app teencare AI.jpg`; crop bezel source và đặt UI theo vùng trong khung, giữ tỷ lệ và thao tác thật.
- Toàn bộ voice tăng khoảng 1,22×, giữ cao độ; hình chuyên gia đồng bộ. Tính lại mốc cảnh/text/SFX. Bản cuối 2069 frame, 30fps, 68,967 giây, đạt trần 70 giây đã yêu cầu.

Đã kiểm tra hook lúc bắt đầu, pop, giữa và cuối cùng ảnh từ MP4 thực tế; full check không lỗi/cảnh báo. Bài học tái dùng là loại khoảng trống dư, tận dụng chiều ngang cho chữ, bảo vệ mặt/cử chỉ và phân biệt chuyên gia là hình chính với chuyên gia overlay. Source, timestamp, tọa độ, font size, rate và trần 70 giây phải đối chiếu lại với brief mới.
