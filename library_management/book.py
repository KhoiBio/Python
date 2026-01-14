def display_menu():
    print('\n--- Library Management System ---')
    print('1. Book Management')
    print('2. Borrower Management')
    print('3. Transaction Management')
    print('4. Exit')

def display_book_menu():
    print('\n--- Book Management ---')
    print('1. Add Book')
    print('2. Update Book')
    print('3. Delete Book')
    print('4. Search Book')
    print('5. View All Books')
    print('6. Back to Main Menu')

def display_borrower_menu():
    print('\n--- Borrower Management ---')
    print('1. Add Borrower')
    print('2. Update Borrower')
    print('3. Delete Borrower')
    print('4. View All Borrowers')
    print('5. Back to Main Menu')

def display_transaction_menu():
    print('\n--- Transaction Management ---')
    print('1. Borrow Book')
    print('2. Return Book')
    print('3. View All Transactions')
    print('4. Back to Main Menu')

def add_book(books):
    book_id = input('Enter Book ID: ')
    
    for book in books:
        if book['id'] == book_id:
            print('Book ID already exists!')
            return
    
    title = input('Enter Title: ')
    author = input('Enter Author: ')
    genre = input('Enter Genre: ')
    
    book = {
        'id': book_id,
        'title': title,
        'author': author,
        'genre': genre,
        'status': 'available'
    }
    
    books.append(book)
    print('Book added successfully!')

def update_book(books):
    book_id = input('Enter Book ID to update: ')
    
    for book in books:
        if book['id'] == book_id:
            print(f"Current Title: {book['title']}")
            new_title = input('Enter new Title (or press Enter to skip): ')
            if new_title:
                book['title'] = new_title
            
            print(f"Current Author: {book['author']}")
            new_author = input('Enter new Author (or press Enter to skip): ')
            if new_author:
                book['author'] = new_author
            
            print(f"Current Genre: {book['genre']}")
            new_genre = input('Enter new Genre (or press Enter to skip): ')
            if new_genre:
                book['genre'] = new_genre
            
            print('Book updated successfully!')
            return
    
    print('Book not found!')

def delete_book(books):
    book_id = input('Enter Book ID to delete: ')
    
    for i, book in enumerate(books):
        if book['id'] == book_id:
            books.pop(i)
            print('Book deleted successfully!')
            return
    
    print('Book not found!')

def search_book(books):
    print('\nSearch by:')
    print('1. Title')
    print('2. Author')
    print('3. Genre')
    choice = input('Enter choice: ')
    
    search_term = input('Enter search term: ').lower()
    results = []
    
    if choice == '1':
        results = [book for book in books if search_term in book['title'].lower()]
    elif choice == '2':
        results = [book for book in books if search_term in book['author'].lower()]
    elif choice == '3':
        results = [book for book in books if search_term in book['genre'].lower()]
    
    if results:
        print('\nSearch Results:')
        for book in results:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Status: {book['status']}")
    else:
        print('No books found!')

def view_all_books(books):
    if not books:
        print('No books in the library!')
        return
    
    print('\n--- All Books ---')
    for book in books:
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Status: {book['status']}")

def add_borrower(borrowers):
    borrower_id = input('Enter Borrower ID: ')
    
    for borrower in borrowers:
        if borrower['id'] == borrower_id:
            print('Borrower ID already exists!')
            return
    
    name = input('Enter Name: ')
    email = input('Enter Email: ')
    phone = input('Enter Phone: ')
    
    borrower = {
        'id': borrower_id,
        'name': name,
        'email': email,
        'phone': phone
    }
    
    borrowers.append(borrower)
    print('Borrower added successfully!')

def update_borrower(borrowers):
    borrower_id = input('Enter Borrower ID to update: ')
    
    for borrower in borrowers:
        if borrower['id'] == borrower_id:
            print(f"Current Name: {borrower['name']}")
            new_name = input('Enter new Name (or press Enter to skip): ')
            if new_name:
                borrower['name'] = new_name
            
            print(f"Current Email: {borrower['email']}")
            new_email = input('Enter new Email (or press Enter to skip): ')
            if new_email:
                borrower['email'] = new_email
            
            print(f"Current Phone: {borrower['phone']}")
            new_phone = input('Enter new Phone (or press Enter to skip): ')
            if new_phone:
                borrower['phone'] = new_phone
            
            print('Borrower updated successfully!')
            return
    
    print('Borrower not found!')

def delete_borrower(borrowers):
    borrower_id = input('Enter Borrower ID to delete: ')
    
    for i, borrower in enumerate(borrowers):
        if borrower['id'] == borrower_id:
            borrowers.pop(i)
            print('Borrower deleted successfully!')
            return
    
    print('Borrower not found!')

def view_all_borrowers(borrowers):
    if not borrowers:
        print('No borrowers registered!')
        return
    
    print('\n--- All Borrowers ---')
    for borrower in borrowers:
        print(f"ID: {borrower['id']}, Name: {borrower['name']}, Email: {borrower['email']}, Phone: {borrower['phone']}")

def borrow_book(books, borrowers, transactions):
    book_id = input('Enter Book ID to borrow: ')
    borrower_id = input('Enter Borrower ID: ')
    
    book_found = None
    for book in books:
        if book['id'] == book_id:
            book_found = book
            break
    
    if not book_found:
        print('Book not found!')
        return
    
    if book_found['status'] == 'borrowed':
        print('Book is already borrowed!')
        return
    
    borrower_found = None
    for borrower in borrowers:
        if borrower['id'] == borrower_id:
            borrower_found = borrower
            break
    
    if not borrower_found:
        print('Borrower not found!')
        return
    
    book_found['status'] = 'borrowed'
    
    transaction = {
        'book_id': book_id,
        'book_title': book_found['title'],
        'borrower_id': borrower_id,
        'borrower_name': borrower_found['name'],
        'type': 'borrowed'
    }
    
    transactions.append(transaction)
    print('Book borrowed successfully!')

def return_book(books, transactions):
    book_id = input('Enter Book ID to return: ')
    
    book_found = None
    for book in books:
        if book['id'] == book_id:
            book_found = book
            break
    
    if not book_found:
        print('Book not found!')
        return
    
    if book_found['status'] == 'available':
        print('Book is not currently borrowed!')
        return
    
    book_found['status'] = 'available'
    
    transaction = {
        'book_id': book_id,
        'book_title': book_found['title'],
        'borrower_id': 'N/A',
        'borrower_name': 'N/A',
        'type': 'returned'
    }
    
    transactions.append(transaction)
    print('Book returned successfully!')

def view_all_transactions(transactions):
    if not transactions:
        print('No transactions recorded!')
        return
    
    print('\n--- All Transactions ---')
    for transaction in transactions:
        print(f"Book ID: {transaction['book_id']}, Title: {transaction['book_title']}, Borrower: {transaction['borrower_name']}, Type: {transaction['type']}")

def book_management(books):
    while True:
        display_book_menu()
        choice = input('Enter choice: ')
        
        if choice == '1':
            add_book(books)
        elif choice == '2':
            update_book(books)
        elif choice == '3':
            delete_book(books)
        elif choice == '4':
            search_book(books)
        elif choice == '5':
            view_all_books(books)
        elif choice == '6':
            break
        else:
            print('Invalid choice!')

def borrower_management(borrowers):
    while True:
        display_borrower_menu()
        choice = input('Enter choice: ')
        
        if choice == '1':
            add_borrower(borrowers)
        elif choice == '2':
            update_borrower(borrowers)
        elif choice == '3':
            delete_borrower(borrowers)
        elif choice == '4':
            view_all_borrowers(borrowers)
        elif choice == '5':
            break
        else:
            print('Invalid choice!')

def transaction_management(books, borrowers, transactions):
    while True:
        display_transaction_menu()
        choice = input('Enter choice: ')
        
        if choice == '1':
            borrow_book(books, borrowers, transactions)
        elif choice == '2':
            return_book(books, transactions)
        elif choice == '3':
            view_all_transactions(transactions)
        elif choice == '4':
            break
        else:
            print('Invalid choice!')

def main():
    books = []
    borrowers = []
    transactions = []
    
    while True:
        display_menu()
        choice = input('Enter choice: ')
        
        if choice == '1':
            book_management(books)
        elif choice == '2':
            borrower_management(borrowers)
        elif choice == '3':
            transaction_management(books, borrowers, transactions)
        elif choice == '4':
            print('Thank you for using the Library Management System!')
            break
        else:
            print('Invalid choice!')

if __name__ == '__main__':
    main()