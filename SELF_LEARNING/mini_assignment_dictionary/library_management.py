# Digital Library Management System

library = {
    "B101": {"title": "Python Basics", "author": "ABC", "copies": 5},
    "B102": {"title": "Data Science", "author": "XYZ", "copies": 0},
    "B103": {"title": "Java Programming", "author": "LMN", "copies": 3},
    "B104": {"title": "Machine Learning", "author": "PQR", "copies": 2},
    "B105": {"title": "Operating Systems", "author": "DEF", "copies": 7},
    "B106": {"title": "Computer Networks", "author": "GHI", "copies": 1},
    "B107": {"title": "DBMS", "author": "JKL", "copies": 4},
    "B108": {"title": "C++ Basics", "author": "MNO", "copies": 6},
    "B109": {"title": "Algorithms", "author": "UVW", "copies": 2},
    "B110": {"title": "Cybersecurity", "author": "RST", "copies": 8},
    "B111": {"title": "AI Fundamentals", "author": "AAA", "copies": 0},
    "B112": {"title": "Cloud Computing", "author": "BBB", "copies": 5},
    "B113": {"title": "Big Data", "author": "CCC", "copies": 3},
    "B114": {"title": "Statistics", "author": "DDD", "copies": 9},
    "B115": {"title": "Discrete Math", "author": "EEE", "copies": 2},
    "B116": {"title": "Compiler Design", "author": "FFF", "copies": 1},
    "B117": {"title": "Theory of Automata", "author": "GGG", "copies": 4},
    "B118": {"title": "Software Engineering", "author": "HHH", "copies": 6},
    "B119": {"title": "Web Development", "author": "III", "copies": 7},
    "B120": {"title": "Mobile Computing", "author": "JJJ", "copies": 3},
    "B121": {"title": "Parallel Computing", "author": "KKK", "copies": 2},
    "B122": {"title": "Data Mining", "author": "LLL", "copies": 5},
    "B123": {"title": "Information Retrieval", "author": "MMM", "copies": 0},
    "B124": {"title": "Blockchain", "author": "NNN", "copies": 1},
    "B125": {"title": "IoT", "author": "OOO", "copies": 4},
    "B126": {"title": "Quantum Computing", "author": "PPP", "copies": 2},
    "B127": {"title": "Game Development", "author": "QQQ", "copies": 3},
    "B128": {"title": "Graphics", "author": "RRR", "copies": 6},
    "B129": {"title": "Human Computer Interaction", "author": "SSS", "copies": 2},
    "B130": {"title": "Ethical Hacking", "author": "TTT", "copies": 5}
}

# 1. Add a book
def add_book(library, bid, title, author, copies):
    library[bid] = {"title": title, "author": author, "copies": copies}

# 2. Remove a book
def remove_book(library, bid):
    if bid in library:
        del library[bid]

# 3. Search by ID
def search_by_id(library, bid):
    return library.get(bid, "Not Found")

# 4. Search by title
def search_by_title(library, title):
    return [info for info in library.values() if info["title"] == title]

# 5. Update copies
def update_copies(library, bid, copies):
    if bid in library:
        library[bid]["copies"] = copies

# 6. Issue a book
def issue_book(library, bid):
    if bid in library and library[bid]["copies"] > 0:
        library[bid]["copies"] -= 1
        return "Book issued successfully"
    return "Book not available"

# 7. Return a book
def return_book(library, bid):
    if bid in library:
        library[bid]["copies"] += 1

# 8. Books with fewer than 3 copies
def low_stock_books(library):
    return [info["title"] for info in library.values() if info["copies"] < 3]

# 9. Unavailable books
def unavailable_books(library):
    return [info["title"] for info in library.values() if info["copies"] == 0]

# 10. Most available book
def most_available(library):
    return max(library.items(), key=lambda x: x[1]["copies"])

# 11. Restocking report
def restocking_report(library):
    return {bid: info for bid, info in library.items() if info["copies"] < 3}

# 12. Immediate purchase (copies == 0)
def immediate_purchase(library):
    return {bid: info for bid, info in library.items() if info["copies"] == 0}

# Challenge: Library Summary Report
def library_report(library):
    print("=== Library Report ===")
    print("Total Books:", len(library))
    print("Unavailable Books:", unavailable_books(library))
    print("Low Stock Books:", low_stock_books(library))
    print("Most Available Book:", most_available(library))
    print("Restocking Report:", restocking_report(library))
    print("Immediate Purchase:", immediate_purchase(library))
    print("======================")

