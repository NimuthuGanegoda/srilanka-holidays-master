
# 🇱🇰 Sri Lanka Holidays - Master Data Collection

<div align="center">

![License](https://img.shields.io/github/license/NimuthuGanegoda/srilanka-holidays-master?style=for-the-badge&color=blue)
![Last Commit](https://img.stellar.io/github/last-commit/NimuthuGanegoda/srilanka-holidays-master?style=for-the-badge&color=green)
![Data Integrity](https://img.shields.io/badge/Data-Verified-success?style=for-the-badge)

---

### 📅 **Validated Sri Lankan Holiday Datasets**
*Providing a standardized, enterprise-ready collection of holiday data (2021-2028).*

[Download Master Calendar](data/holidays/ics/srilanka-holidays.ics) • [View Datasets](data/holidays/)

</div>

---

## 📖 **Description**

An open-source ecosystem delivering high-accuracy Sri Lankan holiday data. This repository serves as the **unified master source**, offering validated datasets in multiple formats optimized for calendar integration and data analysis.

---

## ✨ **Core Features**

*   📅 **Extended Coverage**: Verified holiday data for **2021 through 2028**.
*   🏷️ **Visual Markers**: Instant identification via standard indicators: `*` (Public), `†` (Bank), and `‡` (Mercantile).
*   🍎 **Apple & Google Ready**: Strict **CRLF** compliance and **VTIMEZONE** support for flawless calendar sync.
*   🔔 **Smart Alarms**: Integrated `VALARM` notifications at 09:00 AM on the day preceding each holiday.
*   🔄 **CI/CD Automation**: Real-time synchronization and multi-format distribution (JSON, CSV, XML, ICS).

---

## 📂 **Project Structure**

A clean, modular architecture designed for high-integrity data management:

```bash
.
├── 📁 data/               # 📊 Standardized holiday datasets
│   └── 📁 holidays/       # 🏝️ Validated holiday collections
│       ├── ics/           # 🗓️ iCalendar files (Apple/Google optimized)
│       ├── json/          # 🏗️ Structured JSON for developers
│       ├── csv/           # 📑 Spreadsheet-ready formats
│       └── xml/           # 🧬 Legacy integration support
├── 📁 src/                # 💻 Core processing source code
│   └── converters/        # 🛠️ Data processing & sync scripts
├── 📁 requirements/       # 📋 Dependency management
│   ├── base.txt           # 📦 Core processing dependencies
│   └── github.txt         # 🤖 CI/CD specific requirements
└── 📁 public/             # 🎨 Project assets & documentation
```

---

## 🛠️ **Data Usage**

### **Calendar Subscription**
To subscribe to the master calendar in Apple or Google Calendar, use the direct raw URL of the `srilanka-holidays.ics` file.

### **Developer Integration**
Datasets are available in the `data/holidays/` directory in JSON, CSV, and XML formats for programmatic consumption.

---

## 🏛️ **Integrated Master Collection**

This project is a high-integrity consolidation of multiple specialized repositories. By integrating these diverse sources, we provide a **unified master collection** that offers the most comprehensive and feature-rich holiday dataset available for Sri Lanka.

Integrated projects include:
*   **API Framework & Core Data**: Providing the foundational structure and verified historical records.
*   **Calendar Enhancement Collection**: Inspired the inclusion of rich visual markers and enterprise-grade alarm features.
*   **Extended Master Datasets**: Contributing to the comprehensive 2021-2028 coverage and multi-format distribution logic.

---

## 🛡️ **Data Integrity**

Every holiday entry is manually cross-referenced with the **Official Government Gazette** of Sri Lanka. We prioritize data accuracy over automated heuristics to ensure 100% reliability for production environments.

---

<div align="center">
Developed with 💎 for the Sri Lankan Developer Community.
</div>
