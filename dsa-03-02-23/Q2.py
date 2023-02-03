'''Write a program to accept the names of 10 cities in a single dimension string array and
their STD (Subscribers Trunk Dialing) codes in another single dimension integer array.
Search for a name of a city input by the user in the list. If found, display* “Search successful” and
print the name of the city along with its STD code, or else
display the message “Search Unsuccessful, No such city in the list”.'''

cities = ['delhi', 'pune', 'mumbai', 'chennai', 'hydrabad', 'kolkata', 'amritsar', 'indor', 'chandigarh', 'shimla']
std = [1000, 1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]

print("Enter city name to check std: ")
city = input()
city = city.lower()

result = False
for i in range(0, len(city)):
    if cities[i] == city:
        result = True
        print("Search successful")
        print(city, "std is->", std[i])

if not result:
    print("Search Unsuccessful")