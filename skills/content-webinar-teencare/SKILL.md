---
name: content-webinar-teencare
description: "Làm ảnh, viết kịch bản video, viết caption từ ảnh/kịch bản và dựng hoặc sửa video webinar TeenCare bằng HyperFrames. Dùng khi gọi Content Webinar TeenCare hoặc làm nội dung hội thảo Đồng hành cùng con tuổi dậy thì trong thời đại AI."
---

# Content Webinar TeenCare

Làm nội dung mời ba mẹ dự webinar theo trục **miễn phí + kiến thức cụ thể + cơ sở áp dụng vào tình huống của chính con**. Đúc kết từ brief/feedback của người dùng. Chỉ làm task được yêu cầu, không tự làm cả bốn đầu ra.

## Bắt đầu từ brief

- Xác định task, angle, POV/người nói, nguồn ảnh/voice/footage, format, độ dài và CTA. Kế thừa lựa chọn đã chốt; brief mới ưu tiên hơn ví dụ cũ. Đã đủ input thì thực hiện, không hỏi lại để duyệt lựa chọn thông thường.
- Đọc [campaign.md](references/campaign.md) để lấy thông tin đã xác nhận và nguồn. Giờ, offer, profile là cấu hình chiến dịch có thể thay đổi.
- Trong workspace TeenCare, tuân thủ `AGENTS.md`; đọc `product_info.md` và `customer_persona.md` khi làm copy. Không đọc `AGENT_KNOWLEDGE.md` trừ khi user yêu cầu dùng sổ tay; không tự cập nhật sổ tay chỉ vì gọi skill.
- Luồng mặc định là **đăng ký hội thảo miễn phí**, kèm tư vấn 1:1 miễn phí theo brief. Không chèn thanh toán 199K hoặc CTA mua khóa học vào luồng webinar.
- Bản giới thiệu chưa chỉ định POV mặc định người tư vấn nói với phụ huynh. Brief ghi mẹ/chuyên gia thì dùng đúng POV. Nếu cần POV khác mà không suy ra được, hỏi một câu. Với mẹ/chuyên gia/narrator, đọc tone và mẫu tương ứng trong workspace; mẫu để học giọng, không lấy làm nguồn claim.

## Bốn task

| Task | Đọc thêm | Đầu ra |
| --- | --- | --- |
| Làm/sửa ảnh | [images.md](references/images.md), skill `imagegen` | PNG + prompt; bản mới khi sửa |
| Viết/sửa kịch bản video | [scripts.md](references/scripts.md); [examples.md](references/examples.md) khi cần mẫu sales | Thoại hoàn chỉnh, POV, CTA, số đơn vị đã đếm |
| Caption từ ảnh/kịch bản | [captions.md](references/captions.md) | Caption có thể đăng, đúng creative/offer |
| Dựng/sửa video | [video-editing.md](references/video-editing.md), skill `hyperframes` | Project sửa tiếp được, preview, MP4 khi được yêu cầu xuất |

Khi học video mẫu, đọc [video-references.md](references/video-references.md). **VPV103 ưu tiên do user đánh dấu thắng mạnh nhất**; không suy diễn số liệu/lý do thắng. Free3/5/6 là nhánh người nói trực tiếp. Chỉ viết copy thì không tải video hoặc khởi tạo HyperFrames máy móc.

## Giữ các quyết định này

1. **AI là bối cảnh thực tế**, không chỉ tên hội thảo: con hỏi AI bài tập/lời khuyên, ba mẹ tìm cách trò chuyện; câu trả lời nhanh vẫn cần cân nhắc theo hoàn cảnh con. Không tự thêm tính năng app AI, chẩn đoán hoặc nội dung dạy công cụ AI.
2. **Giải pháp khớp hook**: vấn đề → điều ba mẹ còn thiếu → kiến thức webinar giúp nhìn lại vấn đề thế nào → tư vấn tình huống riêng → đăng ký. Không kể đau dài rồi chốt vài câu giới thiệu.
3. **Văn nói, một người xuyên suốt** mặc định. Khẩu ngữ có chủ đích, câu đọc được; không tự thêm thoại người nghe. Cảnh báo/gay gắt → thấu cảm dùng cho angle xung đột theo brief; không ép giọng gay gắt lên bản sales giới thiệu miễn phí.
4. **Miễn phí có giá trị**: nêu học gì, không chỉ lặp miễn phí. Không hứa webinar sửa ngay hành vi, giải quyết mọi mâu thuẫn hoặc thay thế hỗ trợ chuyên môn cần thiết.
5. **Ảnh cam–kem–đen**, đúng mặt cô Giang, sáng mịn tự nhiên. Template poster đã chốt bỏ thứ/ngày và câu “Hiểu đúng con • Đồng hành từ gốc”; không tự đưa lại khi sửa template đó.
6. Khi sửa, giữ bản đã chốt và chỉ chỉnh phần feedback cùng những phần phụ thuộc cần thiết.

## Kiểm tra và giao

- Đối chiếu tên webinar, 8–18 tuổi, giờ/nền tảng, cô Giang, miễn phí và CTA giữa các đầu ra. Nguồn cũ khác brief thì dùng brief mới, ghi nguồn được chọn.
- Script mặc định **300 đơn vị theo khoảng trắng** nếu brief webinar không yêu cầu mức khác. Không tính nhãn POV, phân cảnh hoặc ghi chú. Đếm lại sau sửa cuối, không cắt thành câu sai để khớp số.
- Rà dấu tiếng Việt, logic vấn đề–kiến thức–áp dụng, claim và văn nói.
- Lưu theo nơi user chọn; mặc định `Output/` trong workspace hiện tại, tên không dấu, phiên bản mới khi sửa. Ảnh/video có link file cuối; video giữ project/nguồn. Copy chỉ trong chat dùng writing block theo giao diện, không tự lưu nếu không cần.

## Dùng Capcut preset trong video

Khi brief có mã/đường dẫn từ Capcut preset, dùng skill `capcut-preset` tìm thư viện và đọc `AI_README.md` cùng chỉ mục. Dùng HyperFrames cho lớp text/bubble/animation/sticker theo quy tắc đó; giữ quy trình FFmpeg chuẩn bị video nền của project. Yêu cầu backend khác được người dùng chỉ định rõ vẫn ưu tiên.

Text Effect/Bubble phải mang chữ thật; In/Loop/Out gắn với đúng text và timing. Sticker dùng file gốc đầy đủ và giữ chuyển động/alpha. Thêm chỉ dẫn đọc quy tắc preset vào `AGENTS.md` của project, kế thừa nội dung khác; kiểm tra các preset thực sự dùng trong file video xuất và ghi rõ phần gần đúng/chưa kiểm chứng. Chỉ mở/chọn mẫu/viết kịch bản thì hoàn thành đúng việc đó, không tự dựng video.
