# 🏙️ Calgary Community Housing Analysis

![Python](https://img.shields.io/badge/Python-3.12-blue)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey)
![Status](https://img.shields.io/badge/Status-Completed-green)

## 🎯 Business Objective
To analyze community housing density in Calgary, providing data-driven insights into residential distribution patterns. This project aims to assist urban planners and policy makers in identifying high-density clusters and potential areas for infrastructure development.

---

## 📊 Key Insights
* **Granular Data:** Analyzed over 140 variables, including demographic counts, dwelling types, and pet ownership across all Calgary communities.
* **Density Metrics:** Calculated precise Resident-to-Dwelling ratios to uncover community development trends.

---

## 🛠️ Tech Stack & Methodology
| Phase | Tool | Description |
| :--- | :--- | :--- |
| **ETL** | `pandas` | Extracted, cleaned, and transformed raw Census CSV data. |
| **Storage** | `SQLite` | Structured the data into a relational database for efficient querying. |
| **Analysis** | `SQL` | Performed complex aggregations to calculate density ratios. |
| **Visualization**| `matplotlib` | Created visual reports for data-driven storytelling. |

---

## 🚀 How to Run
Follow these steps to reproduce the analysis on your machine:

1. **Clone the repository:**
```bash
   git clone [https://github.com/a4ahad/calgary-housing-analysis.git](https://github.com/a4ahad/calgary-housing-analysis.git)
   cd calgary-housing-analysis
```

2. **Generate Analysis:**
```bash
    python3 create_db.py
    python3 visualize.py
```

## 📈 Visual Report
*![Bar chart: Top 10 Calgary communities ranked by resident-to-dwelling density. Leading communities include Scarboro (2.75), Bonavista Downs (2.46), and Springbank Hill (3.00). Seven communities reached the maximum density ratio of 3.00, while Greenwood/Greenbriar showed the lowest among the top 10 at 1.72 residents per dwelling.](density_chart.png)*

## 👨‍💻 Author
**Md Abdul Ahad**  
Aspiring Data Analyst | MSc in Big Data Analytics