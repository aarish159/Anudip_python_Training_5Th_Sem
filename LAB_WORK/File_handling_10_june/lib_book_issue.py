# ---------------- Library Management System ----------------
# Problem: Manage books stored in books.txt with operations like
# display, search, issue, return, and restocking check.

# Function to load book data from file
def load_data():
    # Open file in read mode
    with open(r"C:\Users\aarish\OneDrive\Desktop\python Anudip Training\LAB_WORK\File_handling_10_june\books.txt", "r") as f:
        data = []
        for line in f:
            # Each line format: BookID,Title,Copies
            book_id, title, copies = line.strip().split(",")
            data.append((book_id, title, int(copies)))  # store as tuple
        return data

# Function to save updated book data back to file
def save_data(data):
    with open("books.txt", "w") as f:
        for book in data:
            f.write(f"{book[0]},{book[1]},{book[2]}\n")

# 1. Display all books
def display_all(data):
    print("\nAll Books:")
    for book in data:
        print(book)

# 2. Search book by Book ID
def search_book(data, book_id):
    for book in data:
        if book[0] == book_id:
            print("\nBook Found:", book)
            return
    print("\nBook ID not found!")

# 3. Issue a book (decrease quantity by 1 if available)
def issue_book(data, book_id):
    for i, book in enumerate(data):
        if book[0] == book_id:
            if book[2] > 0:  # check availability
                data[i] = (book[0], book[1], book[2] - 1)
                save_data(data)  # update file
                print("\nBook issued successfully!")
            else:
                print("\nBook unavailable!")
            return
    print("\nBook ID not found!")

# 4. Return a book (increase quantity by 1)
def return_book(data, book_id):
    for i, book in enumerate(data):
        if book[0] == book_id:
            data[i] = (book[0], book[1], book[2] + 1)
            save_data(data)  # update file
            print("\nBook returned successfully!")
            return
    print("\nBook ID not found!")

# 5. Display unavailable books (copies = 0)
def unavailable_books(data):
    print("\nUnavailable Books:")
    for book in data:
        if book[2] == 0:
            print(book)

# 6. Display books requiring restocking (copies < 2)
def restocking_books(data):
    print("\nBooks requiring restocking (copies < 2):")
    for book in data:
        if book[2] < 2:
            print(book)

# ------------------- MENU -------------------
while True:
    data = load_data()  # load fresh data each time
    print("\n--- Library Management System ---")
    print("1. Display All Books")
    print("2. Search Book by ID")
    print("3. Issue a Book")
    print("4. Return a Book")
    print("5. Display Unavailable Books")
    print("6. Display Books Requiring Restocking")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_all(data)
    elif choice == "2":
        book_id = input("Enter Book ID: ")
        search_book(data, book_id)
    elif choice == "3":
        book_id = input("Enter Book ID to issue: ")
        issue_book(data, book_id)
    elif choice == "4":
        book_id = input("Enter Book ID to return: ")
        return_book(data, book_id)
    elif choice == "5":
        unavailable_books(data)
    elif choice == "6":
        restocking_books(data)
    elif choice == "7":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
