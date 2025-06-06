import sqlite3
import pyodbc


# Function to create the city_storage database and fill it with few default cities.
# Parameters:
# - db_path (str): the path to a SQLite database, used by sqlite3 to open (or create) a SQLite database at that path.
# - db_conn (str): the connection string used by pyodbc to connect to a particular database.
def create_city_storage_db(db_path, db_conn):
    connection = sqlite3.connect(db_path)
    connection.close()
    conn = pyodbc.connect(db_conn)
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS City')
    cursor.execute('''
    CREATE TABLE
      IF NOT EXISTS City (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        city_name   VARCHAR(100) NOT NULL,
        lat         FLOAT NOT NULL,
        lon         FLOAT NOT NULL,
        UNIQUE(city_name)
    );''')
    cursor.executemany('INSERT INTO City (city_name, lat, lon) VALUES (?, ?, ?)',
                   [
                   ('Minsk', 53.9006, 27.5590),
                   ('Tbilisi', 41.6971, 44.7736),
                   ('Vilnius', 54.6892, 25.2798),
                   ('Warsaw', 52.2298, 21.0118),
                   ('Moscow', 55.7522, 37.6156),
                   ('New York', 40.7128, -74.0060),
                   ('London', 51.5074, -0.1278),
                   ('Paris', 48.8566, 2.3522),
                   ('Berlin', 52.5200, 13.4049),
                   ('Tokyo',  35.6762, 139.6503),
                   ('Sydney', -33.8688, 151.2093),
                   ('Beijing', 39.9042, 116.4074),
                   ('Rome', 41.9028, 12.4964)
                   ])
    # cursor.execute('SELECT * FROM City')
    # for row in cursor.fetchall():
    #     print(row.id, row.city_name, row.lat, row.lon)
    cursor.close()
    conn.commit()

