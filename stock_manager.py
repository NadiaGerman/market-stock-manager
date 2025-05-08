import json

STOCK_FILE = 'data/stock.json'

# === Load Stock Data ===
with open(STOCK_FILE, 'r') as f:
    products = json.load(f)

# === Q1: Print product names ===
print("📦 Q1 - Product Names:")
for product in products:
    print("-", product['name'])

# === Q2: Print name and stock ===
print("\n📦 Q2 - Name & Stock:")
for product in products:
    print(f"- {product['name']}: {product['stock']} in stock")

# === Q3: Products with stock > 50 ===
print("\n📦 Q3 - Stock > 50:")
for product in products:
    if product['stock'] > 50:
        print("-", product['name'])
