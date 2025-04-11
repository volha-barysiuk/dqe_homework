import sys
import pyodbc

from classes.city import City, fetch_city_from_db
from resources import utils
from db_setup import DB_CONN


# Decorator that prompts the user to try again if an exception occurred during input
def try_again_prompt(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(e)
                # Ask user if they want to retry the operation
                answer = input('\nDo you want to try again? (Y/N): ')
                if answer.upper() == 'Y':
                    continue
                else:
                    sys.exit()

    return wrapper


# Function that prompts user for input (city or its coordinates) and validates entered value using the provided method.
@try_again_prompt
def input_params(prompt_text, validation_method):
    return validation_method(input(prompt_text).strip().title())


# Function that handles the complete city input process:
# - Checks if the entered city exists in the database.
#   - If it doesn't exist, prompts the user to enter coordinates.
#   - If it does exist, displays the current coordinates and asks the user
#     whether to use the existing data or update it with new values.
def input_city_details(connection):
    # Ask user to input city name and validate it
    city_name = input_params(prompt_text='\nEnter the city: ', validation_method=utils.validate_city)

    # Try to fetch the city from the database
    city = fetch_city_from_db(city_name, connection)

    if city is not None:
        # City already exists — ask user if they want to update it
        print(f'{city.name} already exists in database with coordinates: ({city.lat}, {city.lon})')
        answer = input('Do you want to update the coordinates? (Y/N): ')
        if answer.upper() == 'Y':
            # Prompt for new coordinates with validation
            lat = input_params(prompt_text='Enter latitude: ',
                               validation_method=lambda x: utils.validate_coordinate(x, coord_type='lat'))
            lon = input_params(prompt_text='Enter longitude: ',
                               validation_method=lambda x: utils.validate_coordinate(x, coord_type='lon'))
            city.lat, city.lon = lat, lon
            city.update_city_in_db(connection)
    else:
        # City doesn't exist — create a new one and write it to DB
        lat = input_params(prompt_text='Enter latitude: ',
                           validation_method=lambda x: utils.validate_coordinate(x, coord_type='lat'))
        lon = input_params(prompt_text='Enter longitude: ',
                           validation_method=lambda x: utils.validate_coordinate(x, coord_type='lon'))
        city = City(city_name, lat, lon)
        city.write_city_to_db(connection)

    return city


# Function with main logic for calculating the distance between two cities
@try_again_prompt
def calculate_distance(connection):
    city1 = input_city_details(connection)
    city2 = input_city_details(connection)
    if city1 == city2:
        print(f'\n>>> Hold up! You chose the same city twice. The distance between cities is 0, Einstein. 😎')
    else:
        distance = city1.get_distance_to(city2)
        print(f'\n>>> The distance between {city1.name} and {city2.name} is {int(distance)} km.')


# Main entry point of the program
def main():
    print("\n__________Welcome to the City Distance Calculator!__________\n"
          "Eager to find out the distance between cities? Let's dive in!")

    # Establish database connection
    with pyodbc.connect(DB_CONN) as conn:
        while True:
            # Perform distance calculation
            calculate_distance(conn)

            # Ask user if they want to run another calculation
            answer = input('\nDo you want to calculate distance between other cities? (Y/N): ')
            if answer.upper() == 'Y':
                continue
            else:
                # Exit message
                print("\nMission accomplished! If you're not flying around in a private jet, "
                      "maybe double-check the distance online.\n✈️ Bon voyage! ✈️\n")


if __name__ == '__main__':
    main()
