# Mini Library Management System

A Python-based library management system implementing core CRUD operations for books and members.

## Project Structure

library_management/
├── operations.py # Core functions and data structures
├── demo.py # Demonstration script
├── tests.py # Unit tests
├── DesignRationale.md
└── README.md


# Quick Start

## Prerequisites
- Python 3.6 or higher
- No additional packages required (uses only built-in Python libraries)

Step-by-Step Instructions

1. Download the Files
First, ensure you have all the required Python files in the same directory:
- operations.py
- demo.py 
- tests.py

2. Run the Demonstration Script
To see the system in action with sample data:

'''Bash'''
python demo.py

This will execute a complete demo showing:

- Adding books and members
- Searching for books
- Borrowing and returning books
- Updating records
- System status display

3. Run the Unit Tests
To verify all functionality works correctly:

'''Bash'''
python tests.py

This will run 5 comprehensive tests including:

- Adding books with validation
- Borrowing limits enforcement
- Return book functionality
- Deletion protections
- Search functionality

4. Use in Your Own Code
You can import and use the system in your own Python scripts:
# Import the library system
from operations import *

# Initialize with some data
add_book("978-0451524935", "1984", "George Orwell", "Fiction", 5)
add_member("M001", "John Smith", "john@email.com")

# Perform operations
borrow_book("M001", "978-0451524935")
search_results = search_book("Orwell")

Sample Output
When you run demo.py, you'll see output like:

text
=== LIBRARY MANAGEMENT SYSTEM DEMO ===

1. ADDING BOOKS
------------------------------
Adding '1984': Book added successfully
Adding 'To Kill a Mockingbird': Book added successfully
...

Total books in library: 5

2. ADDING MEMBERS
------------------------------
Adding 'John Smith': Member added successfully
...