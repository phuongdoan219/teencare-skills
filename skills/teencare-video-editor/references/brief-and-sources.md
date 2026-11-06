# Brief bảng, source và voice

## Biến bảng thành kế hoạch dựng

Nhận cả prompt bảng Markdown, Excel và ghi chú bổ sung trong chat. Các cột hữu ích: `Frame/STT`, `Thoại`, `Text màn hình`, `Thể hiện`, `Nguồn`, `Note`, `Thời lượng`. Đây là schema gợi ý; ánh xạ tên/cấu trúc thực tế, không yêu cầu người dùng đổi file đã đủ rõ.

### Điền brief Google Sheets theo mẫu KB2

Mẫu người dùng: [Brief AI edit – KB 2](https://docs.google.com/spreadsheets/d/1KvLDUpJuw88E_OsuAOmmEQk_dGFOQpOwN0PsGXOkVMg/edit?gid=762748921#gid=762748921). Dùng mẫu để học cách note, không sao chép nguyên bố cục hay source của từng frame sang kịch bản khác.

Trong workbook này, tên tab thực tế là `KB 2` và `KB 3`. Schema: A `Frame`, B `Thoại`, C `Text hiện trên màn hình`, D `Mô tả phân cảnh`, E `Nguồn`. Khi làm workbook khác, đọc header và metadata để ánh xạ lại. Đọc mẫu và thoại trước; chỉ sửa tab/cột được người dùng yêu cầu, giữ frame, thoại, header và định dạng còn lại. Dùng connector Google Sheets để đọc/sửa file hiện có; không tạo bản sao hoặc dựng video nếu chỉ được yêu cầu điền bảng.

- **C – Text hiện trên màn hình:** chữ ngắn nhấn ý, không chép nguyên câu thoại. Các cụm lần lượt theo voice có thể xuống dòng trong cùng ô. KB2 có những cảnh không cần thêm text; không tự ép mọi cảnh thành một caption box.
- **D – Mô tả phân cảnh:** viết trực tiếp hình gì xuất hiện, nhân vật làm gì, bố cục trong frame và loại source dùng minh họa. Ví dụ: “Chuyên gia source gốc full màn hình”, “Con ngồi học trước laptop”, “Duet cô ở trên, con ở dưới”, “App chiếm phần lớn frame”, “Freeze phần đầu landingpage và crop tên lớp”. Nếu có hình chính + ô vuông/PiP, nói rõ vai trò và vị trí tương đối; text/ảnh tránh mặt, tay và UI quan trọng. Ghi các nhịp cắt trong một frame khi cần, không biến cột D thành hướng dẫn kỹ thuật dài.
- **E – Nguồn:** dùng đường dẫn Windows tuyệt đối tới **file thật**, đặt trong dấu ngoặc kép như Windows “Copy as path”, giữ đúng dấu, khoảng trắng và phần mở rộng. Nhiều nguồn xuống dòng, có thể gắn nhãn `Source chuyên gia:`, `Cảnh trám:`, `App:` hoặc `Duet:`. Timecode đã kiểm tra có thể ghi trước path, ví dụ `1p31–1p39: "E:\...\Đã sửa .mov"`. Không ghi lời mô tả thay path, tên file đoán, hoặc thư mục chung khi đã chọn được file cụ thể. Đường dẫn trong KB2 có thể đã cũ: kiểm tra tồn tại trước khi dùng lại.

Trước khi ghi, đối chiếu metadata/validation và đọc lại vùng đích; dùng cập nhật giá trị ở đúng C:D:E, không viết lại A:B. Sau ghi, đọc lại nội dung và kiểm tra bảng native có xuống dòng, không bị cắt chữ. Khi chỉ chọn nguồn hình, không nói đã nghe/khớp toàn bộ thoại; việc chọn take, in/out voice vẫn cần nghe đối chiếu khi dựng.

### Nguồn và nhịp dựng cho video chuyên gia

- **Mở đầu:** chuyên gia source gốc là hình chính, ưu tiên giữ nền quay. Có thể chèn một ô vuông ảnh/video minh họa ở vùng trống; không thay hook bằng cảnh trám full màn hình nếu brief không yêu cầu. Sau phần chuyên gia dẫn vấn đề, tăng dần cảnh trám theo nội dung; cuối CTA có thể quay lại chuyên gia. Voice chuyên gia tiếp tục chạy dưới cảnh trám.
- **Cảnh trám diễn viên:** chọn tối đa 3 folder diễn viên khác nhau dưới `E:\Teencare\Source quay` cho cả kịch bản; các subfolder của cùng một diễn viên vẫn là một nhóm. Ưu tiên quay lại cùng gia đình ở các cảnh sinh hoạt/học/vận động. App, Duet và source chuyên gia là nhóm nguồn theo chức năng; vẫn cân nhắc số gương mặt để tránh rối.
- **App:** `E:\Teencare\Source quay\Source app Tinke`. Chọn màn hình khớp câu: `nhận xét sau buổi.mov` cho báo cáo Mentor; `tình huống vs con.mov` cho tình huống và gợi ý ứng xử; `xếp lịch học.mov` cho lịch; `mo hinh hanh vi.mp4` có phần demo/slide mô hình, cần crop bỏ người thuyết trình/viền khi dùng làm hình minh họa. Xem UI thật, không tự tạo chức năng hay kết quả mà source không có.
- **Duet:** `E:\Teencare\Source quay\Duet\Cô và con.mp4` và `Cô và mẹ.mp4` cho hai kiểu tương tác online. Khi lên video dọc, crop hai nửa và xếp trên/dưới hoặc bố cục phù hợp; giữ đúng người nói/người nghe đang chuyển động, crop phần UI/phụ đề cũ nếu vướng nội dung.
- **Landingpage:** ưu tiên source mới `E:\Teencare\Source quay\Landingpage.MP4`. Freeze phần đầu đã kiểm tra và crop tên lớp/thông tin giới thiệu, bỏ thanh trình duyệt/điều hướng nếu có. Source cũ `E:\Teencare\Video ads\IMG_2201.MP4` chỉ dùng khi brief chọn lại. Không dùng đoạn form đăng ký hoặc thông tin điền thử ở cuối video để thay hình giới thiệu lớp.

Ví dụ đã đối chiếu cho KB3 ngày 13/10/2026 (không phải source cố định cho mọi brief): chuyên gia `E:\Teencare\Source quay\Thay giao T10.26\C8143.MP4` và `C8144.MP4`; cảnh trám thuộc Mommy 4.0 và Nhung Nguyen. Mommy 4.0 `TeenCare\Đã sửa .mov` có cảnh con vận động trước laptop ở 1p31–1p39. Nhung Nguyen `TeenCera❤️\IMG_2612.MOV` có cảnh kết thúc học, đóng laptop và sắp sách; `IMG_2361.MOV` có con ghi chép khi học; `IMG_2550.MOV` có con ngồi dùng điện thoại. Dùng ví dụ như chỉ mục tìm lại, vẫn kiểm tra take/range cần dùng. C8144 là take bổ sung cần nghe để xác định câu phù hợp, không mặc định là CTA chỉ vì file ngắn.

Giữ row/frame gốc để người dùng tiếp tục nói “frame 5”. Phân biệt header với dòng thoại, giữ xuống dòng, từ bôi đậm, link và note được merge. Không mặc định mọi brief có 13 frame hay thoại luôn ở B1:B13. Một vùng merge có nội dung ở ô đầu; không nhân đôi nó thành nhiều câu đọc.

Helper chỉ đọc workbook, không tính lại công thức:

```powershell
& '<python-runtime>' '<skill-dir>/scripts/extract_brief.py' '<brief.xlsx>' --output '<project>/brief-extracted.json'
```

Có thể thêm `--sheet '<tên sheet>'` và `--range 'A1:G30'`. Output ghi tọa độ ô, text/runs/bold, hyperlink, merges và cached value nếu có công thức. Khi cached value thiếu, tìm câu gốc hoặc hỏi phần thiếu; không coi công thức là lời đọc. Workbook định dạng quá rộng: chọn sheet/range thực tế thay vì xuất hàng triệu ô rỗng.

Lập `edit-manifest.json` hoặc bảng tương đương, gồm:

- ID/frame gốc, câu thoại, nguồn tiếng và source in/out; nhiều range khi ghép đúng một lần đọc.
- Source hình, in/out hình, muted/giữ tiếng thật, playback rate, thời điểm lên hình và duration cuối.
- Cue text: nội dung, lúc xuất hiện/kết thúc và vị trí; cue SFX nếu có.
- Thao tác loại frame và tổng thời lượng sau chỉnh. Bảng/brief gốc giữ nguyên.

Thời gian nguồn và thời gian trên video là hai hệ khác nhau. Ưu tiên mốc frame nguyên ở FPS đích cho điểm nối; tính lại timeline sau cắt/rate, rồi cập nhật hướng dẫn/storyboard liên quan.

## Kiểm kê và tìm phân cảnh

```powershell
& '<python-runtime>' '<skill-dir>/scripts/inventory_sources.py' '<folder chính>' '<folder cảnh trám>' --recursive --output '<project>/source-inventory.json'
```

Helper nhận nhiều folder/file, chỉ đọc và không ghi đè output đã có. FFprobe lấy từ `--ffprobe`, môi trường hoặc bộ tools trên máy. Inventory cho biết kỹ thuật; mô tả hành động cần xem source thật.

Với “tự tìm”: lấy contact sheet đầu/giữa/cuối hoặc theo thay đổi cảnh, chọn candidate rồi xem đoạn chuyển động. Ghi diễn viên, hành động, range sạch, chữ/logo đã bake, có âm nhạc/voice và orientation. Từ video đã edit, lấy range đủ dài cho câu, tránh transition dở dang và cảnh có nhãn khác sản phẩm. “Hết hạn SDHA” trong tên file là note cần giữ/đối chiếu phạm vi dùng, không tự suy đoán tình trạng khác với thông tin người dùng cung cấp.

Đối chiếu động từ của câu với hành động đang thấy: “tự giác làm việc nhà/dọn bàn học” cần cảnh con đang quét nhà, dọn bàn hoặc sắp sách; không chọn một cảnh chỉ vì có con/bàn học trong đó. Ghi source in/out và hành động đã xác minh để lần sửa sau không quay lại đoạn sai.

## Cắt lời chính xác

Transcribe source liên quan, đối chiếu câu và nghe đoạn quanh đầu/cuối. Tìm retake đọc trọn, đúng nội dung, người nói hướng camera; bỏ đọc nhầm, nhắc đạo diễn, nhìn giấy/làm việc riêng và khoảng chờ không phục vụ video. ASR chỉ hỗ trợ tìm range, không phải bằng chứng câu đã đúng.

Nếu cách nói khác nhẹ bản viết, giữ lời ghi âm tự nhiên và ghi khác biệt khi cần. Nếu thiếu hẳn câu, tìm retake/nguồn khác hoặc hỏi; không ghép âm tiết thành phát ngôn mới. Nhạc/tiếng đã bake trong cảnh trám cần tắt khi đặt dưới voice chính, trừ khi brief muốn nghe tiếng tại cảnh đó.

Tăng tốc pitch-preserved khi cần, video người nói tăng tương ứng. Khoảng thoại liên tục không được rơi vào silence ngoài chủ ý; kiểm tra chỗ ghép và các đoạn bị cắt/rút thời lượng. Giới hạn thời lượng từ brief: bỏ các frame người dùng chỉ định rồi tính lại, không đơn thuần tăng tốc đến mức khó nghe.

Nếu yêu cầu tăng voice toàn video, áp dụng nhất quán cho mọi đoạn thoại, rồi tính lại duration, mốc cảnh, caption và SFX theo FPS đích. Rate khoảng 1,22× đã đưa VPV107 xuống 68,967 giây dưới trần 70 giây; đây là kết quả của các range đã cắt, không phải rate áp sẵn cho mọi project. Đo duration MP4 cuối sau làm tròn frame và phần giữ hình/âm thanh cuối.

## Mã text/icon và source landingpage mới

Cột C giữ keyword; cột D hoặc Note ghi mã từ [text-library.md](text-library.md), motion và vị trí. Ví dụ: `Text TC-T05; pop ngắn; giữa thân dưới mặt; Icon TC-I01 khoanh “3 KHÔNG”`. Cột E giữ path thật. Mỗi video chọn 2–3 mẫu chữ, không chép giá/claim trong ảnh reference.

Source landingpage mới người dùng chỉ định: `E:\Teencare\Source quay\Landingpage.MP4`. Ưu tiên phần đầu giới thiệu “Lớp học Tâm lý & Kỹ năng sống… cùng TeenCare”, crop thanh trình duyệt; không dùng form. Source `IMG_2201.MP4` là ví dụ cũ, không tự dùng lại khi brief đã chỉ định Landingpage.MP4.
