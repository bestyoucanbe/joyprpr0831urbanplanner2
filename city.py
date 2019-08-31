# Instructions
# In the previous Urban Planner exercise, you practiced defining custom types to represent buildings. Now you need to create a type to represent your city. Here are the requirements for the class. You define the properties and methods.

# Name of the city.
# The mayor of the city.
# Year the city was established.
# A collection of all of the buildings in the city.
# A method to add a building to the city.
# Remember, each class should be in its own file. Define the City class in the city.py file.


class City:

    def __init__(self, city_name, city_mayor, city_year):
        self.city_name = city_name
        self.city_mayor = city_mayor
        self.city_year_established = city_year
        self.buildings_in_city = list()

    def add_this_building_to_city(self, building_constructed):
        self.buildings_in_city.append(building_constructed)
