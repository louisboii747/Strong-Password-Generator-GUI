🔐 Password Generator (GUI Version)

A simple yet powerful password generator with a graphical user interface built using Python and Tkinter.

## ✨ Features

- Generate random secure passwords
- Choose your own password length
- Automatically copy passwords to clipboard
- Beginner-friendly codebase using only the standard library

## 🖥️ Demo

![Password Generator GUI](https://raw.githubusercontent.com/louisboii747/Strong-Password-Generator-GUI/refs/heads/main/demo.gif)

## 🧰 Requirements

- Python 3.x  
- No external libraries required — `tkinter` comes with Python

## 🚀 How to Run

1. Download the script:
   ```bash
   git clone https://github.com/louisboii747/Strong-Password-Generator-GUI.git
   cd password-generator-gui
   ```

2. Run it with Python:
   ```bash
   python password_generator_gui.py
   ```

✅ A window will pop up where you can:
- Enter a password length (e.g. 16)
- Click **Generate**
- Click **Copy to Clipboard** to paste it anywhere

## 📂 File Structure

```
password-generator-gui/
├── password_generator_gui.py
└── README.md
```

## 🧠 How It Works

- Uses `random.choice()` to select characters from a pool of:
  - Uppercase + lowercase letters
  - Numbers
  - Special symbols
- Displays the password in a GUI window
- Supports clipboard copying with one click

## 🛠️ To-Do / Ideas

- [ ] Add option to toggle symbols, numbers, or uppercase
- [ ] Display password strength
- [ ] Dark mode GUI
- [ ] Save generated passwords to a file

## 📜 License

This project is licensed under the MIT License.

---

> Created by [Louis Hinchliffe](https://github.com/louisboii747)
