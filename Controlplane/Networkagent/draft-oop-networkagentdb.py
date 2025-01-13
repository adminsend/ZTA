import sqlite3

class ObjectDatabaseManager:
    def __init__(self, db_name="objects.db"):
        """Initialize the database manager with a connection to the database."""
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create tables in the database if they don't already exist."""
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ObjectID (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ObjectIntegrity (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                object_id INTEGER NOT NULL,
                checksum TEXT NOT NULL,
                FOREIGN KEY (object_id) REFERENCES ObjectID (id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ObjectAuthToken (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                object_id INTEGER NOT NULL,
                auth_token TEXT NOT NULL,
                FOREIGN KEY (object_id) REFERENCES ObjectID (id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ObjectAddlData (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                object_id INTEGER NOT NULL,
                additional_data TEXT,
                FOREIGN KEY (object_id) REFERENCES ObjectID (id)
            )
        ''')
        self.conn.commit()

    def insert_object(self, name):
        """Insert a new object into the ObjectID table."""
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO ObjectID (name) VALUES (?)", (name,))
        self.conn.commit()
        return cursor.lastrowid

    def insert_integrity(self, object_id, checksum):
        """Insert an integrity record into the ObjectIntegrity table."""
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO ObjectIntegrity (object_id, checksum) VALUES (?, ?)", (object_id, checksum))
        self.conn.commit()

    def insert_auth_token(self, object_id, auth_token):
        """Insert an auth token record into the ObjectAuthToken table."""
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO ObjectAuthToken (object_id, auth_token) VALUES (?, ?)", (object_id, auth_token))
        self.conn.commit()

    def insert_additional_data(self, object_id, additional_data):
        """Insert additional data into the ObjectAddlData table."""
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO ObjectAddlData (object_id, additional_data) VALUES (?, ?)", (object_id, additional_data))
        self.conn.commit()

    def fetch_all_objects(self):
        """Fetch all objects and their details."""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT 
                ObjectID.id, 
                ObjectID.name, 
                ObjectIntegrity.checksum, 
                ObjectAuthToken.auth_token, 
                ObjectAddlData.additional_data 
            FROM ObjectID
            LEFT JOIN ObjectIntegrity ON ObjectID.id = ObjectIntegrity.object_id
            LEFT JOIN ObjectAuthToken ON ObjectID.id = ObjectAuthToken.object_id
            LEFT JOIN ObjectAddlData ON ObjectID.id = ObjectAddlData.object_id
        ''')
        return cursor.fetchall()

    def fetch_object_by_id(self, object_id):
        """Fetch a single object and its details by object_id."""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT 
                ObjectID.id, 
                ObjectID.name, 
                ObjectIntegrity.checksum, 
                ObjectAuthToken.auth_token, 
                ObjectAddlData.additional_data 
            FROM ObjectID
            LEFT JOIN ObjectIntegrity ON ObjectID.id = ObjectIntegrity.object_id
            LEFT JOIN ObjectAuthToken ON ObjectID.id = ObjectAuthToken.object_id
            LEFT JOIN ObjectAddlData ON ObjectID.id = ObjectAddlData.object_id
            WHERE ObjectID.id = ?
        ''', (object_id,))
        return cursor.fetchone()

    def close_connection(self):
        """Close the database connection."""
        self.conn.close()

if __name__ == "__main__":
    db_manager = ObjectDatabaseManager()

    # Insert example data
    object_id = db_manager.insert_object("SampleObject")
    db_manager.insert_integrity(object_id, "123abc")
    db_manager.insert_auth_token(object_id, "token123")
    db_manager.insert_additional_data(object_id, "Some additional data")

    # Fetch and display all objects
    objects = db_manager.fetch_all_objects()
    for obj in objects:
        print(obj)

    # Fetch and display a single object by ID
    single_object = db_manager.fetch_object_by_id(object_id)
    print("Single object fetched by ID:", single_object)

    # Close the connection
    db_manager.close_connection()
