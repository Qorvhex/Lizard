<div align="center">

# 🦎 Qorvhex Lizard
### High-Speed Multithreaded Documentation Crawler & Scraper
**استخراج‌کننده و خزنده‌ی پرسرعت و هوشمند مستندات وب**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Qorvhex/Lizard/blob/main/qorvhex_lizard.ipynb)
[![Telegram Channel](https://img.shields.io/badge/Telegram-Qorvhex__Channel-2CA5E0?style=flat&logo=telegram&logoColor=white)](https://t.me/Qorvhex_Channel)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

<br/>

[**English**](#english-section) | [**فارسی (Persian)**](#persian-section)

</div>

---

<a id="english-section"></a>
## 🇬🇧 English

**Qorvhex Lizard** is a lightweight, multithreaded documentation crawler designed to recursively traverse developer docs, strip away boilerplate HTML (sidebars, navbars, footers, scripts, and code switchers), and produce a clean, unified text file. Ideal for feeding documentation into LLMs, RAG knowledge bases, or offline reading.

### ✨ Features
- 🚀 **High-Speed Multithreading**: Utilizes Python's `ThreadPoolExecutor` and connection pooling for maximum crawling throughput.
- 🧹 **Intelligent Noise Filter**: Automatically detects and strips headers, navigation bars, table of contents, pagination, feedback widgets, and code tab artifacts.
- ☁️ **1-Click Google Colab Deployment**: Run directly in Google Colab with interactive UI forms without installing anything locally.
- 🎯 **Domain & Path Filtering**: Constrains crawling to the source domain with an optional strict subpath restriction.
- 💾 **Clean Structured Output**: Writes title, source URL, and parsed clean text separated by structured delimiters.

---

### 🚀 Deploy to Google Colab

The easiest way to use **Qorvhex Lizard** is directly in your browser:

1. Click the **Open In Colab** badge:  
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Qorvhex/Lizard/blob/main/qorvhex_lizard.ipynb)  
   *(Note: Replace `USERNAME/qorvhex-lizard` in the URL with your GitHub username and repository name)*
2. Configure the parameters in the Colab Form (Target URL, Max Workers, Output File).
3. Click **Run** (`Ctrl + F9` or Run Cell).
4. Once completed, your formatted text file will automatically download to your computer!

---

### 💻 Local Installation & Usage

#### 1. Clone the repository
```bash
git clone https://github.com/USERNAME/qorvhex-lizard.git
cd qorvhex-lizard
```

#### 2. Install dependencies
```bash
pip install -r requirements.txt
```

#### 3. Run the crawler
```bash
# Basic run with defaults (Railway docs)
python crawler.py

# Custom target URL and output file
python crawler.py -u "https://docs.docker.com" -o "docker_docs.txt" -w 12

# Restrict crawling strictly to a specific subpath
python crawler.py -u "https://docs.python.org/3/tutorial/" --restrict-path
```

---

### ⚙️ Command-Line Arguments

| Flag | Full Option | Default | Description |
| :--- | :--- | :--- | :--- |
| `-u` | `--url` | `https://docs.railway.com` | Root documentation URL to start crawling from |
| `-o` | `--output` | `documentation_full.txt` | Destination file for the scraped text |
| `-w` | `--workers` | `10` | Number of parallel worker threads (1-25) |
| | `--restrict-path` | `False` | Only scrape URLs starting with the initial path |
| `-t` | `--timeout` | `10` | HTTP request timeout in seconds |

---

### 📢 Community & Support
Join our official Telegram channel for updates, scripts, and tools:  
👉 **[Qorvhex Telegram Channel](https://t.me/Qorvhex_Channel)**

---

<br/>

<a id="persian-section"></a>
## 🇮🇷 فارسی

**لیزارد (Qorvhex Lizard)** یک خزنده‌ی پرسرعت و چندنخی (Multithreaded) برای استخراج مستندات و داکیومنت‌های وب است. این ابزار صفحات داکیومنت را به صورت بازگشتی خزش کرده، تمام بخش‌های اضافی مانند منوها، فوترها، سایدبارها، کدهای جاوااسکریپت و تبلیغات را حذف می‌کند و محتوای خالص و تمیز را در قالب یک فایل متنی یکپارچه آماده می‌سازد. این خروجی برای مطالعه آفلاین یا آموزش و تغذیه مدل‌های زبانی (LLM / RAG) بسیار کاربردی است.

### ✨ ویژگی‌های کلیدی
- 🚀 **سرعت فوق‌العاده بالا**: بهره‌گیری از پردازش موازی و چندنخی (`ThreadPoolExecutor`) با مدیریت بهینه اتصالات شبکه.
- 🧹 **فیلتر و پاکسازی هوشمند**: حذف خودکار منوها، سایدبارها، فهرست مطالب (TOC)، دکمه‌های ناوبری، تب‌های سوییچ کد و نویزهای وب.
- ☁️ **اجرای آسان با ۱ کلیک در گوگل کولب (Google Colab)**: بدون نیاز به نصب پایتون یا وابستگی‌ها در سیستم شخصی.
- 🎯 **محدودسازی دامنه و مسیر**: جلوگیری از خروج خزنده از دامنه اصلی با قابلیت فعال‌سازی محدودیت به مسیر مشخص.
- 💾 **خروجی تمیز و مرتب**: دسته‌بندی هر صفحه به همراه عنوان، آدرس صفحه و متن تفکیک‌شده با خطوط جداکننده.

---

### 🚀 اجرای مستقیم در Google Colab

ساده‌ترین روش برای اجرای **Qorvhex Lizard** استفاده از محیط ابری گوگل کولب است:

1. بر روی دکمه‌ی زیر کلیک کنید:  
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Qorvhex/Lizard/blob/main/qorvhex_lizard.ipynb)  
   *(نکته: در صورت آپلود روی گیتهاب خود، عبارت `USERNAME/qorvhex-lizard` در لینک را با نام کاربری و نام مخزن خود جایگزین کنید)*
2. مقادیر مورد نظر را در فرم کولب وارد کنید (آدرس مستندات، نام فایل خروجی، تعداد پردازش همزمان).
3. دکمه‌ی اجرای سلول را بزنید (`Ctrl + F9`).
4. پس از اتمام کار، فایل متنی تمیز به صورت خودکار در سیستم شما دانلود خواهد شد!

---

### 💻 نصب و اجرای محلی

#### ۱. کلون کردن مخزن
```bash
git clone https://github.com/USERNAME/qorvhex-lizard.git
cd qorvhex-lizard
```

#### ۲. نصب پیش‌‌نیازها
```bash
pip install -r requirements.txt
```

#### ۳. اجرای اسکریپت
```bash
# اجرای پیش‌فرض
python crawler.py

# تعیین آدرس دلخواه، فایل خروجی و تعداد نخ‌ها
python crawler.py -u "https://docs.docker.com" -o "docker_docs.txt" -w 12

# محدود کردن استخراج فقط به یک زیرشاخه مشخص
python crawler.py -u "https://docs.python.org/3/tutorial/" --restrict-path
```

---

### ⚙️ راهنمای پارامترها و تنظیمات

| فلگ کوتاه | گزینه کامل | مقدار پیش‌فرض | توضیحات |
| :--- | :--- | :--- | :--- |
| `-u` | `--url` | `https://docs.railway.com` | آدرس اولیه و اصلی مستندات جهت شروع خزش |
| `-o` | `--output` | `documentation_full.txt` | نام و مسیر فایل متنی خروجی |
| `-w` | `--workers` | `10` | تعداد پردازش‌های همزمان (بین ۱ تا ۲۵) |
| | `--restrict-path` | `False` | محدود کردن خزش فقط به زیرمسیر آدرس اولیه |
| `-t` | `--timeout` | `10` | مهلت زمانی درخواست‌های شبکه به ثانیه |

---

### 📢 کانال تلگرام و پشتیبانی
برای دریافت ابزارهای بیشتر، اسکریپت‌ها و آموزش‌ها به کانال تلگرام ما بپیوندید:  
👉 **[کانال تلگرام Qorvhex](https://t.me/Qorvhex_Channel)**

---

### 📄 مجوز (License)
این پروژه تحت مجوز [MIT](LICENSE) منتشر شده است.
