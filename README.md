# ⚡ DevPulse Desktop

> A hybrid desktop & terminal utility application powered by an **Electron GUI frontend** and a **Python backend engine**.

DevPulse offers developer-centric utilities including live weather querying and instant local file text analytics—available both as a dark-themed desktop application and as a standalone Command-Line Interface (CLI).

---

## 🚀 Key Features & Capabilities

* 🌤️ **Live Weather Queries:** Search real-time weather metrics for any city globally (Temperature, Humidity, and Wind Speed).
* 📊 **Text File Analyzer:** Compute total line counts, word counts, and character counts across local files (`.txt`, `.md`, `.py`, `.csv`, `.json`).
* 🔄 **CSV to JSON Converter:** Convert raw structured CSV spreadsheets into formatted JSON outputs.
* 🖥️ **Hybrid Architecture:** Modern Electron dark-theme user interface running a high-performance Python process in the background.
* 💻 **Dual Execution:** Use the visual desktop app (`npm start`) or the terminal command tool (`devpulse weather Medan`).

---

## 🌐 Data Sources & Tech Stack

### Data Sources
* **Geocoding & Location:** [Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api) for resolving city names into latitude/longitude coordinates.
* **Weather Metrics:** [Open-Meteo Weather Forecast API](https://open-meteo.com/en/docs) for non-key, real-time meteorological metrics.

### Core Stack
* **Frontend UI:** Electron, HTML5, CSS3 (Dark Mode), Vanilla JS.
* **Backend Engine:** Python 3, `requests`, `rich` (CLI formatting), `argparse`.
* **IPC Bridge:** Node.js `child_process` communicating asynchronously via JSON flags.

---

## 🛠️ Prerequisites

Before installing, ensure you have the following installed on your system:

* **Node.js:** `v18.0.0` or higher (`node -v`)
* **Python:** `3.8` or higher (`python --version`)
* **Git:** Version control (`git --version`)

---

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/susenayw/CLI-Tool.git](https://github.com/susenayw/CLI-Tool.git)
cd devpulse-cli