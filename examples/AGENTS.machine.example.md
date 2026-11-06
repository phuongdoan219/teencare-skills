# Cấu hình TeenCare trên máy này

Mẫu cấu hình: thay các giá trị bên dưới bằng đường dẫn thật trước khi đưa vào AGENTS.md của workspace/project. Giữ nguyên các hướng dẫn khác đang có.

## Ánh xạ đường dẫn từ skill

| Đường dẫn trong tài liệu máy cũ | Đường dẫn thật trên máy này |
| --- | --- |
| `E:/Teencare/Source quay/` | `D:/TeenCare/Source quay/` |
| `E:/Teencare/KB Video Ads/` | `D:/TeenCare/KB Video Ads/` |
| `E:/Teencare/Video ads/` | `D:/TeenCare/Video ads/` |
| `E:/HYPERFRAME/` | `D:/HyperFrames/` |
| `E:/HYPERFRAME/hyperframes.cmd` | `D:/HyperFrames/hyperframes.cmd` |
| `E:/HYPERFRAME/tools/bin/ffprobe.exe` | `D:/Tools/ffmpeg/bin/ffprobe.exe` |
| `C:/Users/Admin/.codex/skills/` | Thư mục skills của tài khoản Codex hiện tại |

Các đường dẫn trong cột phải chỉ là ví dụ. Kiểm tra file thật trước khi chạy; nếu thiếu source hoặc runtime cần thiết thì nêu đúng phần thiếu, không tự coi file ví dụ là đã có.

Khi làm TeenCare, áp dụng mapping của project này cho đường dẫn máy cũ trong tài liệu skill. Dùng runtime/version theo project và router HyperFrames hiện có. Nếu CLI được cài trên PATH, ghi lệnh thật tại đây thay cho wrapper ví dụ.

## Tài liệu copy đã đóng gói

Nếu workspace không có bản sản phẩm/persona/POV mới hơn, lấy tài liệu trong skill `teencare-scriptwriter` đã cài:

- `references/product_info.md`
- `references/customer_persona.md`
- Tone và mẫu tương ứng trong `references/pov/`

Khi viết webinar, học dữ kiện/giọng từ các tài liệu trên và áp dụng offer/CTA/độ dài của `content-webinar-teencare`. Không thay CTA đăng ký webinar bằng Messenger từ skill scriptwriter.

Chỉ đọc `AGENT_KNOWLEDGE.md` khi người dùng yêu cầu dùng sổ tay. Repo skill không chứa sổ tay, footage, voice hay project video cũ.
