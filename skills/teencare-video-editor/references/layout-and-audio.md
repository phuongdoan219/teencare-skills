# Bố cục, chữ, app và âm thanh

## Hook và text

Chọn hình mở đầu đáp ứng câu đầu: giáo viên giới thiệu vấn đề; cảnh gia đình minh họa; một hành động của con; hoặc UI khi hook nói trực tiếp về app. Ô vàng là một cách nhấn, không phải bố cục mặc định. Không copy một khẩu hiệu/số liệu từ VPV106 sang kịch bản khác.

Nếu có reference, xem kích thước chữ, line break, viền/bóng, vị trí tương đối với mặt và nhịp xuất hiện. Tái tạo text/icon và chuyển động nhẹ bằng HyperFrames khi thiếu asset CapCut; dùng Registry/animation skill cho hiệu ứng cụ thể. Font phải hỗ trợ dấu tiếng Việt; Be Vietnam Pro đậm là một lựa chọn, không phải asset logo.

Theo phong cách đã chốt, ưu tiên Be Vietnam Pro ExtraBold/Black hoặc font tương đương có dấu đầy đủ, chữ trắng/vàng, viền/bóng tương phản và motion ngắn. Hook cần đọc được ngay khi vào cảnh; pop có overshoot nhẹ là một lựa chọn, không để hiệu ứng trì hoãn việc hiểu chủ đề. Kiểm tra dấu tiếng Việt và stroke trong lúc chữ nảy để tránh cắt glyph hoặc chạm mặt.

Text box dùng vàng (ví dụ `#ffc843`) với chữ đen hoặc theo mã trong [thư viện mẫu](text-library.md); ôm sát nội dung và giữ padding đủ đọc. Không đặt chiều rộng/chiều cao lớn cố định chỉ để chứa một dòng ngắn. Tại mỗi thời điểm chỉ có một box overlay, kể cả nhãn buổi sáng/trước/sau và caption khác lớp. Khi caption chính có box, câu phụ để chữ trần với màu, viền/bóng, size hoặc effect. Card/nút vốn có trong UI app không tính là text box overlay. Tránh dải kem chứa tiêu đề/branding nằm cố định dưới video; đặt chữ ở vùng trống gần trung tâm từng cảnh, tránh mặt và hành động.

Keyword và hook ưu tiên giữa video, vùng thân dưới mặt hoặc khoảng trống trung tâm; mép trên dễ xén khi lên ads. Chỉ đưa lên trên khi giữa che mặt, hành động/UI hoặc bố cục trên đẹp hơn. Chọn 2–3 mẫu text có mã cho một video, không mặc định mọi cue ở mép trên hay dùng cùng hiệu ứng.

### Hook trước/sau kèm chuyên gia

Hai source trước/sau có thể crop thành ô vuông bo góc, đặt cao và chạm biên ngang/trên nếu phù hợp. Xem hành động và mặt trong cả range; không để chuyên gia phủ lên hai ô. Đặt tiêu đề lớn ở vùng chuyển tiếp giữa hai cảnh và chuyên gia, căn giữa ngang. “Giữa màn hình” là một quyết định bố cục: chọn vùng nổi bật mà không che mặt, rồi cân lại các vùng hình để tiêu đề có chỗ.

Dùng chiều ngang hiệu quả trước khi tăng số dòng: thử hai dòng rộng, font đủ lớn, padding trên/dưới gọn. Không tạo một dải cao với chữ nhỏ nằm giữa và khoảng rỗng lớn hai bên. Loại khoảng trống trên hai ô, trên/dưới chữ và phía trên đầu chuyên gia do crop. Giữ khoảng thở cần thiết cho dấu, stroke, motion và chuyển động của đầu; không cắt tóc/mặt để xóa mọi pixel trống.

Khi chuyên gia là hình chính phía dưới, tăng diện tích hiển thị bằng cách thu các vùng rỗng, đẩy vùng hình lên và chỉnh `object-position` theo vị trí đầu/thân thật. Giữ nền gốc khi người dùng đã yêu cầu; không tự tách nền để giải quyết việc xếp lớp. Tọa độ, font size và tỷ lệ cuối VPV107 nằm trong [vpv107-example.md](vpv107-example.md), chỉ là một ví dụ cho canvas/source đó.

Mỗi cụm chữ phục vụ một ý của voice. Keyword có thể xuất hiện ở đầu ý và giữ tới hết ý. Khi cần hai số liệu cùng biến mất, tính `end = start + duration` của cue tham chiếu, đặt cùng end cho cue còn lại. Không kéo dài cả cụm qua frame sau chỉ để lấp chỗ trống. Bỏ bớt text/đổi bố cục khi UI hoặc thoại đã cung cấp đủ thông tin.

Không che mặt, tay đang minh họa hoặc con số trên laptop. Ảnh khóa học có thể hạ xuống dưới mặt, hoặc đặt sau nhân vật đã tách nền, theo yêu cầu. Chọn crop sau khi xem tất cả trạng thái zoom; kiểm tra trên kích thước điện thoại.

## Người thật và source online

Nếu có duet, chia đủ chiều ngang, crop phần trên/dưới phù hợp để bỏ khoảng trống mà vẫn giữ mặt. Tắt audio người nghe và dùng video họ đang chú ý. Chọn cảnh nghe sạch liên tục; cần tua chậm nhẹ thì xem toàn range, không lặp lại một đoạn họ nhìn giấy hoặc nói. Giữ chuyển động hai phía qua lượt thoại để tránh nhảy pose cùng lúc.

Khi tách nền giáo viên lên source laptop, xem bbox phần thân thực sự: alpha có thể còn padding dưới. Crop padding/đặt chân thân chạm đường chia hoặc mặt bàn, rồi đặt pivot zoom tại điểm tựa. Không kéo nhân vật lơ lửng ở giữa source. Zoom trên inner wrapper, timing clip để framework sở hữu theo core/keyframes.

Khi chuyên gia chèn lên cảnh gia đình/con, kích thước phải để hoạt động chính còn nhìn rõ. Thu nhỏ và đặt sát đáy nếu phù hợp; tính mép thân có alpha thực sự thay vì đáy của bounding box video. Viền trắng quanh silhouette có thể giúp tách nhân vật khỏi nền khi được yêu cầu; không vẽ stroke quanh cả hình chữ nhật. Xem đầu/giữa/cuối để kiểm tra mặt, tay và nội dung cảnh trám.

Kiểm tra rotation metadata trước crop. Footage điện thoại/laptop bị quay ngang phải đúng góc nhìn; chuyển HLG/BT.2020 về SDR có kiểm soát nếu dự án đích SDR, theo media-use. Giữ source gốc.

## App dễ đọc

Khung app TeenCare người dùng đã chọn trên máy: `E:/Teencare/Video ads/VPV106/khung app teencare AI.jpg`. Ưu tiên tái dùng cho cảnh app khi brief mới không chỉ định khung khác; kiểm tra file còn tồn tại và xem ảnh trước khi căn vùng hiển thị. Copy asset vào project đang dựng, giữ source gốc; không đóng gói ảnh này vào skill.

Quan sát source trước khi đặt khung: clip có thể đã bake bezel, tai thỏ, status bar, viền đen và ngón tay/cursor. Nếu background là khung app lớn, loại phần khung thừa và dùng vùng hiển thị cho chính báo cáo/tình huống. Không thu nhỏ cả điện thoại thêm lần nữa.

Crop đồng nhất theo source và giữ tỷ lệ UI; không kéo méo chữ/nút. Đặt title phía trên hoặc vùng riêng, ưu tiên diện tích báo cáo. Giữ video cuộn, lựa chọn và phản hồi thật; kiểm tra đầu/giữa/cuối để biết nội dung chính còn đọc được sau crop. Nếu background có ảnh cũ, cover/crop đúng vùng trước khi đưa app lên, giữ brand theo brief.

## Nhạc và SFX

Nhạc hơi nhanh, đều nhịp phù hợp ads phụ huynh khi brief muốn mood đó; dùng nhạc được cung cấp hoặc tìm theo media-use. Mở project đã duyệt thì giữ nền đang dùng, trừ khi yêu cầu đổi. Carve/duck/fade và automation qua hyperframes-audio; kiểm tra giọng trên cả đoạn nhạc dày, không chỉ giảm thanh volume theo mắt.

SFX nhấn một sự kiện: số liệu xuất hiện, ý mới, thao tác app, CTA. Một video khoảng một phút có thể bắt đầu với 4–6 điểm nếu chưa có chỉ định; đây là phương án thử, không hạn mức cứng. Dùng vài chất âm nhất quán và tránh âm mỗi caption/điểm cắt. Nếu đã có SFX, thống kê trước khi thêm; bỏ/thay điểm dư khi phù hợp để không chồng lớp.

Khi user chọn tiếng chụp ảnh, dùng shutter ngắn cho số liệu; tiếng thứ hai có thể nhỏ hơn. Pop/whoosh/click không tự thay nghĩa cho nhau. Khoảng 0,15–0,4 giây thường đủ cho click/shutter; whoosh chọn độ dài theo chuyển động. Level phụ thuộc file, không coi cùng `data-volume` là cùng độ to. Tiếng phải nghe được mà thoại vẫn rõ; giữ headroom và fade ngắn ở điểm cắt.

Trình tự tìm asset trên máy:

1. Asset project và `E:/HYPERFRAME/audio-library/sound_effects/`.
2. Bộ SFX của media-use; đọc manifest thực tế, không dựa vào số lượng asset được nhắc ở phiên bản khác.
3. Khi thiếu âm phù hợp, đọc `C:/Users/Admin/.codex/skills/hyperframes-sfx-fallback/SKILL.md` và tự tìm [MyInstants Việt Nam](https://www.myinstants.com/en/index/vn/) theo lựa chọn người dùng.

Lưu audio vào project, ghi URL trang nguồn/ngày lấy/quyền nếu có. Không đoán URL hay mặc định âm trên website được dùng thương mại. Nếu nguồn dự phòng không dùng được, tìm nguồn phù hợp khác theo skill fallback. Tái dùng file đã đúng chất âm; không cần tìm một file mới chỉ vì bắt đầu project mới.
