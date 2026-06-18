# 🕵️ My Portfolio Website

Welcome to my portfolio website! This project showcases my work and skills using Flask, a lightweight WSGI web application framework in Python. It has been hardened with specific security logic to demonstrate a "Security-First" approach to web development.

## 📋 Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Security Showcase](#security-showcase)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact/Connect](#contactconnect)

---

## ✨ Features

- **Home Page**: A professional landing page to introduce visitors to my portfolio and technical background.
- **Dynamic Page Rendering**: Utilizes Flask's Jinja2 engine to render HTML pages dynamically based on URL strings.
- **Secure Form Submission**: Processes contact information with server-side validation and sanitization.
- **AppSec Hardening**: Built-in protection against CSV Injection (Formula Injection) to ensure data integrity.
- **Thank You Page**: A confirmation page displayed after successful data persistence.

---

## 🔧 Technologies Used

- **Flask**: Python web framework
- **HTML/CSS**: For the front-end design
- **CSV**: For form data storage
- **Python**: Main programming language

---

## 🔒 Security Showcase

In this project, I prioritized Application Security (AppSec) by addressing CSV Injection. Standard CSV logging is vulnerable if a user submits a message starting with `=`, `+`, `-`, or `@`.

**The Fix:** My `server.py` logic proactively detects these "dangerous" characters and prepends a single quote (`'`) to the input before writing to `database.csv`. This forces spreadsheet software to treat the input as literal text, preventing unauthorized command execution or data exfiltration.

---

## 🛠️ Installation

### 🐍 Verify Python

```bash
python3 --version
# Requires Python 3.x — download from https://www.python.org/downloads/
```

### 📥 Clone the Repository

```bash
git clone https://github.com/cainepavl/portfo.git
cd portfo
```

### ⬇️ Install Dependencies

```bash
pip3 install flask
```

### ▶️ Run the Application

```bash
python3 server.py
```

Open your browser and go to `http://127.0.0.1:50000/` to view the site.

---

## 🚀 Usage

1. Navigate to the home page to explore the portfolio.
2. Use the contact form to send a message. After submission, you'll be redirected to a thank you page.
3. Check the saved data in `database.txt` and `database.csv` to see form submissions.

---

## 🔧 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- [Flask](https://flask.palletsprojects.com/en/2.0.x/) for the web framework.
- [ZTM Academy](https://zerotomastery.io/courses/) for the course and walkthrough!
- All contributors and creators of open-source resources that made this project possible.

---

## 📩 Contact/Connect

**Caine Pavlosky**

* Email: [cainepavl@outlook.com](mailto:cainepavl@outlook.com)
* Portfolio: [fairdinkumstudios.com](https://fairdinkumstudios.com/)
* LinkedIn: [linkedin.com/in/cainepavlosky008](https://linkedin.com/in/cainepavlosky008)
