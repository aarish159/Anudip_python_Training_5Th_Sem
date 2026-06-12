# Library Book Availability System

books = {
    "Python": 5,
    "Java": 2,
    "DBMS": 4,
    "Networking": 1,
    "OS": 3,
    "AI": 6,
    "ML": 2,
    "Cloud": 5,
    "Cyber Security": 1,
    "Web Development": 4
}

# 1. Display books with fewer than 3 copies
print("Books Requiring Attention:")
for book in books:
    if books[book] < 3:
        print(book)

# 2. Find the book with maximum copies
max_book = None
max_copies = -1
for book in books:
    if books[book] > max_copies:
        max_copies = books[book]
        max_book = book
print("Book with Maximum Copies:", max_book, "(", max_copies, "copies)")

# 3. Find the book with minimum copies
min_book = None
min_copies = 9999
for book in books:
    if books[book] < min_copies:
        min_copies = books[book]
        min_book = book
print("Book with Minimum Copies:", min_book, "(", min_copies, "copies)")

# 4. Count total books available
total = 0
for book in books:
    total += books[book]
print("Total Copies Available:", total)

# 5. Generate a restocking list (<3 copies)
restock_list = []
for book in books:
    if books[book] < 3:
        restock_list.append(book)
print("Restocking List:", restock_list)
