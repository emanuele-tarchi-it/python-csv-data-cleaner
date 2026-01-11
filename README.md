# Python CSV Data Cleaner

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Pandas](https://img.shields.io/badge/library-Pandas-orange.svg)

An automated utility designed to transform "messy" CSV files into structured, clean datasets. Ideal for data analysts and businesses that need to prep data for databases or BI tools.

## ✨ Features
- **Empty Row Removal:** Automatically detects and drops rows that contain no data.
- **String Normalization:** Trims hidden whitespaces from text (leading and trailing).
- **Smart Type Conversion:** Converts columns to numeric types where possible for better analysis.
- **Safe Export:** Generates a new cleaned file without modifying the original source.

## 🛠 Prerequisites
This tool uses the **Pandas** library. You can install it via terminal:
```bash
pip install pandas
```

🚀 How to Use
Clone the repository.

Place your "dirty" CSV in the project folder.

Open csv_cleaner.py and update the input_file name in the main block.

Run: python csv_cleaner.py

## 📄 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---
*Developed by Emanuele Tarchi | Automation Specialist Portfolio*
