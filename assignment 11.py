#11 - 1

#city_function.py
def city_country(city, country, population=None):
    """Return a string like 'Budapest, Hungary' or
       'Budapest, Hungary - population 5000000'."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    return f"{city.title()}, {country.title()}"


