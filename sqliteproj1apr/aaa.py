import sqlite3

def execute_query(query, params=None, fetch=True):
    with sqlite3.connect("Northwind_small.sqlite") as conn:
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        if fetch:
            return cursor.fetchall()
        conn.commit()

# 1. Find Order Details
query1 = """
SELECT "Order".Id AS OrderID, Customer.CompanyName, Product.ProductName, OrderDetail.Quantity
FROM "Order"
INNER JOIN OrderDetail ON "Order".Id = OrderDetail.OrderId
INNER JOIN Customer ON "Order".CustomerId = Customer.Id
INNER JOIN Product ON OrderDetail.ProductId = Product.Id;
"""
order_details = execute_query(query1)
print("Order Details:")
print("{:<10} {:<30} {:<40} {:<10}".format("OrderID", "Customer Name", "Product Name", "Quantity"))
print("-" * 100)
for row in order_details:
    print("{:<10} {:<30} {:<40} {:<10}".format(*row))

# 2. Find Expensive Products
query2 = """
SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
FROM Product
INNER JOIN Supplier ON Product.SupplierId = Supplier.Id
WHERE Product.UnitPrice > 50;
"""
expensive_products = execute_query(query2)
print("\nExpensive Products:")
print("{:<40} {:<15} {:<30}".format("Product Name", "Unit Price", "Supplier Name"))
print("-" * 80)
for row in expensive_products:
    print("{:<40} {:<15.2f} {:<30}".format(*row))

# 3. Modify Product Prices
query3 = """
UPDATE Product
SET UnitPrice = UnitPrice * 1.10
WHERE CategoryId = (SELECT Id FROM Category WHERE CategoryName = 'Beverages');
"""
execute_query(query3, fetch=False)
print("Beverage prices updated.")
print("\n\n")

# 4. Add a New Customer
query4 = """
INSERT INTO Customer (Id, CompanyName, ContactName, Country, Phone)
VALUES ('TECHS', 'Tech Solutions Ltd.', 'Hiroshi Tanaka', 'Japan', '81-123-4567');
"""
execute_query(query4, fetch=False)
print("New customer added.")
print("\n\n")

# 5. Remove a Discontinued Product
query5 = """
DELETE FROM Product WHERE ProductName = 'Outback Lager';
"""
execute_query(query5, fetch=False)
print("Discontinued product removed.")
print("\n\n")

# 6. Find Top Customers by Order Count
query6 = """
SELECT Customer.CompanyName, COUNT("Order".Id) AS OrderCount
FROM "Order"
INNER JOIN Customer ON "Order".CustomerId = Customer.Id
GROUP BY Customer.Id
ORDER BY OrderCount DESC
LIMIT 5;
"""
top_customers = execute_query(query6)
print("Top Customers:", top_customers)