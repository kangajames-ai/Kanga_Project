"""
Unit tests for Library Management System
"""
import operations

def test_add_book():
    """Test adding books functionality"""
    print("Testing add_book()...")
    
    # Clear existing data
    operations.books.clear()
    
    # Test 1: Add valid book
    success, message = operations.add_book("TEST-001", "Test Book", "Test Author", "Fiction", 5)
    assert success == True, "Should successfully add valid book"
    assert "TEST-001" in operations.books, "Book should be in dictionary"
    
    # Test 2: Add duplicate ISBN
    success, message = operations.add_book("TEST-001", "Another Book", "Another Author", "Sci-Fi", 3)
    assert success == False, "Should fail to add duplicate ISBN"
    
    # Test 3: Add book with invalid genre
    success, message = operations.add_book("TEST-002", "Invalid Genre Book", "Author", "Invalid-Genre", 2)
    assert success == False, "Should fail with invalid genre"
    
    print("✓ add_book() tests passed")

def test_borrow_book_limits():
    """Test borrowing limits and availability"""
    print("Testing borrow_book() limits...")
    
    # Clear data and setup
    operations.books.clear()
    operations.members.clear()
    
    # Add test book and member
    operations.add_book("TEST-BORROW", "Borrow Test", "Test Author", "Fiction", 2)
    operations.add_member("TEST-MEMBER", "Test Member", "test@email.com")
    
    # Test 1: Successful borrow
    success, message = operations.borrow_book("TEST-MEMBER", "TEST-BORROW")
    assert success == True, "Should successfully borrow available book"
    assert operations.books["TEST-BORROW"]['available_copies'] == 1, "Available copies should decrease"
    
    # Test 2: Borrow same book again
    success, message = operations.borrow_book("TEST-MEMBER", "TEST-BORROW")
    assert success == False, "Should fail to borrow same book twice"
    
    # Add more books for limit testing
    operations.add_book("TEST-2", "Book 2", "Author", "Fiction", 1)
    operations.add_book("TEST-3", "Book 3", "Author", "Fiction", 1)
    operations.add_book("TEST-4", "Book 4", "Author", "Fiction", 1)
    
    # Borrow up to limit
    operations.borrow_book("TEST-MEMBER", "TEST-2")
    operations.borrow_book("TEST-MEMBER", "TEST-3")
    
    # Test 3: Try to borrow fourth book
    success, message = operations.borrow_book("TEST-MEMBER", "TEST-4")
    assert success == False, "Should fail to borrow more than 3 books"
    
    print("✓ borrow_book() limit tests passed")

def test_return_book():
    """Test returning books functionality"""
    print("Testing return_book()...")
    
    # Setup
    operations.books.clear()
    operations.members.clear()
    
    operations.add_book("TEST-RETURN", "Return Test", "Author", "Fiction", 3)
    operations.add_member("TEST-RETURNER", "Returner", "return@email.com")
    
    # Borrow then return
    operations.borrow_book("TEST-RETURNER", "TEST-RETURN")
    initial_copies = operations.books["TEST-RETURN"]['available_copies']
    
    success, message = operations.return_book("TEST-RETURNER", "TEST-RETURN")
    assert success == True, "Should successfully return book"
    assert operations.books["TEST-RETURN"]['available_copies'] == initial_copies + 1, "Available copies should increase"
    
    # Test returning non-borrowed book
    success, message = operations.return_book("TEST-RETURNER", "TEST-RETURN")
    assert success == False, "Should fail to return non-borrowed book"
    
    print("✓ return_book() tests passed")

def test_delete_protections():
    """Test deletion protections"""
    print("Testing deletion protections...")
    
    operations.books.clear()
    operations.members.clear()
    
    # Add book and member with borrowed book
    operations.add_book("TEST-DELETE", "Delete Test", "Author", "Fiction", 1)
    operations.add_member("TEST-DELETER", "Deleter", "delete@email.com")
    operations.borrow_book("TEST-DELETER", "TEST-DELETE")
    
    # Test 1: Try to delete book with borrowed copies
    success, message = operations.delete_book("TEST-DELETE")
    assert success == False, "Should fail to delete borrowed book"
    
    # Test 2: Try to delete member with borrowed books
    success, message = operations.delete_member("TEST-DELETER")
    assert success == False, "Should fail to delete member with borrowed books"
    
    # Return book and test successful deletion
    operations.return_book("TEST-DELETER", "TEST-DELETE")
    success, message = operations.delete_book("TEST-DELETE")
    assert success == True, "Should successfully delete returned book"
    
    print("✓ deletion protection tests passed")

def test_search_functionality():
    """Test book search functionality"""
    print("Testing search_book()...")
    
    operations.books.clear()
    
    # Add test books
    operations.add_book("SEARCH-1", "Python Programming", "John Developer", "Non-Fiction", 2)
    operations.add_book("SEARCH-2", "Advanced Python", "Jane Coder", "Non-Fiction", 1)
    operations.add_book("SEARCH-3", "Java Guide", "John Developer", "Non-Fiction", 1)
    
    # Test title search
    results = operations.search_book("Python")
    assert len(results) == 2, "Should find 2 Python books"
    
    # Test author search
    results = operations.search_book("John Developer")
    assert len(results) == 2, "Should find 2 books by John Developer"
    
    # Test case insensitive search
    results = operations.search_book("python")
    assert len(results) == 2, "Should be case insensitive"
    
    print("✓ search_book() tests passed")

def run_all_tests():
    """Run all unit tests"""
    print("RUNNING LIBRARY MANAGEMENT SYSTEM TESTS")
    print("=" * 50)
    
    test_add_book()
    test_borrow_book_limits()
    test_return_book()
    test_delete_protections()
    test_search_functionality()
    
    print("=" * 50)
    print("🎉 ALL TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    run_all_tests()