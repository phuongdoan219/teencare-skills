# Sửa theo feedback và giao bản

## Xác định đúng đoạn

Khi người dùng nói timestamp hoặc frame, dùng timeline HyperFrames để xác định clip/file đang sở hữu. Ở PowerShell trên máy này:

```powershell
& 'E:/HYPERFRAME/hyperframes.cmd' timeline --json
```

Đọc composition liên quan; dùng history theo CLI để giữ các chỉnh sửa người dùng. Frame gốc là ID góp ý, khác số frame mã hóa. Sau xóa/tăng tốc, không dùng timestamp bản cũ để đặt caption/SFX bản mới.

Góp ý cụ thể thì sửa trực tiếp trong phạm vi. Câu hỏi/ý tưởng chưa chỉ định thay đổi thì trả lời bằng đề xuất ngắn. Người dùng đã yêu cầu dựng/xuất: không hỏi lại để duyệt các lựa chọn triển khai thông thường. Giữ các điểm đã chốt, sửa tài liệu mô tả hiện trạng để lần tiếp theo không trở lại lựa chọn cũ.

Khi feedback mới đến trong lúc render, áp dụng vào project đang sửa và phân biệt file đang xuất từ bố cục cũ với bản giao cuối. Kiểm tra/xuất lại phần cần thay đổi hoặc toàn video; chỉ giao phiên bản phản ánh góp ý mới nhất. Ghi rõ trạng thái cuối trong tài liệu project, không để hướng dẫn vẫn mô tả tọa độ/bố cục đã bị thay.

## Kiểm tra đủ, tránh render thừa

- Sau HTML: full check theo AGENTS/CLI. Review warnings và sửa errors, không coi `0/0` samples là kết quả kiểm tra hình nếu lint đã chặn browser.
- Chữ: frame trước/sau onset/end; crop mặt: các mức zoom; app: đầu/giữa/cuối; điểm nối bị giật: đoạn chuyển động cả hai bên. Một ảnh không đủ để kết luận hết giật.
- Hook có nhiều vùng: xem đầu/giữa/cuối và lúc pop lớn nhất; rà khoảng trống trên hai ô, quanh tiêu đề, trên đầu chuyên gia. Chữ đọc ngay, không che mặt/cử chỉ, không cắt dấu hoặc tóc; vùng chuyên gia chiếm đủ diện tích sau khi thu padding.
- Box: kiểm tra các khoảng hiển thị chồng nhau trên toàn scene, kể cả nhãn có nền và các lớp từ sub-composition; tối đa một text box overlay cùng lúc. Box vàng/chữ đen ôm nội dung, câu phụ không có box.
- Thoại: câu/range thật, đồng bộ miệng, silence ngoài chủ ý, nhạc/SFX ở mốc dày. Đo peak/voice correlation là bằng chứng hỗ trợ; không thay việc nghe khi cần kết luận về chất âm hoặc từ bị cắt.
- File giao: duration/FPS/kích thước/codec, đủ hình/tiếng, không frame đen/freeze ngoài chủ ý, chữ đọc được và tiếng không clipping. Kiểm tra đoạn bị sửa từ MP4 thực tế.
- Khi có trần thời lượng, so duration MP4 với trần đã chốt (VPV107: ≤70 giây), không chỉ nhìn tổng duration voice hoặc số trên preview. Kiểm tra hình người nói và cue theo voice đã tăng tốc.

Chạy checks phù hợp một lượt sau thay đổi cuối; chỉ mở rộng/chạy lại khi còn lỗi hoặc có sửa mới. Mốc trước/sau boundary ưu tiên frame nguyên theo FPS đích.

## Xuất nhanh khi chỉ sửa một phần

Ưu tiên cách đơn giản đủ chắc chắn. Render toàn bộ là hợp lệ; không phát minh tối ưu phức tạp cho một sửa nhỏ.

- **Chỉ tiếng đổi:** mix qua cùng HyperFrames audio graph/automation của project. Có thể render composition audio trên canvas nhỏ rồi chép luồng audio vào MP4 đã duyệt. Không dùng bản mix FFmpeg bỏ qua carve/FX mà preview đang dùng. Nếu chép luồng hình, xác minh hash payload hình không đổi và duration/FPS vẫn đúng.
- **Chỉ hình ở vài cảnh đổi:** cân nhắc render đoạn thay đổi với mốc frame rõ ràng; giữ local timeline của sub-composition. Ghép với đầu/cuối đã duyệt và giữ audio đã kiểm tra khi tiếng không đổi. Xác minh số frame đoạn, số frame cuối và nội dung ở hai điểm nối.
- Nếu thay đổi timing/rate hoặc thoại, tính lại cả timeline và audio liên quan; không tái dùng tiếng cũ chỉ vì tên file giống nhau.

Helper/staging phải có asset thực sự đọc được. Bundler warning hoặc symlink/junction không phải bằng chứng render đã đủ nội dung; kiểm tra pixel và các file phụ thuộc. Các cách ghép này là lựa chọn triển khai, không phải yêu cầu phải dùng trong mọi project.

## Preview và giao file

```powershell
& 'E:/HYPERFRAME/hyperframes.cmd' preview --background
& 'E:/HYPERFRAME/hyperframes.cmd' preview --status --json
```

Xác nhận server sẵn sàng/URL trả HTTP 200, dùng URL có `#project/<project-name>` và giữ server sống trong lúc xem. Mở preview trước bản xuất khi hữu ích, không để tác vụ nền tạm của terminal làm mất preview.

Render/check theo skill CLI và AGENTS của project. Ghi version bản giao, duration và thay đổi chính; giữ bản trước. Copy MP4 cuối vào folder người dùng chọn và xác nhận file đích tồn tại/đúng kích thước. Chỉ giao MP4 cuối, không nhầm helper audio canvas nhỏ với video hoàn chỉnh.

Nếu được yêu cầu upload Drive hoặc cập nhật content cho team ads, tiếp tục theo [drive-and-content-sheet.md](drive-and-content-sheet.md), dùng đúng bản giao cuối và CTA đã chốt.

Không đóng gói source diễn viên, voice riêng, clip gia đình hay nhạc dự án vào skill tái dùng. Những file đó ở project nguồn; skill giữ quy trình và ví dụ, không thu gom thư viện footage riêng của người dùng.
