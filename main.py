def addTemperature(list, day, value):
    list.append((day, value))

def calculateAverageTemperature(list): 
   avg_temperature = sum(map(lambda x: x[1], list)) / len(list)
   print("Calculate average temperature during week: ", round(avg_temperature, 1))

def printForecast(temperature):
    print(temperature)
 

temperature = [
    ("Monday", 27.5),
    ("Tusday", 30.0),
    ("Wednesday", -5.0),
    ("Thursday", 15.9),
    ("Friday", 22.0)
]

print("Add Saturday and Sunday to list")
addTemperature(temperature, "Saturday", 18.4)
addTemperature(temperature, "Sunday", 20.1)

calculateAverageTemperature(temperature)

print("Print information: ")
printForecast(temperature)