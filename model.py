import sqlite3

# Database oluşturuldu
conn = sqlite3.connect("products.db")
cursor = conn.cursor()

# Ürün tablosunu oluştur
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Ürün No
    description TEXT NOT NULL,            -- Açıklama
    price REAL NOT NULL,                  -- Fiyat
    category TEXT NOT NULL,               -- Kategori
    image TEXT NOT NULL                   -- Resim Yolu
)
""")

products = [
    ("Topuklu bot", 1690.99, "Dış Giyim", "ayakkabı1.jpg"),
    ("Pamuklu günlük bluz", 420.99, "Kadın Giyim", "bluz1.jpg"),
    ("Spor kışlık ceket", 1390.99, "Dış Giyim", "ceket1.jpg"),
    ("Şık elbise", 1249.99, "Kadın Giyim", "elbise1.jpg"),
    ("Tüylü kaban", 2890.99, "Dış Giyim", "kaban1.jpg"),
    ("Bordo yünlü kışlık kazak", 1190.99, "Kadın Giyim", "kazak1.jpg"),
    ("V yaka yünlü kazak", 1159.99, "Kadın Giyim", "kazak2.jpg"),
    ("Gri günlük pantolon", 940.99, "Kadın Giyim", "pantolon1.jpg"),
    ("Düşük bel pantolon", 1190.99, "Kadın Giyim", "pantolon2.jpg"),
    ("Kısa paça kot pantolon", 940.99, "Kadın Giyim", "pantolon3.jpg"),
    ("Pamuklu saran t-shirt", 290.99, "Kadın Giyim", "tshirt1.jpg"),
    ("İkili t-shirt seti", 710.99, "Kadın Giyim", "tshirt2.jpg")
]

cursor.executemany("""
INSERT INTO products (description, price, category, image) 
VALUES (?, ?, ?, ?)
""", products)

conn.commit()
conn.close()

print("Veritabanı oluşturuldu ve ürünler eklendi!")