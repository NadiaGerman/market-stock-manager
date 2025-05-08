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
# === Q4: Products in "Beverage" category ===
print("\n🍹 Q4 - Beverages Only:")
for product in products:
    if product["category"].lower() == "beverage":
        print(f"- {product['name']}")

# === Q5: Product with the lowest price ===
print("\n💰 Q5 - Cheapest Product:")
cheapest = min(products, key=lambda p: p["price"])
print(f"- {cheapest['name']} at ${cheapest['price']}")

# === Q6: Beverages priced below $3 ===
print("\n🥤 Q6 - Beverages Under $3:")
for product in products:
    if product["category"].lower() == "beverage" and product["price"] < 3:
        print(f"- {product['name']} (${product['price']})")
# === Q7: Total stock value (price * stock)
print("\n📦 Q7 - Total Stock Value:")
total_value = sum(product["price"] * product["stock"] for product in products)
print(f"💰 Total Value: ${total_value:.2f}")

# === Q8: Average product price
print("\n📊 Q8 - Average Product Price:")
avg_price = sum(p["price"] for p in products) / len(products)
print(f"📉 Average Price: ${avg_price:.2f}")

# === Q9: Only products in stock (stock > 0)
print("\n✅ Q9 - In-Stock Products:")
for product in products:
    if product["stock"] > 0:
        print(f"- {product['name']} ({product['stock']} in stock)")
