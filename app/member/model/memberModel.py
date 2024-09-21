from db_connection import connect
from datetime import datetime

class MemberModel:
    def __init__(self):
        self.connection = connect
        
    # ! List Book
    def list_book(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT Books.book_id, Books.title, Books.author_name, Genre.genre_name
                    FROM Books
                    JOIN Genre ON Books.genre_id = Genre.genre_id;
                    """
                )
                results = cursor.fetchall()
                return results
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            
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
                result = cursor.fetchone()
                fine_count = result[0] if result else 0
                    
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