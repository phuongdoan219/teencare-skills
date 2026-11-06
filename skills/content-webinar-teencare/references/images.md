# Làm ảnh webinar và profile

## Asset

- `../assets/teencare-logo.png`: logo nguồn; xem trước khi dùng.
- `../assets/giang-identity-reference.png`: card chân dung nguồn ban đầu. Dùng nhận diện mặt/tóc/trang phục; chữ cũ không phải nguồn claim.
- `../assets/webinar-poster-approved.png`: poster cam–kem sau sửa giờ, độ tuổi, quyền lợi, profile, slogan, da mặt.
- `../assets/giang-profile-square.png`: profile vuông hai cột.

Ảnh chân dung thật chất lượng cao user cung cấp về sau được ưu tiên. Card nguồn có graphic/chữ: không mang chúng vào da mặt/ảnh mới. Không lấy mặt qua nhiều lần tạo làm chuẩn duy nhất rồi trôi nhận diện.

## Nhận diện

Cam chủ đạo, nền kem/ivory, chữ đen/charcoal. Tham khảo `#FF8500`, `#FFF7E8`, `#171717` là xấp xỉ theo ảnh, không phải mã brand công bố. Brand kit mới ưu tiên.

Chữ có dấu, rõ trên điện thoại, hierarchy headline → diễn giả/offer → thông tin. Nền ấm sạch, hạn chế neon/texture hạt. Mặt cô Giang sáng mịn tự nhiên; bỏ gạch/viền vẽ, nhám và grain trên da; giữ hình mặt, mắt/mũi/miệng, nụ cười, tóc, tuổi và tỷ lệ. Không thay bằng người tương tự.

## Poster webinar

Khi clone mẫu, xem ảnh rồi giữ phân vùng/hierarchy, thay đúng content. Mẫu là screenshot Facebook thì mặc định tạo **poster bên trong**, bỏ header/page/reaction/khung feed.

Template đã chốt: logo nhỏ phía trên; tên webinar lớn; giờ/nền tảng/độ tuổi bên trái; chân dung/profile cô Giang bên phải; tư vấn 1:1 nổi bật; CTA. Hai ghế/micro thuộc template này, không bắt buộc mọi ảnh. Chỉ cô Giang nếu brief không thêm diễn giả.

Giữ dữ kiện brief: 19h30–21h00, 8–18 tuổi, Google Meet, WEBINAR MIỄN PHÍ, TƯ VẤN 1:1 MIỄN PHÍ. Không đưa lại thứ/ngày hoặc slogan đã bỏ. Canvas theo brief/kênh; mẫu cũ dọc 4:5 chỉ dùng khi phù hợp. Không tự thêm nhiều biến thể.

## Ảnh vuông chỉ cô Giang + profile

Canvas 1:1. Chân dung trái, tên/vai trò và dấu ấn chuyên môn phải. Cam–kem–đen, check cam, dễ đọc. Chỉ hình cô + profile: bỏ tên webinar, giờ, CTA, offer, ghế/micro và logo rời nếu không yêu cầu. “Hiệu trưởng TeenCare” thuộc profile nên giữ.

## Thực hiện/sửa

1. Dùng skill `imagegen` và công cụ tạo/sửa ảnh tích hợp. Đọc local bằng `view_image` trước khi sửa; không dùng HTML/SVG thay raster.
2. Prompt gắn rõ vai trò từng ảnh: đích, bố cục, màu/logo, nhận diện. Ghi chữ nguyên văn có dấu và yếu tố cần giữ/phần sửa.
3. Sửa theo feedback: đổi màu giữ chữ/bố cục; sửa mặt giữ mọi chữ; bỏ slogan phục hồi nền, giữ CTA. “Bỏ viền ở mặt” không phải bỏ viền card.
4. Xem kết quả: đúng người, da sạch, không méo mặt/tay, đủ profile, đúng dấu, không thêm claim/ngày/diễn giả, chữ đọc được trên điện thoại.
5. Lưu PNG + prompt trong workspace, có phiên bản, giữ nguồn/bản duyệt. Dùng path Windows thật `C:/...` hoặc `E:/...`, không truyền `/C:/...` cho công cụ đọc file.
