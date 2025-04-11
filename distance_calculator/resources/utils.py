# Validate latitude/longitude: it should be a float and within the valid range
def validate_coordinate(value, coord_type):
    try:
        value = float(value)
    except:
        raise TypeError(f'The latitude/longitude should be a number')
    if coord_type == 'lat':
        if not (-90 <= value <= 90):
            raise ValueError('Latitude must be between -90 and 90 degrees')
    elif coord_type == 'lon':
        if not (-180 <= value <= 180):
            raise ValueError('Longitude must be between -180 and 180 degrees')
    else:
        raise ValueError(f'Invalid coordinate type: {coord_type}. Expected "lon" or "lat"')
    return value


# Validate string for correctness: it should be of string type and of acceptable length
def validate_city(city_str, min_len=0, max_len=100):
    if type(city_str) is not str or not city_str:
        raise TypeError(f'City should be a string.')
    if not min_len <= len(city_str) <= max_len:
        raise ValueError(f'City must be between {min_len} and {max_len} characters long.')
    return city_str
