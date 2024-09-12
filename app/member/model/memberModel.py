from db_connection import connect

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