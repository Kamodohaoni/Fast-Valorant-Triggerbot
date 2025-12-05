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

python
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

