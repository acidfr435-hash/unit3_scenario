import csv
import re

# 1. Read book records from books.csv
books = []
with open("book.csv", mode="r") as file:
  reader = csv.DictReader(file)
  for row in reader:
    books.append(row)

# 2. Display all book details
print("--- All Books ---")
for book in books:
  print(f"Title: {book['Title']} | Author: {book['Author']}")

# 3. Search books whose title starts with a user-entered keyword using RegEx
keyword = input("\nEnter starting keyword to search: ")

# ^ means starts with, re.IGNORECASE makes it not case-sensitive
pattern = re.compile(f"^{keyword}", re.IGNORECASE)

print(f"\n--- Search Results (Starting with '{keyword}') ---")
found = False
for book in books:
  if pattern.match(book["Title"]):
    print(f"Title: {book['Title']} | Author: {book['Author']}")
    found = True

if not found:
  print("No matching books found.")