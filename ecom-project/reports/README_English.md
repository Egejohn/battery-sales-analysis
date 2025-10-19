İşte dosya adlarını çevirmeden README.md dosyanın tamamının İngilizce çevirisi:

````{"id":"80542","variant":"standard","title":"Battery Sales Analysis - English Translation"}
# Battery Sales Analysis - Project

## Summary
This project is designed to analyze **battery (automotive / tubular battery)** sales in the Turkish market. The objectives are:
- To observe sales trends (monthly/yearly)
- To analyze performance by region and store
- To identify the best-selling battery models and profitability
- To perform customer segmentation (frequent buyers vs one-time customers)

**Note:** As a real data source, you can use the "Turkish Market Sales Dataset" or a similar retail sales dataset available on Kaggle.

## Required Software
- Windows + Power BI Desktop (installed)
- Anaconda / Python 3.10
- VS Code (optional)
- DB Browser for SQLite (optional)

## Folder Structure
```
ecom_battery_project/
  data/                    # place your sales.csv file here
  notebooks/
    data_cleaning_and_analysis.py
  sql/
    queries.sql
  powerbi/
    POWERBI_DASHBOARD_PLAN.md
  reports/
  README.md
```

## How to Start
1. Download a suitable dataset from Kaggle (e.g., Turkish Market Sales Dataset) and save it as `data/sales.csv`.  
   **NOTE:** In my project, I wanted to use a battery dataset, but since there was no dataset suitable for the Turkish market, I asked ChatGPT to interpret a Kaggle dataset for me.  
2. Open the Anaconda Prompt:
   ```
   conda create -n ecomenv python=3.10 -y
   conda activate ecomenv
   pip install pandas sqlalchemy jupyter openpyxl
   ```
3. Run the steps in `notebooks/data_cleaning_and_analysis.py` using Jupyter Notebook or VS Code.
4. Save the cleaned CSV as `data/sales_clean.csv`.  
   (I saved it as `aku_satislari.csv`.)
5. Import the `data/sales_clean.csv` file into Power BI Desktop and create a dashboard.

