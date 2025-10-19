# Akü (Battery) Sales Analysis - Project

## Özet
Bu proje, Türkiye pazarına yönelik **akü (otomotiv / tüvit akü) satışlarını** analiz etmek için tasarlanmıştır. Amaç:
- Satış trendlerini görmek (aylık/yıllık)
- Bölge ve mağaza bazlı performans
- En çok satan akü modelleri ve kârlılık analizi
- Müşteri segmentasyonu (sık alıcılar vs tek seferlik)


**Not:** Gerçek veri kaynağı olarak Kaggle'daki "Turkish Market Sales Dataset" veya benzeri bir perakende satış dataset'i kullanılabilir.

## Gerekli Yazılımlar
- Windows + Power BI Desktop (kurulu)
- Anaconda / Python 3.10
- VS Code (opsiyonel)
- DB Browser for SQLite (opsiyonel)


## Klasör Yapısı
```
ecom_battery_project/
  data/                    # sales.csv dosyanızı buraya koyun
  notebooks/
    data_cleaning_and_analysis.py
  sql/
    queries.sql
  powerbi/
    POWERBI_DASHBOARD_PLAN.md
   reports/
  README.md
```

## Nasıl Başlanır 
1. Kaggle'dan uygun dataset'i indirin (ör. Turkish Market Sales Dataset) ve `data/sales.csv` olarak kaydedin.NOT:BEN PROJEMDE AKÜ DATASET'İ KULLANMAK İSTEDİM TÜRKİYE PAZARINA UYGUN ÖRNEK DATASET OLMADIĞINDAN CHATGPT DEN KAGGLE'DAN BİR DATASETİ BENİM İÇİN YORUMLAMASINI İSTEDİM
2. Anaconda Prompt açın:
   ```
   conda create -n ecomenv python=3.10 -y
   conda activate ecomenv
   pip install pandas sqlalchemy jupyter openpyxl
   ```
3. `notebooks/data_cleaning_and_analysis.py` içindeki adımları Jupyter Notebook veya VS Code'da çalıştırın.
4. Temizlenmiş CSV'yi `data/sales_clean.csv` olarak kaydedin.(Ben 'aku_satislari.csv' olarak kaydettim )
5. Power BI Desktop ile `data/sales_clean.csv` dosyasını import ederek dashboard oluşturun.


