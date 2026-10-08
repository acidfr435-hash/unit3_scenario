import csv

# 1. Read mobile details from mobiles.csv
filename = "mobiles.csv"
mobiles = []

try:
  with open(filename, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
      mobiles.append(row)
except FileNotFoundError:
  print(f"Error: The file '{filename}' was not found.")
  exit()

# 2. Display all mobile records
print("--- All Mobile Records ---")
for mobile in mobiles:
  print(
      f"Brand: {mobile['Brand']} | Model: {mobile['Model']} | Price:"
      f" ${mobile['Price']} | Storage: {mobile['Storage']}"
  )

# 3. Search mobiles using Brand Name
search_brand = input(
    "\nEnter Brand Name to search (e.g., Apple, Samsung): "
).strip()

print(f"\n--- Search Results for Brand: '{search_brand}' ---")
found = False
for mobile in mobiles:
  # Case-insensitive comparison for the brand name
  if mobile["Brand"].lower() == search_brand.lower():
    print(
        f"Brand: {mobile['Brand']} | Model: {mobile['Model']} | Price:"
        f" ${mobile['Price']} | Storage: {mobile['Storage']}"
    )
    found = True

if not found:
  print(f"No mobile records found for brand '{search_brand}'.")