import sqlite3

def connect_to_database(db_name="objects.db"):
    """Connect to the SQLite database or create it if it doesn't exist."""
    conn = sqlite3.connect(db_name)
    return conn

def create_tables(conn):
    """Create tables in the database if they don't already exist."""
    cursor = conn.cursor()
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
    conn.commit()

def insert_object(conn, name):
    """Insert a new object into the ObjectID table."""
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ObjectID (name) VALUES (?)", (name,))
    conn.commit()
    return cursor.lastrowid

def insert_integrity(conn, object_id, checksum):
    """Insert an integrity record into the ObjectIntegrity table."""
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ObjectIntegrity (object_id, checksum) VALUES (?, ?)", (object_id, checksum))
    conn.commit()

def insert_auth_token(conn, object_id, auth_token):
    """Insert an auth token record into the ObjectAuthToken table."""
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ObjectAuthToken (object_id, auth_token) VALUES (?, ?)", (object_id, auth_token))
    conn.commit()

def insert_additional_data(conn, object_id, additional_data):
    """Insert additional data into the ObjectAddlData table."""
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ObjectAddlData (object_id, additional_data) VALUES (?, ?)", (object_id, additional_data))
    conn.commit()

def fetch_all_objects(conn):
    """Fetch all objects and their details."""
    cursor = conn.cursor()
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

def fetch_object_by_id(conn, object_id):
    """Fetch a single object and its details by object_id."""
    cursor = conn.cursor()
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

def main():
    """Main function to demonstrate functionality."""
    conn = connect_to_database()
    create_tables(conn)

    # Insert example data
    object_id = insert_object(conn, "SampleObject")
    insert_integrity(conn, object_id, "123abc")
    insert_auth_token(conn, object_id, "token123")
    insert_additional_data(conn, object_id, "Some additional data")

    # Fetch and display all objects
    objects = fetch_all_objects(conn)
    for obj in objects:
        print(obj)

    # Fetch and display a single object by ID
    single_object = fetch_object_by_id(conn, object_id)
    print("Single object fetched by ID:", single_object)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
