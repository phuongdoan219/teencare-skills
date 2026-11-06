---
name: teencare-video-editor
description: "Lập brief, chọn source local, dựng hoặc sửa video quảng cáo TeenCare bằng HyperFrames; bàn giao video lên Google Drive, viết caption và cập nhật bảng Ads lấy content theo yêu cầu. Dùng cho video chuyên gia, Mentor 1:1, kỹ năng sống, phụ huynh/học sinh và TeenCare AI."
---

# Dựng video TeenCare bằng HyperFrames

Biến thoại thành brief phân cảnh hoặc video theo nội dung và nguồn thực tế. Khi chỉ được yêu cầu điền bảng/chọn nguồn, hoàn tất bảng và dừng ở đó. Kế thừa lựa chọn đã chốt khi sửa project; với video mới, chọn bố cục theo hook, thoại và source. Yêu cầu hiện tại của người dùng ưu tiên hơn các ví dụ trong skill.

## Khởi động đúng project

- Xác định brief, nhóm source chính, cảnh trám, app, nguồn voice và project/output. Đã đủ thông tin thì dựng ngay; chỉ hỏi phần thiếu làm ảnh hưởng quyết định dựng. Khi người dùng đang hỏi ý tưởng, trả lời/propose trước, không tự xuất một bản khác chỉ vì có câu hỏi.
- Đọc `AGENTS.md` của workspace và project. Trước khi tạo/sửa composition, dùng skill `hyperframes`, rồi các domain nó yêu cầu. Skill này bổ sung quyết định dựng TeenCare, không thay hợp đồng HyperFrames.
- Trên máy này, chạy CLI bằng `E:/HYPERFRAME/hyperframes.cmd`; wrapper dùng bộ npm/FFmpeg/FFprobe và cache trên ổ E. Tôn trọng cấu hình pin/version của project theo router; không hardcode một phiên bản cũ vào skill.
- Nhánh dựng custom: `general-video` + `hyperframes-core`. Cắt/chọn media, tách nền, xử lý rotation/HDR: `media-use`. Zoom: `hyperframes-keyframes`. Mix tiếng: `hyperframes-audio`. Kiểm tra/preview/render: `hyperframes-cli`. Đọc Excel theo skill spreadsheets khi cần phân tích workbook.
- Package dùng chung ở `E:/HYPERFRAME/tools/node_modules/` chỉ là công cụ có sẵn. Nạp runtime hoặc đưa asset cần dùng vào project trước khi đặt hiệu ứng; cài package không đồng nghĩa hiệu ứng đã được áp dụng.

## Các nguyên tắc dựng TeenCare

- **Quy trình FFmpeg trước, HyperFrames sau (người dùng chốt 31/10/2026):** đọc kịch bản → xác định thoại, mô tả hình và source IN/OUT → dùng FFmpeg cắt ghép source, crop/layout/PIP, phối voice/nhạc thành video nền → dùng HyperFrames tạo text, animation và sticker trên video nền đó. Giữ plan/timecode và phần nền riêng để sửa lớp chữ mà không dựng lại source. Không đặt toàn bộ các clip source rời vào HyperFrames làm backend cắt ghép chính khi đang theo quy trình này. Với project cũ, có thể tái dùng các đoạn đã chuẩn bị và voice đã căn nếu khớp brief; báo rõ nguồn bị thiếu hoặc bản dựng được kế thừa.

- Với kịch bản chuyên gia, ưu tiên mở đầu bằng source chuyên gia gốc, giữ chuyên gia là hình chính; có thể chèn ảnh/video khung vuông để minh họa, rồi tăng dần cảnh trám ở các đoạn sau. Giữ voice chuyên gia dưới cảnh trám. Đây là lựa chọn mặc định cho nhánh chuyên gia, không áp lên mọi loại video.
- Khi tự chọn cảnh trám trong `E:\Teencare\Source quay`, giới hạn tối đa **3 folder diễn viên khác nhau** trong một kịch bản; dùng ít hơn nếu đã đủ cảnh. App lấy từ `Source app Tinke`, tương tác cô với con/mẹ online lấy từ `Duet`; landingpage mới ưu tiên `E:\Teencare\Source quay\Landingpage.MP4`, freeze/crop phần giới thiệu lớp; `IMG_2201.MP4` là source cũ, chỉ dùng khi brief chọn lại. Xem file thật trước khi ghi hành động hoặc timecode. Quy ước điền ba cột và chọn nhóm nguồn nằm ở [brief-and-sources.md](references/brief-and-sources.md).
- Chọn mở đầu từ câu hook: giáo viên nói trực tiếp, hành động của phụ huynh/con, tương tác online, app hoặc một câu chữ ngắn. **Không mặc định mở đầu bằng ô vàng + text**, duet hay bộ số liệu 90%/5%.
- Theo brief và reference hiện tại. Font đậm hỗ trợ tiếng Việt; chọn **2–3 mẫu text** phù hợp từ [thư viện có mã](references/text-library.md). Box vàng/chữ đen dùng khi hợp lý; thẻ trắng, dải đỏ hoặc box đen theo mẫu đã chọn. Phối motion ngắn để tránh mọi cue đều pop giống nhau; không dùng footer cố định. Không đưa logo/phong cách VUIHOC sang TeenCare.
- Hook nhiều dòng cần phân cấp bằng màu và một cụm có nền box; không để tất cả dòng cùng màu/kiểu. Đan xen chữ rời với text box, nhưng chọn **2–3 màu chủ đạo cố định cho cả video**, không thêm màu mới ở mỗi frame. Có thể dùng màu ngoài thương hiệu; ghi palette cùng mã mẫu trong brief và giữ xuyên suốt các cue, box, tick, mũi tên/khoanh. Giữ nguyên đúng cụm text/bố cục hook được duyệt trong ảnh; không hiểu thành giữ nguyên mọi text trong cả frame. Các ý liệt kê “ba không” và “ba có” vẫn phải đồng bộ palette. CTA có thể là ngoại lệ đỏ/chữ trắng khi người dùng chỉ định.
- **Tối đa một text box overlay đang hiển thị tại mỗi thời điểm**, tính cả các nhãn có nền và lớp ở sub-composition khác. Chữ phụ dùng màu, viền/bóng, size hoặc motion để nhấn; nhãn trước/sau và thời điểm ưu tiên không có box. Chi tiết UI vốn có trong app không phải caption overlay.
- Tiêu đề hook và keyword ưu tiên **giữa video** vì mép trên dễ bị xén khi lên ads. Chọn vùng thân dưới mặt hoặc khoảng trống trung tâm; chỉ đưa lên trên khi giữa che mặt/hành động/UI hoặc bố cục trên đẹp và an toàn hơn. Cụm hook cần đủ nghĩa, font lớn, đọc ngay trên điện thoại. Với hook trước/sau kèm chuyên gia, ưu tiên vùng chữ gọn giữa hai cảnh trên và chuyên gia dưới. Loại padding rỗng ở mép trên, quanh chữ và trên đầu chuyên gia để tăng diện tích hình; chọn tọa độ theo source thực tế.
- Chữ và ảnh không che mặt, cử chỉ quan trọng, số liệu hoặc UI đang được minh họa. Caption đặt trong vùng trống gần trung tâm theo từng cảnh. Chữ xuất hiện theo cụm nghĩa của voice; những chữ cần biến mất cùng nhau dùng chung mốc kết thúc, không ước lượng độc lập.
- Bảng brief là nguồn kế hoạch, nhưng thoại phải khớp tiếng thật. Chọn đúng lần đọc, loại lời trao đổi/đọc lỗi; không tự bịa từ hoặc dùng TTS để vá một câu. Dùng voice clone/file voice riêng khi người dùng chỉ định, giữ đúng file và cắt theo kịch bản.
- Tăng tốc khi brief/mood yêu cầu và lời vẫn rõ. Giữ cao độ, đồng bộ video người nói với voice và tính lại cue text/SFX. Chọn rate theo giới hạn thời lượng rồi đo MP4 cuối; khi yêu cầu tối đa 1p10s, bản giao phải ≤70 giây. Rate và thời lượng cụ thể của video cũ không phải mặc định cho brief mới.
- Cảnh trám phải minh họa đúng câu. Xem hành động và range thực tế, kể cả khi lấy từ video đã edit. Không đoán nội dung chỉ từ tên file; không để caption/logo của sản phẩm khác lọt vào cảnh trám.
- Người nói/người nghe trong duet dùng video đang chuyển động. Cảnh nghe cần đang chú ý; muted footage vẫn nói hoặc làm việc riêng không phải cảnh nghe phù hợp. Giữ nền gốc khi người dùng đã chốt. Chuyên gia là hình chính cần đủ diện tích; chuyên gia chèn trên cảnh trám cần nhỏ vừa đủ, không che nội dung, thân chạm đáy/điểm tựa, có thể thêm viền trắng theo yêu cầu. Tách nền/crop phải giữ mặt và cử chỉ.
- Khi demo app: dùng đúng khung được chỉ định và ưu tiên diện tích đọc nội dung. Khung TeenCare đã chọn trên máy được ghi trong `references/layout-and-audio.md`. Nếu source đã có điện thoại mà background cũng có khung, crop bezel/tai thỏ và cho **nội dung app phủ đầy vùng lớn**, tránh khung lồng khung. Đưa tiêu đề ra vùng riêng; giữ tỷ lệ UI, video cuộn và thao tác thật.
- Nhạc và SFX phục vụ voice. Chọn ít điểm nhấn có nghĩa, dùng lại một số chất âm nhất quán. Tiếng chụp ảnh là lựa chọn phù hợp cho các số liệu khi người dùng chọn; không áp nó lên mọi caption.

Khi hook liệt kê từng chữ “không”, có thể zoom gần thêm từng nấc đúng onset voice; giữ mặt và tay trong khung, text đứng ổn định. Nhạc nhanh/thúc giục khi được yêu cầu, carve dưới voice, thêm SFX theo sự kiện. Icon nhẹ dùng TC-I01 khoanh đỏ, TC-I02 mũi tên chuyển động hoặc TC-I03 tick; chỉ vào ý/hành động thật.

## Đọc chi tiết theo việc đang làm

| Việc | Tài liệu |
| --- | --- |
| Đọc mẫu KB2, điền Text/Mô tả phân cảnh/Nguồn trong Google Sheets, chọn tối đa 3 folder diễn viên | [brief-and-sources.md](references/brief-and-sources.md) |
| Đọc brief dạng bảng, chọn source/retake, cắt voice, lập timeline | [brief-and-sources.md](references/brief-and-sources.md) |
| Chọn bố cục, chữ, crop/tách nền, khung app, nhạc và SFX | [layout-and-audio.md](references/layout-and-audio.md) |
| Chọn mã text/icon và ghi vào brief cho AI | [text-library.md](references/text-library.md) · [xem thư viện](assets/text-library/library.html) |
| Sửa theo timestamp/frame, xuất nhanh và kiểm tra bản giao | [revision-and-delivery.md](references/revision-and-delivery.md) |
| Upload bản giao lên Drive, viết caption và cập nhật tab Ads lấy content | [drive-and-content-sheet.md](references/drive-and-content-sheet.md) |
| Cần một ví dụ đã dựng và sửa, không phải template bắt buộc | [vpv106-example.md](references/vpv106-example.md) |
| Hook trước/sau, loại khoảng trống, box vàng/đen, chuyên gia và giới hạn 70 giây đã chốt ở VPV107 | [vpv107-example.md](references/vpv107-example.md) |

Hai helper đọc nguồn, không chỉnh media gốc:

- `scripts/extract_brief.py`: xuất ô, rich text/bold, link và vùng merge từ `.xlsx` ra JSON. Không tự coi B1 là câu đầu; giữ tọa độ để ánh xạ cột Thoại/Nguồn/Thể hiện.
- `scripts/inventory_sources.py`: dùng FFprobe để ghi duration, audio, FPS, rotation và màu. Inventory không thay việc xem/nghe source.

Dùng runtime Python từ `load_workspace_dependencies` nếu cần openpyxl. Chỉ chạy helper khi chưa có bản trích xuất/inventory còn dùng được.

## Giao kết quả

Sau sửa HTML, chạy full check theo hướng dẫn project; xem trước/sau các điểm sửa và kiểm tra MP4 thực tế. Giữ preview chạy khi người dùng đang xem. Khi đã được yêu cầu dựng/xuất, hoàn tất bản giao, không dừng ở preview hoặc lời hứa.

Giao MP4 trong folder người dùng chỉ định, link project có thể sửa và vài dòng nêu thay đổi/thời lượng. Giữ source và bản trước để tiếp tục sửa. Chỉ nói đã xem/nghe những phần thực sự được kiểm tra; phép đo âm lượng hoặc một ảnh không chứng minh toàn video đã được nghe/xem.

Khi người dùng yêu cầu upload hoặc bàn giao content cho team ads, dùng [quy trình Drive + Sheet](references/drive-and-content-sheet.md). Thực hiện các bước được yêu cầu: chỉ upload thì hoàn tất Drive; khi yêu cầu cập nhật bảng thì viết caption, gắn link bản giao và xác minh dòng mới. **VPV là mã video, VPA là mã ảnh; TC là mã caption độc lập.**

## Dùng Capcut preset trong video

Khi brief có mã/đường dẫn từ Capcut preset, dùng skill `capcut-preset` tìm thư viện và đọc `AI_README.md` cùng chỉ mục. Dùng HyperFrames cho lớp text/bubble/animation/sticker theo quy tắc đó; giữ quy trình FFmpeg chuẩn bị video nền của project. Yêu cầu backend khác được người dùng chỉ định rõ vẫn ưu tiên.

Text Effect/Bubble phải mang chữ thật; In/Loop/Out gắn với đúng text và timing. Sticker dùng file gốc đầy đủ và giữ chuyển động/alpha. Thêm chỉ dẫn đọc quy tắc preset vào `AGENTS.md` của project, kế thừa nội dung khác; kiểm tra các preset thực sự dùng trong file video xuất và ghi rõ phần gần đúng/chưa kiểm chứng. Chỉ mở/chọn mẫu/viết kịch bản thì hoàn thành đúng việc đó, không tự dựng video.
