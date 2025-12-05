
# 🌌 Fast-Purple Triggerbot (Python Interception Fork)

**The fastest and most stable Python-based triggerbot fork.**  
Optimized for dynamic resolution, burst delay, and extremely low reaction times.

**Triggerbot nhanh nhất và ổn định nhất bằng Python.**  
Tối ưu cho độ phân giải linh hoạt, hỗ trợ burst delay, và phản ứng cực nhanh.

---

## 🚀 About This Fork / Giới thiệu
This fork is an enhanced version of the original Fast Valorant Triggerbot with:  
Fork này là phiên bản nâng cấp của Fast Valorant Triggerbot gốc, với:

- ✅ Interception Python (low-latency key injection) / Nhấn phím cực nhanh, thấp độ trễ  
- ✅ Auto-resolution / DPI awareness / Tự động nhận độ phân giải, DPI awareness  
- ✅ TAB toggle system / Hệ thống toggle bằng TAB  
- ✅ Burst-delay support / Hỗ trợ burst-delay  
- ✅ Safer threading & cooldown feedback / Threading an toàn và phản hồi bằng âm thanh  
- ✅ Optimized color scanning / Quét màu tối ưu  
- ✅ Configurable delays & tolerance / Cấu hình delay & độ nhạy dễ chỉnh  
- ✅ K key (scancode) as secondary fire / Phím K (scancode) làm bắn phụ  

Reaction times are **typically 2–10ms**, depending on your refresh rate.  
Thời gian phản ứng thường **2–10ms**, tùy thuộc vào refresh rate màn hình.

---

## 🎯 How It Works / Cách hoạt động
The bot scans a small **center screen zone (10x10 px)** for enemies with purple outline:  
Triggerbot quét một **vùng nhỏ ở trung tâm màn hình (10x10 px)** để phát hiện enemy có viền **màu tím**:

```text
RGB = (250, 100, 250)
````

If a match is detected, it sends a keypress (`K` scancode).
Nếu phát hiện màu trùng khớp, nó sẽ gửi phím (`K` scancode).

RGB and tolerance can be adjusted in `config.json`.
Bạn có thể chỉnh RGB và độ nhạy trong file `config.json`.

---

## ⚙ Setup / Cài đặt

### 1️⃣ Requirements / Yêu cầu

Install Python dependencies:
Cài các thư viện Python:

```bash
py -m pip install interception numpy mss keyboard pywin32
```

*(Make sure interception.dll is installed on your system / Đảm bảo `interception.dll` đã cài đặt trên máy.)*

### interception install link/link cài đặt interception:https://github.com/oblitum/Interception

### video tutorial install interception/video hướng dẫn cài đặt interception:https://www.youtube.com/watch?v=dM61_2B_1tM

### 2️⃣ Valorant Settings / Cài đặt Valorant

* Use Purple Outline / Dùng Purple Outline
* Add `K` as secondary shoot key / Thêm K làm bắn phụ
* Optional: disable RawInput to avoid conflicts / Tùy chọn: Tắt RawInput để tránh xung đột

### 3️⃣ Config File (`config.json`) / File cấu hình

```json
{
    "trigger_hotkey": "0xA0",
    "base_delay": 0.01,
    "trigger_delay": 40,
    "color_tolerance": 70,
    "always_enabled": false,
    "burst_delay": 0.05
}
```

**Key Explanation / Giải thích các thông số:**

| Key             | Function                                    | Chức năng                                   |
| --------------- | ------------------------------------------- | ------------------------------------------- |
| trigger_hotkey  | VirtualKey code when not always enabled     | Phím kích hoạt khi không bật always_enabled |
| base_delay      | Minimum delay between shots                 | Delay tối thiểu giữa các phát bắn           |
| trigger_delay   | Extra percentage delay on top of base_delay | Delay thêm theo % trên base_delay           |
| color_tolerance | RGB detection tolerance                     | Độ nhạy quét màu                            |
| always_enabled  | If true, triggerbot is always on            | Nếu true, triggerbot luôn bật               |
| burst_delay     | Delay between shots in a burst              | Delay giữa các phát trong một chuỗi bắn     |

---

## 🎮 Controls / Phím điều khiển

| Key              | Function                 | Chức năng          |
| ---------------- | ------------------------ | ------------------ |
| TAB              | Toggle triggerbot on/off | Bật/tắt triggerbot |
| Ctrl + Shift + X | Emergency exit           | Thoát khẩn cấp     |

Sound feedback is included.
Có âm thanh phản hồi khi bật/tắt.

---

## 🖥 Resolution Support / Hỗ trợ độ phân giải

* Works on 720p, 1080p, 1440p, 4K / Hỗ trợ 720p, 1080p, 1440p, 4K
* Works with stretched resolutions / Hỗ trợ màn hình stretched
* DPI / scaling independent / Không phụ thuộc DPI / scaling
* Auto-updates when alt-tabbing / Tự cập nhật khi alt-tab

---

## ⚡ Performance Notes / Hiệu năng

Reaction time: 2–10ms (depends on monitor refresh rate)
Thời gian phản ứng: 2–10ms

Optional improvements / Có thể cải thiện thêm:

* GPU capture (DXCAM) / Quét GPU
* Native rewrite (C++ / Rust) / Viết lại bằng ngôn ngữ native
* Thread pinning / CPU affinity / Pin thread / CPU affinity

---

## 🔒 Safety / An toàn

* Interception is low-risk, no memory reading/writing / Interception ít rủi ro, không đọc/ghi bộ nhớ
* Pixel detection is the safest type of automation / Pixel detection an toàn nhất
* Use at your own risk / Sử dụng theo rủi ro của bạn

---

## 📦 Compilation / Biên dịch

Compile using Nuitka for better performance:
Biên dịch bằng Nuitka để tăng hiệu năng:

```bash
py -m nuitka --onefile triggerbot.py
```

---

## 📝 Why This Fork? / Tại sao làm fork này?

Original: fast but hardcoded, unstable / Gốc: nhanh nhưng cứng nhắc, không ổn định
Fork: auto-resolution, burst delay, toggle system, safer & cleaner / Fork: tự động độ phân giải, hỗ trợ burst delay, toggle, an toàn và sạch hơn

---

## ⚡ License

Use responsibly. This fork is provided as-is.
Sử dụng có trách nhiệm. Fork này được cung cấp nguyên trạng.

