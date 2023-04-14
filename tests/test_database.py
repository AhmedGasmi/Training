import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
        """
        self.conn.execute(query)

    def insert_user(self, name, age):
        query = f"INSERT INTO users (name, age) VALUES ('{name}', {age})"
        self.conn.execute(query)
        self.conn.commit()

    def get_users(self):
        query = "SELECT * FROM users"
        return self.conn.execute(query).fetchall()

def test_database():
    # Create a test database
    db = Database(":memory:")

    # Test the create_table method
    db.create_table()
    query = "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
    assert len(db.conn.execute(query).fetchall()) == 1

    # Test the insert_user method
    db.insert_user("Alice", 25)
    db.insert_user("Bob", 30)
    assert len(db.get_users()) == 2

    # Test the get_users method
    users = db.get_users()
    assert users[0] == (1, "Alice", 25)
    assert users[1] == (2, "Bob", 30)