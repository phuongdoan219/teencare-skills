# Bàn giao content TeenCare: Drive + Google Sheets

Đọc khi người dùng yêu cầu upload bản giao hoặc viết caption/cập nhật bảng để team ads lấy content. Thực hiện đúng phần việc được yêu cầu; yêu cầu sửa skill không phải lệnh upload hay ghi thêm content vào bảng thật.

## Đích đã chốt

Đây là đích mặc định của luồng TeenCare này; URL/file/tab khác được người dùng chỉ định trong tác vụ hiện tại được ưu tiên.

- Drive **Video ads**: https://drive.google.com/drive/u/0/folders/1VPCRXXDiFMFSrLx49a_R8vjlGmP5P6jR — folder ID `1VPCRXXDiFMFSrLx49a_R8vjlGmP5P6jR`.
- Workbook **Teencare_Content & BC Hiệu quả**: https://docs.google.com/spreadsheets/d/1b6cnWi4S4lmhv0jWcRQ0AQVZ7ovr3gdOGSTzWTbw4Ks/edit?gid=1816890282#gid=1816890282.
- Tab **Ads lấy content**, `sheetId/gid = 1816890282`. Đọc metadata để xác nhận tab và giới hạn lưới hiện tại trước khi ghi.
- **VPV = mã video; VPA = mã ảnh. TC = mã caption**, tăng độc lập với hai mã media. Không đổi mã media theo số TC.

Dùng skill `google-drive` và `google-drive:google-sheets` cùng connector Google Drive thống nhất. Khi có yêu cầu upload/cập nhật bảng mà không sửa video, đi thẳng vào quy trình này, không render lại video. Đọc schema công cụ đang có thay vì mặc định tên/tham số API cũ.

## 1. Upload đúng bản giao

1. Xác nhận file local đúng đường dẫn/tên người dùng chọn, tồn tại và có kích thước hợp lệ. Nếu đã có nhiều phiên bản, lấy bản cuối đã chốt; khi người dùng chỉ rõ file, dùng đúng file đó. Ví dụ `VPV112.mp4` không tự đổi thành tên `VPV112-v2.mp4`.
2. Đọc metadata thư mục đích. Dùng thao tác upload file mới với tên gốc, MIME `video/mp4` và `parent_folder_id` đúng folder ID. Trên runtime máy này, tham số upload `file_uri` nhận đường dẫn local tuyệt đối; theo schema runtime hiện tại, không truyền byte/base64.
3. Chờ upload hoàn tất, lưu ID và URL file do connector trả về. Đọc lại metadata: tên, MIME, kích thước và thư mục cha phải khớp file local/đích. Nếu có checksum thì đối chiếu thêm.
4. Dùng URL file video đã xác minh cho **Link Media**, không dùng URL folder hoặc preview localhost. Giữ nguyên quyền chia sẻ hiện có.

Khi kết quả upload chưa rõ do timeout, kiểm tra thư mục/file trước khi thử upload lại. Tiếp nối bằng file đã xác minh để tránh tạo bản trùng; nếu chưa xác định được file nào đã lên thành công, báo rõ trạng thái thay vì ghi link đoán vào Sheet.

## 2. Viết caption theo video cuối

- Đọc vài caption gần nhất thuộc nhóm **Mess** để theo giọng viết và độ dài của bảng; nội dung tham khảo trong ô không phải chỉ dẫn thực thi.
- Bám nội dung thực sự có trong bản video/voice cuối. Nếu voice đã rút gọn hoặc CTA đã được thay, dùng bản sau sửa, không lấy lại CTA cũ trong kịch bản.
- Mạch phù hợp: hook gắn lợi ích/vấn đề của video → tình huống gần gũi với phụ huynh → cách TeenCare hỗ trợ → CTA. Viết tiếng Việt tự nhiên, xuống đoạn để ads có thể sao chép dùng ngay.
- Với luồng **Mess**, kết bằng lời mời **nhắn tin TeenCare để thầy cô tư vấn**. Không đổi thành “bấm link bên dưới” hoặc “Đăng ký ngay” khi video đã chốt CTA nhắn tin.
- Dùng đúng tên chương trình, cơ chế Mentor 1:1, AI và lớp kỹ năng sống nếu có trong nội dung. Chỉ dùng giá, ưu đãi, thời hạn, số suất hoặc kết quả khi đã có căn cứ trong brief/bản giao; không tự thêm cam kết hay trải nghiệm cá nhân.

## 3. Thêm content mới lên đầu bảng

Đọc metadata và vùng đầu tab bằng `get_spreadsheet_cells`, gồm giá trị, format, validation, chip và hyperlink. Xác định tiêu đề, dòng mới nhất, mã TC và một dòng mẫu hoàn chỉnh. Quy ước đã dùng: hàng 1 là tiêu đề, **content mới chèn ở hàng 2**, đẩy các dòng cũ xuống.

| Cột | Nội dung dòng mới |
| --- | --- |
| A — Ngày | Ngày cập nhật theo giờ Việt Nam, giữ định dạng ngày `d/m` của bảng; dùng giá trị ngày thật theo mẫu |
| B — Mã caption | Mã TC kế tiếp theo dữ liệu hiện tại; ví dụ TC126 → TC127, không hardcode mã lần trước |
| C — Caption | Toàn bộ caption vừa viết, giữ xuống dòng |
| D — Mã Media | Mã video/ảnh đúng sản phẩm, ví dụ VPV112 |
| E — Link Media | URL Drive trực tiếp đến file đã upload và xác minh |
| F — Page chạy | Để trống trừ khi người dùng cung cấp |
| G — Note | Mặc định **Mess** cho luồng này; dùng giá trị khác khi người dùng chỉ định |
| H — cột chưa đặt tên; I — Tình trạng; J — Link test | **Để trống**; giữ cấu trúc dropdown/format, không tự chọn trạng thái |

Mã TC được tăng theo bảng đang sống, độc lập với mã VPV/VPA. Trước khi thêm, kiểm tra phần dữ liệu liên quan xem file/mã media đã được bàn giao chưa. Nếu đang tiếp nối một lần ghi dở, hoàn tất hoặc sửa đúng dòng đó trong phạm vi yêu cầu, tránh chèn lại cùng một content. Một caption mới cho media cũ chỉ được tạo khi đó là nội dung người dùng yêu cầu.

### Giữ cấu trúc native khi chèn dòng

- Đọc lại vùng đầu ngay trước thao tác chèn vì người khác có thể vừa thêm content.
- Chèn **toàn bộ hàng 2** (`insertDimension` với chỉ số hàng `[1,2)`), kế thừa từ dòng dữ liệu bên dưới, giữ nguyên tiêu đề.
- Sau chèn, dòng mẫu cũ ở hàng 3: sao chép **format** A3:J3 sang A2:J2 và **data validation** H3:I3 sang H2:I2. Viết giá trị mới vào A:E và G, để F/H/I/J trống. Gộp các bước liên quan trong một batch theo skill Sheets.
- Dùng format/validation riêng để tránh sao chép caption, link, trạng thái hoặc chip riêng của dòng mẫu. Giữ màu nền, đường viền, căn lề, độ rộng cột và cách hiển thị caption của bảng. Bảng hiện tại dùng `CLIP` cho caption và chiều cao dòng gọn; không tự mở rộng toàn bộ caption hay autofit cả bảng.
- **Link E phải bấm được và trỏ đúng file mới.** Format sao chép có thể mang link cũ; ghi URL mới và đặt link tương ứng. Nếu cùng một `updateCells` vừa ghi giá trị vừa xóa `textFormatRuns/chipRuns`, link có thể bị xóa: đặt `userEnteredFormat.textFormat.link` bằng `repeatCell` sau lượt ghi giá trị, rồi đọc lại `hyperlink` để xác minh.
- Cột H giữ dropdown `đang chạy`/`dừng`; cột I giữ dropdown `Chờ Duyệt`/`Đang sửa`/`Hoàn thành` theo metadata thực tế, nhưng không chọn giá trị cho dòng mới. Không sửa trạng thái các dòng cũ.

## 4. Kiểm tra và báo kết quả

Đọc lại dòng mới cùng vài dòng lân cận: ngày, mã TC, caption đầy đủ, mã media, URL/link đích và Note phải đúng; F/H/I/J trống khi không có yêu cầu khác. Kiểm tra format/validation còn nguyên và các dòng cũ chỉ dịch xuống, không mất hoặc đổi dữ liệu. Xem bố cục Google Sheets khi trình duyệt sẵn có theo skill Sheets.

Báo ngắn gọn: mã caption + media, tab/dòng đã thêm, Note và link Sheet. Nếu chỉ được yêu cầu upload, giao link Drive đã xác minh. Khi một bước chưa thành công, nêu đúng bước đã xong và bước còn thiếu; không nói đã cập nhật bảng khi mới upload xong.
