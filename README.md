
# 🚀 Automation Testing Framework

This repository contains a complete automation testing suite covering **Web UI Automation, Windows Desktop Automation, Wiki Mobile App Automation, and API Automation** using Python-based frameworks and industry-standard tools.

---

## 📌 Project Overview

This automation framework is designed to validate end-to-end application workflows across different platforms:

- 🌐 Web Automation (Selenium)
- 🪟 Windows Notepad Automation (Pywinauto / PyAutoGUI)
- 📱 Wiki App Automation (Used Cloud platform Browserstack to test Wiki app in Andriod device)
- 🔌 API Automation (Requests / Pytest)

The framework is built with scalability, maintainability, and modular structure in mind.

---

## 🧰 Tech Stack & Tool Versions

| Component | Technology |
|----------|------------|
| Programming Language | Python 3.10+ |
| Web Automation | Selenium |
| API Testing | Requests, Pytest |
| Desktop Automation | Pywinauto / PyAutoGUI |
| Test Framework | Pytest |
| Reporting | HTML Reports / Allure (if used) |
| Version Control | Git & GitHub |
| IDE | PyCharm / VS Code |
| OS Support | Windows / Linux |

---

## 📁 Project Structure

automation-framework/
│
├── tests/
│   ├── web/                # Web automation test cases
│   ├── windows/            # Notepad desktop automation
│   ├── wiki/               # Wiki application automation
│   ├── api/                # API test cases
│
├── pages/                  # Page Object Model (Web UI)
├── utils/                  # Reusable utilities (driver, config, helpers)
├── testdata/               # Test data files (JSON/CSV)
├── reports/                # Generated test reports
├── conftest.py             # Pytest fixtures
├── requirements.txt        # Dependencies
└── README.md

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Voyager1-u/AutomationAssessment
cd AutomationAssessment
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Install Browser Drivers (for Web Automation)

- Download ChromeDriver matching your Chrome version
- Add it to system PATH  
OR
- Use webdriver-manager (recommended)

---

## ▶️ How to Execute Tests

### Run All Tests
```bash
pytest
```

### Run Web Tests
```bash
pytest tests/web/
```

### Run API Tests
```bash
pytest tests/api/
```

### Run Wiki App Tests
```bash
pytest tests/wiki/
```

### Run Windows Notepad Tests
```bash
pytest tests/windows/
```

---

## 📊 Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

Report location:
```
reports/report.html
```

---

## 🧪 Features

- Page Object Model (POM) for Web Automation
- Reusable utilities and helpers
- Modular test design
- API validation with status and schema checks
- Desktop automation support
- Logging and reporting integration
- CI/CD ready structure

---

## 👨‍💻 Author

Udayanand Chintalapalli  
Automation Test Engineer (Web, API, Desktop, Storage Testing)

---

## 📌 Notes

- Always use virtual environment
- Ensure browser driver compatibility
- Update dependencies when required
- Test data can be modified inside testdata folder
