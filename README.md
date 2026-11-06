# TeenCare Skills

Bộ 3 skill TeenCare để mang sang máy khác cài cho Codex. Giữ riêng tên gọi và toàn bộ nội dung gốc của từng skill; không gộp luồng Messenger với luồng đăng ký webinar.

| Skill | Công việc |
| --- | --- |
| `teencare-scriptwriter` | Kịch bản ads, hook, CTA; POV mẹ/bố/chuyên gia/narrator |
| `teencare-video-editor` | Brief, chọn source, dựng/sửa video TeenCare, bàn giao Drive/Sheet theo yêu cầu |
| `content-webinar-teencare` | Ảnh, kịch bản, caption và video webinar TeenCare |

Repo chứa 49 file gốc: SKILL.md, metadata giao diện, tài liệu sản phẩm, chân dung khách hàng, tone/mẫu POV, ảnh webinar/cô Giang/logo, thư viện mẫu text và 2 helper Python. `manifest.json` lưu SHA-256 để kiểm tra đủ và đúng file.

## Cài trên máy mới

Cần Git và Python 3.9 trở lên. Đăng nhập GitHub bằng tài khoản được cấp quyền vào repo private, rồi chạy trong PowerShell hoặc terminal:

```sh
git clone https://github.com/phuongdoan219/teencare-skills.git
cd teencare-skills
python install.py --check
python install.py
```

Mặc định cài vào `~/.codex/skills`, hoặc `CODEX_HOME/skills` nếu đã đặt biến `CODEX_HOME`. Windows có thể dùng `py` thay `python`. Đóng rồi mở lại Codex để nhận skill.

Nếu tải bằng **Code → Download ZIP**, giải nén, mở terminal trong thư mục chứa `install.py`, rồi chạy hai lệnh Python như trên; không cần Git.

Cài vào thư mục khác:

```powershell
python install.py --dest 'D:\Codex\skills'
```

Cập nhật sau này:

```sh
git pull --ff-only
python install.py --replace
```

`--replace` sao lưu nguyên thư mục skill hiện có sang `skill-backups/teencare-<thời điểm>/` cạnh thư mục `skills` trước khi thay. Không có `--replace`, bộ cài dừng nếu đã tồn tại bất kỳ skill nào trong bộ. Bộ cài không cài runtime, đăng nhập dịch vụ hay thay đổi cấu hình Codex khác.

## Gọi skill

Ví dụ trong Codex:

```text
$teencare-scriptwriter Viết kịch bản POV mẹ, concept phiên dịch, CTA Messenger.
$teencare-video-editor Lập brief dựng video từ kịch bản và nguồn tôi cung cấp.
$content-webinar-teencare Viết caption mời đăng ký webinar từ poster này.
```

## Chuẩn bị đường dẫn trên máy mới

Các skill được giữ nguyên byte theo bản gốc, nên tài liệu còn ghi đường dẫn của máy cũ (`E:/Teencare/`, `E:/HYPERFRAME/`, `C:/Users/Admin/…`). Đây không phải các file đã được chuyển sang máy mới.

Trước khi dựng video, điền đường dẫn thực vào [mẫu AGENTS.md](examples/AGENTS.machine.example.md), rồi đưa phần đó vào `AGENTS.md` của workspace/project đang làm. Giữ các hướng dẫn có sẵn của project. Codex đọc mapping này khi dùng skill; bộ cài không tự đổi đường dẫn trong tài liệu hay di chuyển footage.

- Source quay, voice, nhạc, SFX, khung app, project và cache video mẫu cần được chép/tải riêng nếu task sử dụng chúng. Repo không chứa những thư viện đó.
- Tài liệu sản phẩm, chân dung phụ huynh, tone và mẫu POV đã có trong `skills/teencare-scriptwriter/references/`. Khi viết webinar ngoài workspace cũ, dùng bộ tài liệu này; giữ offer/CTA của skill webinar. Tài liệu cập nhật do người dùng cung cấp ưu tiên hơn bản đóng gói.
- Link Google Drive/Sheets trong tài liệu vẫn giữ nguyên; tài khoản trên máy mới phải được cấp quyền và kết nối lại.
- Không đóng gói `AGENT_KNOWLEDGE.md`, thông tin đăng nhập, token hay cấu hình tài khoản.

## Phụ thuộc theo công việc

| Công việc | Chuẩn bị thêm |
| --- | --- |
| Viết kịch bản/caption | Codex và tài liệu đã kèm; không cần runtime video |
| Tạo/sửa ảnh webinar | Skill `imagegen` và quyền dùng công cụ tạo ảnh của Codex |
| Dựng/sửa video | Bộ skill HyperFrames đang dùng ở máy nguồn: `hyperframes`, `hyperframes-cli`, `media-use`, cùng domain mà router yêu cầu; Node.js/npm, HyperFrames CLI, FFmpeg/FFprobe theo hướng dẫn bộ đó |
| Hiệu ứng từ thư viện | `hyperframes-registry` khi task cần; `capcut-preset` và thư viện preset khi brief có mã preset |
| SFX dự phòng | `hyperframes-sfx-fallback` khi thực sự dùng nhánh này |
| Đọc brief Excel bằng helper | Python + `openpyxl>=3.1` (`python -m pip install -r requirements-helpers.txt`) |
| Đọc workbook/Drive/Sheets | Skill spreadsheet/Google Drive/Google Sheets phù hợp và connector đã kết nối trên máy mới |

Các skill phụ thuộc trên không nằm trong bộ 3 skill này. Sao chép/cài chúng từ bộ đang sử dụng; không giả định cài repo này là đã có môi trường render hoàn chỉnh. Khi cần ghi Google file, đọc thêm skill `google-workspace` nếu môi trường cung cấp.

Helper inventory hỗ trợ FFprobe trên PATH hoặc chỉ định trực tiếp:

```powershell
python skills/teencare-video-editor/scripts/inventory_sources.py 'D:\TeenCare\Source quay' --recursive --ffprobe 'D:\Tools\ffmpeg\bin\ffprobe.exe' --output inventory.json
```

Đọc `--help` của từng helper trước khi dùng. Inventory không thay cho xem/nghe footage.

## Kiểm tra và bảo quản

```sh
python install.py --check
```

Kiểm tra này xác nhận danh sách và hash của 49 file skill, không xác nhận tài khoản Drive, CLI hay footage đã sẵn sàng. Ngày chiến dịch, offer và các ví dụ trong tài liệu là dữ liệu của bản nguồn; kiểm tra lại theo brief mới.

Repo được tạo private vì chứa tài liệu và hình ảnh TeenCare dùng nội bộ. Không kèm giấy phép công khai để tái phân phối các nội dung này.
