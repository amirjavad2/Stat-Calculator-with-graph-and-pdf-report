---
# 📊 Statistic Calculator

A powerful, Python-based statistics pipeline that takes in raw float data, builds a full frequency distribution table, calculates statistical values (mean, median, standard deviation, variance), generates visualizations (line, bar, histogram, scatter, pie), and exports it all into a clean PDF report.

---

## 🔧 Features

- ✅ Accepts raw float data (manual input or from `.txt` file)
- ✅ Automatically:
  - Sorts and counts data points
  - Builds a **Frequency Distribution Table** with `xi`, `fi`, `pi`, `si`
  - Computes **mean**, **median**, **standard deviation**, and **variance**
  - Generates 5 types of plots with `matplotlib`
  - Saves all visualizations as PNGs
  - Combines everything into a **PDF report**
- ✅ Exports:
  - CSV file for the frequency table
  - PDF report including:
    - Sorted data
    - Frequency table
    - Stats summary
    - All graphs

---

## 🖼️ Output Preview

**PDF Content Includes:**
1. Sorted Data (top)
2. Frequency Distribution Table (auto-formatted)
3. Statistical Summary
4. Visual Graphs (2 per line, except Pie chart)

All visuals are saved at high resolution (300 DPI).

---

## 📁 File Structure

```

project/
│
├── main.py               # The main script
├── data.txt              # Sample input data file
├── dataframe.csv         # Auto-generated table export
├── Stat report.pdf       # Final exported PDF
├── \*.png                 # Auto-generated graphs
└── README.md

````

---

## 🧪 How to Use

### 📌 Requirements

- Python 3.x
- Libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `fpdf`
  - `os`, `re`

Install dependencies:
```bash
pip install numpy pandas matplotlib fpdf
````

---

### 🚀 Run the Program

```bash
python main.py
```

You can either:

* Let the program **generate random float data**
* Or modify `data.txt` to use your own dataset (one float per line or separated by spaces)

---

## 📥 Sample Input (data.txt)

```
38.74 38.16 32.73 37.54 31.69 52.96 48.27 33.04 53.56 42.79 50.01 44.44 46.32 36.45 46.98 45.83 33.79 43.13 51.04 49.09 45.22 45.08 39.76 49.96 38.58 39.09 51.23 40.59 37.93 40.31 38.24 32.05 45.5 53.67 37.39 45.94 54.2 30.2 37.17 30.86 31.72 44.78 51.95 42.65 54.75 30.35 36.07 45.75 32.82 38.31 35.17 43.71 46.47 32.39 39.29 44.6 49.15 32.13 52.64 52.74 34.33 42.04 54.45 39.51 35.54 48.89 34.85 53.7 46.12 42.6 51.84 35.77 52.27 44.19 52.88 52.31 49.29 40.79 48.61 40.11

```
* Remember to seprate all numbers with only one space code will od the rest 
---

## 📤 Output Location

All files are exported to your **Documents** folder:

* `Stat report.pdf` – the full PDF report
* `dataframe.csv` – frequency table in CSV format

---

## 🧠 Developer Notes

* Handles edge cases where data might fall out of range
* All intervals are automatically calculated using **Sturges' Rule**
* Designed with performance in mind — minimal nested loops
* Easily extendable with CLI support or GUI (e.g. using Tkinter)

---

## 📜 License

This project is open source and free to use for educational and analytical purposes.

---

## ✍️ Author

Made by [@AmirJavad](https://github.com/your-username) — future AI engineer, lover of chaos, conqueror of data.

