from flask import Flask, redirect, render_template, request,url_for
import sqlite3 as sql

app = Flask(__name__)

def get_db_connection():
    conn = sql.connect("products.db")
    conn.row_factory = sql.Row  
    return conn
    
@app.route('/')
def home():
    conn = get_db_connection()
    products = conn.execute("SELECT * FROM products").fetchall()
    conn.close()
    return render_template("home.html", products=products)

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    conn = get_db_connection()
    product = conn.execute("SELECT * FROM products WHERE id = ?", (product_id,)).fetchone()
    conn.close()
    
    if product is None:
        return "Ürün bulunamadı", 404
    
    return render_template("detail.html", product=product)

@app.route("/category/<category>")
def category_page(category):
    conn = get_db_connection()
    products = conn.execute("SELECT * FROM products WHERE category = ?", (category,)).fetchall()
    conn.close()
    return render_template("category.html", products=products, category=category)

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query") 
    if query:
        conn = get_db_connection()
        products = conn.execute("""
            SELECT * FROM products
            WHERE description LIKE ? OR category LIKE ? OR CAST(price AS TEXT) LIKE ?
        """, (f"%{query}%", f"%{query}%", f"%{query}%")).fetchall()
        conn.close()
    else:
        products = []  # Eğer query boşsa sonuçları boş döndür

    return render_template("search.html", products=products, query=query)


if __name__ == "__main__":
    app.run(debug=True)