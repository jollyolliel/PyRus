# 💻 Fake BSOD Prank (Windows Only)

This is a prank application that simulates a **fake Blue Screen of Death (BSOD)** on Windows. It captures the screen, overlays custom BSOD images, plays system alert sounds, and blocks keyboard input temporarily to simulate a crash.

> ⚠️ **WARNING:** This program blocks important keys like `Alt`, `Tab`, `Ctrl`, `Del`, and `Win`. Use responsibly. Only run in controlled environments with permission.

---

## 🧰 Requirements

- Windows OS
- Python 3.7+
- The following Python libraries:
  - `tkinter` (built-in)
  - `pyautogui`
  - `keyboard`
  - `Pillow`
  - `winsound` (Windows-only)

---

## 📦 Installation

1. **Clone the repository or download the script**

```bash
git clone https://github.com/your-username/fake-bsod-prank.git
cd fake-bsod-prank
```

2. **Install dependencies**

```bash
pip install pyautogui keyboard pillow
```

> Note: `winsound` and `tkinter` are included with Python on Windows.

---

## 📁 Folder Structure

```
fake-bsod-prank/
├── BSOD/
│   ├── bsod1.png
│   ├── bsod2.png
│   ├── bsod3.png
│   ├── bsod4.png
│   ├── bsod5.png
│   ├── bsod6.png
│   └── bsod7.png
├── main.py
├── desktop.png
```

Make sure the `BSOD/` folder contains all the required fake BSOD images named as `bsod1.png` through `bsod7.png`, and the root folder includes all sound files.

---

## 🚀 Running the Script

```bash
python prank.py
```

- The program waits 2 seconds, takes a screenshot, and overlays it as background.
- On **left click**, a sequence of BSOD images and sound effects is played.
- After completion, the window is closed and system input is restored.

---

## 🕹️ Controls

| Action             | Behavior                  |
|--------------------|---------------------------|
| Left-click         | Starts the BSOD sequence  |
| Alt, Ctrl, Win, etc| Blocked during sequence   |
| Alt+F4 / ESC       | Blocked (fullscreen only) |

---

## 🛑 Disclaimer

This tool is for **educational or entertainment** purposes **only**. Do not use it to deceive, harm, or annoy others. Ensure you have permission before running it on someone else's system.

---

## 👨‍💻 Author

- [Oliver](https://github.com/jollyolliel)



