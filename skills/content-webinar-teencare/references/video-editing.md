# Dựng/sửa video bằng HyperFrames

Đây là quyết định creative TeenCare, **không thay hợp đồng kỹ thuật HyperFrames**. Chỉ dựng khi được yêu cầu video; viết script không tự tạo avatar/voice, gọi dịch vụ hay render.

## Route/nguồn

- Đọc skill `hyperframes` entry point trước khi tạo/sửa; đi theo workflow/domain hiện hành, không đóng băng version/lệnh cũ.
- Custom recut/trộn footage: `general-video` + `hyperframes-core`; timing do framework quản lý. Caption thuần/overlay giữ footage có route riêng theo entry point.
- `hyperframes-cli` cho check/preview/render; `media-use` cho nguồn/xử lý; `hyperframes-keyframes` cho zoom; `hyperframes-audio` cho mix/duck/fade; Registry theo domain khi cần effect.
- Đọc `teencare-video-editor` khi chọn source/brief/layout TeenCare. Máy này có `E:/HYPERFRAME/hyperframes.cmd`; kiểm tra tồn tại, dùng theo version/hợp đồng project hiện hành.
- Project đang sửa: kế thừa brief/timeline/history/lựa chọn user, không lại intake. Video mới đủ brief thì không hỏi lại.

Xác định script cuối, voice/footage người nói, poster/profile, cảnh webinar/gia đình/tư vấn/form và thời lượng/tỷ lệ. Thiếu voice chính thì hỏi phần đó, không âm thầm clone. Một người nói xuyên suốt trừ brief khác. Copy nguồn dùng vào project/ánh xạ theo framework, giữ nguồn gốc. Xem clip thật trước khi chọn range. Video full tham khảo ở workspace, không nhúng hàng trăm MB vào skill.

## Creative

- Mẫu ưu tiên VPV103: mời/miễn phí → hình kiến thức thật → đời sống → tư vấn riêng miễn phí → đăng ký. Đọc [video-references.md](video-references.md). Dùng logic nối, không copy cứng timecode/mọi cảnh.
- Tham khảo 9:16, 1080×1920, 30 fps; đổi theo kênh/brief. Không ép script 300 đơn vị thành 49 hoặc 70 giây.
- Người tư vấn có thể khác cô Giang. Giữ danh tính; không tự gọi avatar sales là cô Giang. AI voice/avatar dùng theo nguồn/cách user đã chọn.
- Nói miễn phí thì chữ nổi bật. Nói kiến thức thì webinar thật/slide + profile, slide phải đọc được. Nói con thì trám đúng hành động. Nói 1:1 thì hình tương tác phù hợp. CTA thì form hoặc card hành động rõ.
- Không chỉ chạy poster bất động suốt bản yêu cầu footage; không thêm trám vô nghĩa. Cảnh minh họa không tự thành case trước/sau. Không lấy comment/số cũ làm social proof mới.

## Chữ/màu/nhịp

Poster/profile/card dùng cam–kem–đen. Overlay footage ưu tiên contrast; trắng/vàng có viền, box vàng chữ đen là phương án TeenCare hiện hành, không ép footage thành cam. Xanh lá “MIỄN PHÍ” là look VPV103, kế thừa khi user chọn hoặc có lợi cho contrast.

- Một text box overlay chính tại một lúc theo `teencare-video-editor`; không đếm card/profile hoặc UI nguồn vốn có như nhiều caption overlay.
- Subtitle theo cụm nghĩa/voice thật, keyword lúc được nói; không dán toàn thoại. Header có thể giữ nếu không che mặt/slide, không ép fixed header lên mọi cảnh.
- Không che mặt/miệng/tay/UI/chữ gốc. Safe area theo canvas; kiểm tra dấu, line break và lúc animation lớn nhất.
- Cut theo ý/voice. Nhạc/SFX phục vụ giọng, mix bằng graph HyperFrames. Thumbnail không chứng minh audio mẫu.

## Bản giao

Cue gồm ý voice, range audio/source, hình, text, duration. Tính lại sau đổi timing/tốc độ; không đoán cue từ số từ. Talking head khớp môi/voice, không tự tạo TTS vá lời đọc lỗi.

Check/lint/render theo workflow; xem đầu/giữa/cuối layout và điểm nối; nghe voice, nhạc/SFX và đầu/cuối câu. Preview theo entry point, xuất MP4 khi user yêu cầu dựng/xuất. Đo duration/kích thước/FPS/codec, kiểm tra MP4 đủ hình/tiếng.

Giữ project, preview và bản trước; giao MP4 cuối + project + tóm tắt. Chỉ được yêu cầu brief/storyboard thì giao tài liệu đó, không tự dựng.
