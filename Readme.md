# 🛡️ Python Keylogger

A lightweight and cross-platform **keystroke logger** built with Python using the `pynput` library. It captures and logs all keyboard inputs into a local file for analysis or monitoring purposes.

> ⚠️ **DISCLAIMER**  

> This tool is created strictly for **educational**, **parental control**, or **authorized security auditing** purposes. Unauthorized use of this script may violate privacy laws and result in legal consequences.  
> **Always obtain proper consent before monitoring any system.**

---

## 📚 Table of Contents

- [📚 Table of Contents](#-table-of-contents)
- [🚀 Features](#-features)
- [📂 Output File](#-output-file)
- [⚙️ Installation](#️-installation)
- [▶️ Usage](#️-usage)
- [🛑 Legal & Ethical Usage](#-legal--ethical-usage)
- [📄 License](#-license)
- [📬 Contact](#-contact)

---

## 🚀 Features

- ✅ Records all keyboard inputs
- ✅ Supports alphanumeric and special keys
- ✅ Logs data to a persistent text file
- ✅ Simple and minimalistic code
- ✅ Cross-platform (Windows, Linux, macOS)

---

## 📂 Output File

All captured keystrokes are saved to a file named:
`keylog.txt`

### Example log:

```
hello[Key.space]world[Key.enter]
```

Printable characters are logged directly, while special keys are enclosed in brackets (`[]`).


## ⚙️ Installation

Ensure you have Python 3.x installed on your system.

1. **Clone the Repository**

```bash
git clone https://github.com/AbdullahJaveid/python-keylogger.git
cd python-keylogger
```
2. **Install Required Library**

```bash
pip install pynput
```

## ▶️ Usage

Run the script:

```bash
python keylogger.py
```
Once executed:

- The script starts capturing all keypresses.

- The data is continuously appended to keylog.txt.

- To stop the logger, press Ctrl + C or manually terminate the process.

### 🛑 Legal & Ethical Usage
This project is intended only for authorized and ethical usage. Examples of acceptable use include:

- ✅ Parental monitoring with consent

- ✅ Personal security auditing

- ✅ Educational research and demonstrations

### ❌ Do NOT Use For:
- Spying or data theft

- Monitoring systems without owner’s consent

- Illegal surveillance

Using this tool irresponsibly is a criminal offense in many jurisdictions.

### 📄 License
This project is licensed under the GPL-3.0 license. You are free to use, modify, and distribute the software for ethical and legal purposes.

### 📬 Contact
Have suggestions or want to contribute? Feel free to open an issue or reach out:

- GitHub: AbdullahJaveid