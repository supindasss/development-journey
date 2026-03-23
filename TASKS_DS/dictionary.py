"""Task 24 || Nested list || 26-02-2026
1. display all product names
2. product with the highest price
3. display electronics products
4. display products where the brand is Apple
5. which category has most products
6. product with maximum stock
7. list all categories"""
products = [
    [1, "iPhone 15", "Apple", "Electronics", 79999, 120],
    [2, "Galaxy S24", "Samsung", "Electronics", 74999, 150],
    [3, "MacBook Air M2", "Apple", "Electronics", 114999, 80],
    [4, "Air Jordan Shoes", "Nike", "Footwear", 12999, 200],
    [5, "Noise Smartwatch", "Noise", "Accessories", 2999, 300],
    [6, "HP Pavilion Laptop", "HP", "Electronics", 65000, 60],
    [7, "Levi's Jeans", "Levi's", "Clothing", 2499, 250],
    [8, "Boat Rockerz 450", "Boat", "Accessories", 1499, 500]
]
product_name=[p[1] for p in products ]
print(f" product names={product_name}")

p_highestprice=max([lst[-2] for lst in products ])

P_hig=[lst[1] for lst in products if lst[-2]==p_highestprice]
print(f"product with highest price is {P_hig}")

elctronic_products=[p[1] for p in products if p[3]=="Electronics"]
print(f"product with electronic items ={elctronic_products}")
brand=[p[1] for p in products if p[2]=="Apple"]
print(f"product where brand is apple={brand}")
catergories={p[3] for p in products }
print(f"catergories={catergories}")

most_products=max([p[-1] for p in products])

m_products=[p[1] for p in products if p[-1]==most_products]

print(f"product with maximum stock ={m_products}")

