# 🌌 Fast-Purple Triggerbot (Python Interception Fork)

**The fastest and most stable Python-based triggerbot fork.**  
Optimized for dynamic resolution, burst delay, and extremely low reaction times.

---

## 🚀 About This Fork
This fork is an enhanced version of the original Fast Valorant Triggerbot with:

- ✅ Interception Python (low-latency key injection)  
- ✅ Auto-resolution / DPI awareness  
- ✅ TAB toggle system  
- ✅ Burst-delay support  
- ✅ Safer threading & cooldown feedback  
- ✅ Optimized color scanning  
- ✅ Configurable delays & tolerance  
- ✅ K key (scancode) as secondary fire  

Reaction times are **typically 2–10ms**, depending on your refresh rate.

---

## 🎯 How It Works
The bot scans a small **center screen zone (10x10 px)** for enemies with purple outline:


RGB = (250, 100, 250)
It sends a keypress (K scancode) when a match is detected.
You can adjust RGB and tolerance in the config.json.

⚙ Setup
1️⃣ Requirements
Install Python dependencies:

bash
Copy code
py -m pip install interception numpy mss keyboard pywin32
(Ensure interception.dll is installed on your system)

2️⃣ Valorant Settings
Use Purple Outline

Add K as secondary shoot key

Optional: Disable RawInput to avoid conflicts

3️⃣ Config File (config.json)
json
Copy code
{
    "trigger_hotkey": "0xA0",
    "base_delay": 0.01,
    "trigger_delay": 40,
    "color_tolerance": 70,
    "always_enabled": false,
    "burst_delay": 0.05
}
Key Explanation:

Key	Function
trigger_hotkey	VirtualKey code when not always enabled
base_delay	Minimum delay between shots
trigger_delay	Extra percentage delay on top
color_tolerance	RGB detection tolerance
always_enabled	If true, triggerbot is always on
burst_delay	Delay between shots in a burst

🎮 Controls
Key	Function
TAB	Toggle triggerbot on/off
Ctrl + Shift + X	Emergency exit

Sound feedback included.

🖥 Resolution Support
Works on 720p, 1080p, 1440p, 4K

Works with stretched resolutions

DPI / scaling independent

Auto-updates when alt-tabbing

⚡ Performance Notes
Reaction time: 2–10ms (depends on monitor refresh rate)

Optional improvements:

GPU capture (DXCAM)

Native rewrite (C++ / Rust)

Thread pinning / CPU affinity

🔒 Safety
Interception is low-risk, no memory reading/writing

Pixel detection is the safest type of automation

Use at your own risk

📦 Compilation
Compile using Nuitka for better performance:

bash
Copy code
py -m nuitka --onefile triggerbot.py
📝 Why This Fork?
Original: fast but hardcoded, unstable

Fork: auto-resolution, burst delay, toggle system, safer & cleaner

⚡ License
Use responsibly. This fork is provided as-is.

# 🌌 Fast-Purple Triggerbot (Python Interception Fork)

**Triggerbot nhanh nhất và ổn định nhất bằng Python.**  
Tối ưu cho độ phân giải linh hoạt, hỗ trợ burst delay, và phản ứng cực nhanh.

---

## 🚀 Giới thiệu
Fork này là phiên bản nâng cấp của Fast Valorant Triggerbot gốc, với:

- ✅ Sử dụng Interception Python (nhấn phím cực nhanh, thấp độ trễ)  
- ✅ Tự động nhận độ phân giải / DPI awareness  
- ✅ Hệ thống toggle bằng **TAB**  
- ✅ Hỗ trợ **burst-delay**  
- ✅ Threading an toàn và phản hồi bằng âm thanh  
- ✅ Quét màu tối ưu  
- ✅ Cấu hình delay & độ nhạy dễ chỉnh  
- ✅ Phím K (scancode) làm bắn phụ  

Thời gian phản ứng thường **2–10ms**, tùy thuộc vào refresh rate màn hình.

---

## 🎯 Cách hoạt động
Triggerbot quét một **vùng nhỏ ở trung tâm màn hình (10x10 px)** để phát hiện enemy có viền **màu tím**:


RGB = (250, 100, 250)
Nếu phát hiện màu trùng khớp, nó sẽ gửi phím (K) xuống.
Bạn có thể chỉnh RGB và độ nhạy trong config.json.

⚙ Cài đặt
1️⃣ Yêu cầu
Cài các thư viện Python:

bash
Copy code
py -m pip install interception numpy mss keyboard pywin32
(Đảm bảo interception.dll đã cài đặt trên máy)

2️⃣ Cài đặt Valorant
Dùng Purple Outline

Thêm K làm bắn phụ

Tùy chọn: Tắt RawInput để tránh xung đột

3️⃣ File cấu hình (config.json)
json
Copy code
{
    "trigger_hotkey": "0xA0",
    "base_delay": 0.01,
    "trigger_delay": 40,
    "color_tolerance": 70,
    "always_enabled": false,
    "burst_delay": 0.05
}
Giải thích các thông số:

Key	Chức năng
trigger_hotkey	Phím kích hoạt khi không bật always_enabled
base_delay	Delay tối thiểu giữa các phát bắn
trigger_delay	Delay thêm theo % trên base_delay
color_tolerance	Độ nhạy quét màu
always_enabled	Nếu true, triggerbot luôn bật
burst_delay	Delay giữa các phát trong một chuỗi bắn

🎮 Phím điều khiển
Phím	Chức năng
TAB	Bật/tắt triggerbot
Ctrl + Shift + X	Thoát khẩn cấp

Có âm thanh phản hồi khi bật/tắt.

🖥 Hỗ trợ độ phân giải
Hỗ trợ 720p, 1080p, 1440p, 4K

Hỗ trợ màn hình stretched

Không phụ thuộc DPI / scaling

Tự cập nhật khi alt-tab

⚡ Hiệu năng
Thời gian phản ứng: 2–10ms

Có thể cải thiện thêm:

Quét GPU (DXCAM)

Viết lại bằng ngôn ngữ native (C++ / Rust)

Pin thread / CPU affinity

🔒 An toàn
Interception ít rủi ro, không đọc/ghi bộ nhớ

Pixel detection an toàn nhất

Sử dụng theo rủi ro của bạn

📦 Biên dịch
Biên dịch bằng Nuitka để tăng hiệu năng:

bash
Copy code
py -m nuitka --onefile triggerbot.py
📝 Tại sao làm fork này?
Gốc: nhanh nhưng cứng nhắc, không ổn định

Fork: tự động độ phân giải, hỗ trợ burst delay, toggle, an toàn và sạch hơn

⚡ License
Sử dụng có trách nhiệm. Fork này được cung cấp nguyên trạng.
