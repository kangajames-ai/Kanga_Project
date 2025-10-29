"""
Demo script showing Library Management System usage
"""
from operations import *

def main():
    print("=== LIBRARY MANAGEMENT SYSTEM DEMO ===\n")
    
    # 1. Add books
    print("1. ADDING BOOKS")
    print("-" * 30)
    
    books_to_add = [
        ("978-0451524935", "1984", "George Orwell", "Fiction", 5),
        ("978-0061120084", "To Kill a Mockingbird", "Harper Lee", "Fiction", 3),
        ("978-0544003415", "The Lord of the Rings", "J.R.R. Tolkien", "Fantasy", 4),
        ("978-1451673319", "Fahrenheit 451", "Ray Bradbury", "Sci-Fi", 3),
        ("978-0141439518", "Pride and Prejudice", "Jane Austen", "Fiction", 2)
    ]
    
    for book in books_to_add:
        success, message = add_book(*book)
        print(f"Adding '{book[1]}': {message}")
    
    print(f"\nTotal books in library: {len(books)}")
    
    # 2. Add members
    print("\n2. ADDING MEMBERS")
    print("-" * 30)
    
    members_to_add = [
        ("M001", "John Smith", "john.smith@email.com"),
        ("M002", "Sarah Johnson", "sarah.j@email.com"),
        ("M003", "Mike Brown", "mike.brown@email.com")
    ]
    
    for member in members_to_add:
        success, message = add_member(*member)
        print(f"Adding '{member[1]}': {message}")
    
    print(f"\nTotal members: {len(members)}")
    
    # 3. Search for books
    print("\n3. SEARCHING FOR BOOKS")
    print("-" * 30)
    
    search_terms = ["Tolkien", "fiction", "451"]
    for term in search_terms:
        results = search_book(term)
        print(f"Search for '{term}': Found {len(results)} results")
        for isbn, book in results:
            print(f"  - {book['title']} by {book['author']}")
    
    # 4. Borrow books
    print("\n4. BORROWING BOOKS")
    print("-" * 30)
    
    borrow_actions = [
        ("M001", "978-0451524935"),  # John borrows 1984
        ("M001", "978-0061120084"),  # John borrows To Kill a Mockingbird
        ("M002", "978-0544003415"),  # Sarah borrows Lord of the Rings
        ("M001", "978-1451673319"),  # John borrows Fahrenheit 451 (3rd book)
        ("M001", "978-0141439518"),  # John tries to borrow 4th book (should fail)
    ]
    
    for member_id, isbn in borrow_actions:
        success, message = borrow_book(member_id, isbn)
        book_title = books[isbn]['title'] if isbn in books else "Unknown"
        print(f"{members[0]['name'] if member_id == 'M001' else members[1]['name']} borrowing '{book_title}': {message}")
    
    # 5. Display current status
    print("\n5. CURRENT LIBRARY STATUS")
    print("-" * 30)
    
    print("Books:")
    for isbn, book in books.items():
        print(f"  - {book['title']}: {book['available_copies']}/{book['total_copies']} available")
    
    print("\nMembers and their borrowed books:")
    for member in members:
        borrowed_titles = [books[isbn]['title'] for isbn in member['borrowed_books'] if isbn in books]
        print(f"  - {member['name']}: {borrowed_titles}")
    
    # 6. Return books
    print("\n6. RETURNING BOOKS")
    print("-" * 30)
    
    return_actions = [
        ("M001", "978-0061120084"),  # John returns To Kill a Mockingbird
        ("M002", "978-0544003415"),  # Sarah returns Lord of the Rings
    ]
    
    for member_id, isbn in return_actions:
        success, message = return_book(member_id, isbn)
        book_title = books[isbn]['title']
        member_name = next((m['name'] for m in members if m['member_id'] == member_id), "Unknown")
        print(f"{member_name} returning '{book_title}': {message}")
    
    # 7. Update operations
    print("\n7. UPDATING RECORDS")
    print("-" * 30)
    
    # Update book
    success, message = update_book("978-0451524935", total_copies=6)
    print(f"Updating '1984' copies to 6: {message}")
    
    # Update member
    success, message = update_member("M001", email="john.smith.new@email.com")
    print(f"Updating John's email: {message}")
    
    # 8. Final status
    print("\n8. FINAL LIBRARY STATUS")
    print("-" * 30)
    
    print("Books:")
    for isbn, book in books.items():
        print(f"  - {book['title']}: {book['available_copies']}/{book['total_copies']} available")
    
    print("\nDemo completed successfully!")

if __name__ == "__main__":
    main()