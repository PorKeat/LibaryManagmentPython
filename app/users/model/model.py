from db_connection import connect
import hashlib


class UserModel:
    def __init__(self) -> None:
        self.connection = connect
        
    def register(self, username, first_name, last_name, email, password, phone_number,role):
        try:
            with self.connection.cursor() as cursor:
                    cursor.execute(
                    """
                    INSERT INTO users (username, first_name, last_name, email, password, phone_number, membership_date, role_id)
                    VALUES (%s, %s, %s, %s, %s, %s, NOW(),%s)
                    """,
                    (username, first_name, last_name, email, password, phone_number,role)
                )
            self.connection.commit()
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
            
    def login(self, email, password):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                """
                SELECT * FROM users WHERE email = %s AND password = %s
                """,
                (email, password)
                )
                results = cursor.fetchone()
                if results:
                    print("Successfully")
                    print("User Success:", results)
                else:
                    print("Fail")
                    print("User Fail:", results)
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()