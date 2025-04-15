import sqlite3
import pyodbc


# Function to create the posts_storage database and fill it with few default cities.
# Parameters:
# - db_path (str): the path to a SQLite database, used by sqlite3 to open (or create) a SQLite database at that path.
# - db_conn (str): the connection string used by pyodbc to connect to a particular database.
def create_posts_db(db_path, db_conn):
    connection = sqlite3.connect(db_path)
    connection.close()
    conn = pyodbc.connect(db_conn)
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS PostTypes;')
    cursor.execute('DROP TABLE IF EXISTS Posts;')
    cursor.execute('DROP TABLE IF EXISTS News;')
    cursor.execute('DROP TABLE IF EXISTS PrivateAd;')
    cursor.execute('DROP TABLE IF EXISTS Rumor;')
    cursor.execute('''
    CREATE TABLE
      IF NOT EXISTS PostTypes (
        type_id     INTEGER PRIMARY KEY AUTOINCREMENT,
        type_name   VARCHAR(20) NOT NULL
        );

    CREATE TABLE
      IF NOT EXISTS Posts (
        post_id     INTEGER PRIMARY KEY AUTOINCREMENT,
        type_id     INTEGER NOT NULL,
        create_date DATETIME NOT NULL,
        FOREIGN KEY (type_id) REFERENCES PostTypes(type_id)
        );

    CREATE TABLE
      IF NOT EXISTS News (
        news_id     INTEGER PRIMARY KEY AUTOINCREMENT,
        post_id     INTEGER NOT NULL,
        text        VARCHAR(500) NOT NULL,
        city        VARCHAR(50) NOT NULL,
        FOREIGN KEY (post_id) REFERENCES Posts(post_id)
        );

    CREATE TABLE
      IF NOT EXISTS PrivateAd (
        ad_id       INTEGER PRIMARY KEY AUTOINCREMENT,
        post_id     INTEGER NOT NULL,
        text        VARCHAR(500) NOT NULL,
        expiry_date DATETIME NOT NULL,
        FOREIGN KEY (post_id) REFERENCES Posts(post_id)
        );

    CREATE TABLE
      IF NOT EXISTS Rumor (
        rumor_id    INTEGER PRIMARY KEY AUTOINCREMENT,
        post_id     INTEGER NOT NULL,
        text        VARCHAR(500) NOT NULL,
        celebrity   VARCHAR(50) NOT NULL,
        FOREIGN KEY (post_id) REFERENCES Posts(post_id)
        );
    ''')
    sql = 'INSERT INTO PostTypes (type_name) VALUES (?)'
    post_types_data = [
        ('News',),
        ('Private Ad',),
        ('Rumor',)
    ]
    cursor.executemany(sql, post_types_data)
    conn.commit()
    cursor.close()
    conn.close()


def fetch_posts_from_db(db_conn):
    conn = pyodbc.connect(db_conn)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM PostTypes')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.execute('SELECT * FROM News')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.execute('SELECT * FROM Rumor')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.execute('SELECT * FROM PrivateAd')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()
