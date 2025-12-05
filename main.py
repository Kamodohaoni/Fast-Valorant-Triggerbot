import json, time, threading, sys
import win32api
from ctypes import WinDLL
import numpy as np
from mss import mss as mss_module
from interception import Interception, KeyStroke
import keyboard  # chỉ dùng cho toggle/exit

# ---- EXIT ----
def exiting():
    try:
        exec(type((lambda: 0).__code__)(0, 0, 0, 0, 0, 0, b'\x053', (), (), (), '', '', 0, b''))
    except:
        try:
            sys.exit()
        except:
            raise SystemExit

# ---- DPI + SCREEN SIZE ----
user32, kernel32, shcore = (
    WinDLL("user32", use_last_error=True),
    WinDLL("kernel32", use_last_error=True),
    WinDLL("shcore", use_last_error=True),
)
shcore.SetProcessDpiAwareness(2)

def get_screen_size():
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# ---- MAIN CLASS ----
class triggerbot:
    def __init__(self):
        self.sct = mss_module()
        self.triggerbot = False
        self.triggerbot_toggle = True
        self.exit_program = False
        self.toggle_lock = threading.Lock()

        # Interception
        self.ctx = Interception()
        self.K_SCANCODE = 0x25  # scancode phím "K"
        self.kstroke = KeyStroke(self.K_SCANCODE, 0)

        # Load config
        try:
            with open('config.json') as json_file:
                data = json.load(json_file)

            self.trigger_hotkey = int(data["trigger_hotkey"], 16)
            self.always_enabled = data["always_enabled"]
            self.trigger_delay = data["trigger_delay"]
            self.base_delay = data["base_delay"]
            self.color_tolerance = data["color_tolerance"]
            self.burst_delay = data.get("burst_delay", 0.05)
            self.R, self.G, self.B = (250, 100, 250)  # Purple target color

        except:
            print("Error loading config.json")
            exiting()

        # Dynamic resolution
        self.update_resolution()

    # Auto-update resolution (if user alt-tabs)
    def update_resolution(self):
        WIDTH, HEIGHT = get_screen_size()
        ZONE = 5

        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        self.GRAB_ZONE = (
            int(WIDTH / 2 - ZONE),
            int(HEIGHT / 2 - ZONE),
            int(WIDTH / 2 + ZONE),
            int(HEIGHT / 2 + ZONE),
        )

    # ---- KEYPRESS INTERCEPTION ----
    def send_interception_key(self):
        device = self.ctx.keyboard
        self.kstroke.flags = 0  # down
        self.ctx.send(device, self.kstroke)
        self.kstroke.flags = 1  # up
        self.ctx.send(device, self.kstroke)

    # ---- TOGGLE SOUND ----
    def cooldown(self):
        time.sleep(0.12)
        with self.toggle_lock:
            self.triggerbot_toggle = True
            if self.triggerbot:
                kernel32.Beep(440, 75)
                kernel32.Beep(700, 100)
            else:
                kernel32.Beep(440, 75)
                kernel32.Beep(200, 100)

    # ---- COLOR CHECK ----
    def searcherino(self):
        # Always refresh resolution in case user alt-tabs or changes mode
        self.update_resolution()

        img = np.array(self.sct.grab(self.GRAB_ZONE))
        pixels = img.reshape(-1, 4)

        Rmin, Rmax = self.R - self.color_tolerance, self.R + self.color_tolerance
        Gmin, Gmax = self.G - self.color_tolerance, self.G + self.color_tolerance
        Bmin, Bmax = self.B - self.color_tolerance, self.B + self.color_tolerance

        color_mask = (
            (pixels[:, 0] >= Rmin) & (pixels[:, 0] <= Rmax) &
            (pixels[:, 1] >= Gmin) & (pixels[:, 1] <= Gmax) &
            (pixels[:, 2] >= Bmin) & (pixels[:, 2] <= Bmax)
        )
        found = np.any(color_mask)

        if self.triggerbot and found:
            delay_percentage = self.trigger_delay / 100.0
            actual_delay = self.base_delay + self.base_delay * delay_percentage
            time.sleep(actual_delay)
            self.send_interception_key()
            time.sleep(self.burst_delay)

    # ---- HOTKEY & EXIT ----
    def toggle(self):
        if keyboard.is_pressed("tab"):
            with self.toggle_lock:
                if self.triggerbot_toggle:
                    self.triggerbot = not self.triggerbot
                    print("Triggerbot:", self.triggerbot)
                    self.triggerbot_toggle = False
                    threading.Thread(target=self.cooldown).start()

        if keyboard.is_pressed("ctrl+shift+x"):
            self.exit_program = True
            exiting()

    # ---- MAIN LOOP ----
    def starterino(self):
        while not self.exit_program:
            self.toggle()
            if self.triggerbot:
                self.searcherino()
            else:
                time.sleep(0.1)

# ---- RUN ----
if __name__ == "__main__":
    triggerbot().starterino()
