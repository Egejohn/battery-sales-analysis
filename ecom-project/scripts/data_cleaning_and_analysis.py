# 📊 Veri Analisti Mini Projesi: Akü Satış Analizi 
# ---------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r"C:\PROJECTS\ecom-project\data\orders.csv")

print("📋 Sütunlar:", df.columns.tolist(), "\n")

print("🧩 Eksik veri sayısı:\n", df.isnull().sum(), "\n")

df_battery = df[df['urun_adi'].str.contains('akü|battery', case=False, na=False)]

print(f"🔋 Toplam {len(df_battery)} satır akü ürünleriyle ilgili bulundu.\n")


print("💰 Akü ürünleri fiyat istatistikleri:\n", df_battery['birim_fiyat'].describe(), "\n")

city_sales = df_battery.groupby('sehir')['adet'].sum().sort_values(ascending=False)
print("🌆 Şehirlere göre akü satış miktarları:\n", city_sales, "\n")


plt.figure(figsize=(10,5))
sns.barplot(x=city_sales.index, y=city_sales.values, hue=city_sales.index, legend=False, palette="cool")

plt.title("Şehirlere Göre Akü Satışları")
plt.xlabel("Şehir")
plt.ylabel("Satış Adedi")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


output_path = r"C:\PROJECTS\ecom-project\data\aku_satislari.csv"
df_battery.to_csv(output_path, index=False)
print(f"✅ Filtrelenmiş veri '{output_path}' dosyasına kaydedildi.")
