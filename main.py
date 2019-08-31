from building import Building
from city import City

# Create 5 building instances

FirstBuilding = Building("101 1st Street", 10)
SecondBuilding = Building("202 2nd Street", 20)
ThirdBuilding = Building("303 3rd Street", 30)
FourthBuilding = Building("404 4th Street", 40)
FifthBuilding = Building("505 5th Street", 50)

# Have each one get purchased by a real estate magnate

FirstBuilding.purchase("RealEstateMagnate1")
SecondBuilding.purchase("RealEstateMagnate2")
ThirdBuilding.purchase("RealEstateMagnate3")
FourthBuilding.purchase("RealEstateMagnate4")
FifthBuilding.purchase("RealEstateMagnate5")

# After purchased, construct each one

FirstBuilding.construct()
SecondBuilding.construct()
ThirdBuilding.construct()
FourthBuilding.construct()
FifthBuilding.construct()


# Once all building are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one.
# Example
# 800 8th Street was purchased by Bob Builder on 03/14/2018 and has 12 stories.

print(f'{FirstBuilding.address} was purchased by {FirstBuilding.owner} on {FirstBuilding.date_constructed} and has {FirstBuilding.stories} stories')
print(f'{SecondBuilding.address} was purchased by {SecondBuilding.owner} on {SecondBuilding.date_constructed} and has {SecondBuilding.stories} stories')
print(f'{ThirdBuilding.address} was purchased by {ThirdBuilding.owner} on {ThirdBuilding.date_constructed} and has {ThirdBuilding.stories} stories')
print(f'{FourthBuilding.address} was purchased by {FourthBuilding.owner} on {FourthBuilding.date_constructed} and has {FourthBuilding.stories} stories')
print(f'{FifthBuilding.address} was purchased by {FifthBuilding.owner} on {FifthBuilding.date_constructed} and has {FifthBuilding.stories} stories')
print("")

# Create a city using the City class
Nashville = City("Nashville", "David Briley", 1897)

# Add each building to this city
Nashville.add_this_building_to_city(FirstBuilding)
Nashville.add_this_building_to_city(SecondBuilding)
Nashville.add_this_building_to_city(ThirdBuilding)
Nashville.add_this_building_to_city(FourthBuilding)
Nashville.add_this_building_to_city(FifthBuilding)

print("Buildings in Nashville:")
print("")
for each_building in Nashville.buildings_in_city:
    print(f' Address of building: {each_building.address}')
