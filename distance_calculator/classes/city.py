from dataclasses import dataclass
from math import radians, sin, cos, asin, sqrt


# Class to represent a city with its name and geographical coordinates.
# Attributes:
#   - name (str): The name of the city.
#   - lat (float): The latitude of the city.
#   - lon (float): The longitude of the city.
@dataclass
class City:
    name: str
    lat: float
    lon: float

    # Calculates the distance in kilometers to another city using the Haversine formula.
    # - Args: other (City): Another city object to calculate distance to.
    # - Returns: float: Distance in kilometers.
    def get_distance_to(self, other):
        R = 6371  # Define Earth radius

        # Convert coordinates into radians
        lat1, lat2 = radians(self.lat), radians(other.lat)
        lon1, lon2 = radians(self.lon), radians(other.lon)

        # Calculate difference between latitudes and longitudes
        dlat = lat1 - lat2
        dlon = lon1 - lon2

        # Calculate the distance between cities based on Havercine formula
        distance = 2 * R * asin(sqrt(sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2))
        return distance

    # Updates the latitude and longitude of the city in the database.
    # - Args: connection: A database connection object.
    def update_city_in_db(self, connection):
        with connection.cursor() as cursor:
            try:
                cursor.execute('UPDATE City SET lat = ?, lon = ? WHERE city_name LIKE ?',
                               (self.lat, self.lon, self.name))
                connection.commit()
                print(f'{self.name} coordinates were updated successfully: {self.lat}, {self.lon}')
            except Exception as e:
                print(f'Unexpected error appeared when updating city in database: {e}')
            return None

    # Inserts the city into the database.
    # - Args: connection: A database connection object.
    # - Returns: bool: True if insertion was successful, False otherwise.
    def write_city_to_db(self, connection):
        with connection.cursor() as cursor:
            try:
                cursor.execute('INSERT INTO City (city_name, lat, lon) VALUES (?, ?, ?)',
                               (self.name, self.lat, self.lon))
                connection.commit()
                return True
            except Exception as e:
                print(f'Unexpected error appeared when writing city into database: {e}')
                return False


# Retrieves a city from the database by name.
# Args:
# - city (str): The name of the city to search for.
# - connection: A database connection object.
# Returns: City/None: A City object if found, None otherwise.
def fetch_city_from_db(city, connection):
    with connection.cursor() as cursor:
        try:
            cursor.execute('SELECT * FROM City WHERE city_name LIKE ?', (city,))
            row = cursor.fetchone()
            if row is not None:
                return City(row.city_name, row.lat, row.lon)
        except Exception as e:
            print(f'Unexpected error appeared when fetching city from database: {e}')
        return None
