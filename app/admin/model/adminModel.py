from db_connection import connect
from datetime import datetime

class AdminModel:
    def __init__(self):
        self.connection = connect
        
    # TODO LIST
    # ! List Role
    def list_role(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT * FROM Roles
                    """)
                results = cursor.fetchall()
                return results
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
    # ! List User
    def list_user(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT Users.user_id, Users.username, Roles.role_name
                    FROM Users 
                    JOIN Roles ON Users.role_id = Roles.role_id;
                    """
                )
                results = cursor.fetchall()
                return results
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
    # ! List Book
    def list_book(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT Books.book_id, Books.title, Books.author_name, Genre.genre_name, Books.copies_available
                    FROM Books
                    JOIN Genre ON Books.genre_id = Genre.genre_id;
                    """
                )
                results = cursor.fetchall()
                return results
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
    # ! List Genre
    def list_genre(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT * FROM genre
                    """
                )
                results = cursor.fetchall()
                return results
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
    
    # ! List Borrow Book
    def list_borrow_book(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT BorrowedBooks.borrow_id,Users.username,books.title, BorrowedBooks.borrow_date, BorrowedBooks.due_date, BorrowedBooks.status
                    FROM BorrowedBooks
                    JOIN Users ON BorrowedBooks.user_id = Users.user_id
					JOIN Books ON BorrowedBooks.book_id = Books.book_id
                    """
                )
                results = cursor.fetchall()
                return results
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            
    
    # TODO SEARCH
    # ! Search User ID
    def search_user_by_id(self,id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT Users.user_id, Users.username, Roles.role_name
                    FROM Users
                    JOIN Roles ON Users.role_id = Roles.role_id
                    WHERE Users.user_id = %s
                    """,
                    (id,)
                )
                result = cursor.fetchone()
                return result
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
    # ! Search User Name
    def search_user_by_name(self,name):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT Users.user_id, Users.username, Roles.role_name
                    FROM Users
                    JOIN Roles ON Users.role_id = Roles.role_id
                    WHERE Users.username LIKE %s
                    """,
                    (f'%{name}%',)
                )
                results = cursor.fetchall()
                return results
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
    # ! Search Book ID
    def search_book_by_id(self,id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT Books.book_id, Books.title, Books.author_name, Genre.genre_name
                    FROM Books
                    JOIN Genre ON Books.genre_id = Genre.genre_id
                    WHERE Books.book_id = %s
                    """,
                    (id,)
                )
                result = cursor.fetchone()
                return result
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
    # ! Search To Check this user exist or not
    def user_exist(self, user_id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT * FROM Users WHERE user_id = %s;
                    """,
                    (user_id,)
                )
                return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error: {e}")
            return False
        
    def book_exist(self, book_id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT * FROM Books WHERE book_id = %s;
                    """,
                    (book_id,)
                )
                return cursor.fetchone() is not None
        except Exception as e:
            print(f"Error: {e}")
            return False

    # TODO UPDATE
    # ! Update All User Data
    def update_user_data(self, username, first_name, last_name, phone_number, user_id):
        try:
            if self.user_exist(user_id):
                with self.connection.cursor() as cursor:
                    cursor.execute(
                        """
                        UPDATE Users
                        SET username = %s, first_name = %s, last_name = %s, phone_number = %s
                        WHERE user_id = %s;
                        """,
                        (username, first_name, last_name, phone_number, user_id)
                    )
                    self.connection.commit()
                    return True
            else:
                return False
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
    # ! Upgrade User Role  
    def upgrade_role(self, role, id):
        try:
            if self.user_exist(id):
                with self.connection.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT role_id
                        FROM Users
                        WHERE user_id = %s;
                        """,
                        (id,)
                    )
                    current_role = cursor.fetchone()        
                    if current_role and current_role[0] == role:
                        print(f"User {id} already has the role {role}.")
                        return False
                    cursor.execute(
                        """
                        UPDATE Users
                        SET role_id = %s
                        WHERE user_id = %s;
                        """,
                        (role, id)
                    )
                    self.connection.commit()
                    return True
            else:
                return False
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
    # ! Change Book Genre  
    def change_genre(self, genre, id):
        try:
            if self.book_exist(id):
                with self.connection.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT genre_id
                        FROM Books
                        WHERE book_id = %s;
                        """,
                        (id,)
                    )
                    current_genre = cursor.fetchone()        
                    if current_genre and current_genre[0] == genre:
                        print(f"This book id {id} already {genre}.")
                        return False
                    cursor.execute(
                        """
                        UPDATE Books
                        SET genre_id = %s
                        WHERE book_id = %s;
                        """,
                        (genre, id)
                    )
                    self.connection.commit()
                    return True
            else:
                return False
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
    # ! Update Book
    def update_book_data(self, title, author_name, publisher_name, copies_available, year_of_publisher, book_id):
        try:
            if self.book_exist(book_id):
                with self.connection.cursor() as cursor:
                    cursor.execute(
                        """
                        UPDATE Books
                        SET title = %s, author_name = %s, publisher_name = %s, copies_available = %s, year_of_publisher = %s
                        WHERE book_id = %s;
                        """,
                        (title, author_name, publisher_name, copies_available, year_of_publisher, book_id)
                    )
                    self.connection.commit()
                    return True
            else:
                return False
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
    
    # TODO CREATE & ADD
    # ! Add New Book
    def create_book(self,title,author,publisher,copies,year,genre_id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO books (title,author_name,publisher_name,copies_available,year_of_publisher,created_at,genre_id)
                    VALUES (%s,%s,%s,%s,%s,NOW(),%s)
                    """,
                    (title,author,publisher,copies,year,genre_id)
                )
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
    
    # ! Borrow Book
    def borrow_book(self, user_id, book_id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT *
                    FROM Fines
                    WHERE user_id = %s AND status = 'Unpaid'
                    """,
                    (user_id,))
                fine_count = cursor.fetchone()[0]
                    
                if fine_count > 0:
                    print("User has unpaid fines and cannot borrow books.")
                    return False
                
                cursor.execute(
                    """
                    SELECT copies_available FROM Books
                    WHERE book_id = %s
                    """,
                    (book_id,))
                result = cursor.fetchone()
                if result and result[0] > 0:
                    cursor.execute(
                        """
                        INSERT INTO BorrowedBooks (user_id, book_id, borrow_date, due_date, return_date, status)
                        VALUES (%s, %s, NOW(), NOW() + INTERVAL '7 days',NULL, %s)
                        """,
                        (user_id, book_id, "Pending"))
                    cursor.execute(
                        """
                        UPDATE Books
                        SET copies_available = copies_available - 1
                        WHERE book_id = %s
                        """,
                        (book_id,))
                    self.connection.commit()
                    return True
                else:
                    return False
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False

    def return_book(self, borrow_id, user_id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT book_id, due_date, status
                    FROM BorrowedBooks
                    WHERE borrow_id = %s
                    """,
                    (borrow_id,)
                )
                result = cursor.fetchone()
                if result is None:
                    print("No borrowed book found with the given borrow_id!")
                    return False
                
                book_id, due_date,status = result
                
                if status == 'Returned' or status == 'Returned (Overdue)':
                    print("This book has already been returned.")
                    return False
                
                current_date = datetime.now().date()
                overdue = current_date > due_date
                
                cursor.execute(
                    """
                    UPDATE BorrowedBooks
                    SET return_date = %s, status = %s
                    WHERE borrow_id = %s
                    """,
                    (current_date, 'Returned' if not overdue else 'Returned (Overdue)', borrow_id)
                )
                
                cursor.execute(
                    """
                    UPDATE Books
                    SET copies_available = copies_available + 1
                    WHERE book_id = %s
                    """,
                    (book_id,)
                )
                
                if overdue:
                    fine_amount = (current_date - due_date).days * 1.00
                    cursor.execute(
                        """
                        INSERT INTO Fines (fine_date, amount, status, borrow_id, user_id)
                        VALUES (%s, %s, %s, %s, %s)
                        """,
                        (current_date, fine_amount, 'Unpaid', borrow_id, user_id)
                    )
                    
                    print(f"The book was returned late. A fine of ${fine_amount:.2f} has been recorded.")
                
                self.connection.commit()
                return True
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False

    def create_member(self, username, first_name, last_name, email, password, phone_number):

        try:
            with self.connection.cursor() as cursor:
                    cursor.execute(
                    """
                    INSERT INTO users (username, first_name, last_name, email, password, phone_number, membership_date, role_id)
                    VALUES (%s, %s, %s, %s, %s, %s, NOW(),%s)
                    """,
                    (username, first_name, last_name, email, password, phone_number,3)
                )
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
        
    def create_librarian(self, username, first_name, last_name, email, password, phone_number):
        try:
            with self.connection.cursor() as cursor:
                    cursor.execute(
                    """
                    INSERT INTO users (username, first_name, last_name, email, password, phone_number, membership_date, role_id)
                    VALUES (%s, %s, %s, %s, %s, %s, NOW(),%s)
                    """,
                    (username, first_name, last_name, email, password, phone_number,2)
                )
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False

    
    # TODO REMOVE
    # ! Remove Book 
    def remove_book(self,id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    DELETE FROM books WHERE book_id = %s      
                    """,
                    (id)
                )
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
    # ! Remove User
    def remove_user(self,id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    DELETE FROM users WHERE user_id = %s      
                    """,
                    (id)
                )
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False
        
    def remove_borrow_book(self,id):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    DELETE FROM borrowedbooks WHERE borrow_id = %s      
                    """,
                    (id)
                )
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            return False