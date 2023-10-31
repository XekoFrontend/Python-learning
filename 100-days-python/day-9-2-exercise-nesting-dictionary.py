# Nesting dictionary in list
travel_log = [
    {
        "country": "France",
        "visits": 12,
        # 1 key is only 1 value, so nesting them in a list
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        # 1 key is only 1 value, so nesting them in a list
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]


def add_new_country(country_visited, time_visited, cities_visited):

    # Creating the new dictionary, that is a item to add to the list
    new_country = {}

    new_country["country"] = country_visited
    new_country["visits"] = time_visited
    new_country["cities"] = cities_visited

    # Adding the new item to the list
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
