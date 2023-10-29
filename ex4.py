buses = 100
seats = 50.0
drivers = 60
passengers = 5300
buses_not_driven = buses - drivers
buses_driven = drivers
passenger_capacity = buses_driven*seats
average_passengers_per_bus = passengers / buses_driven
print("There are ", buses, " buses available today")
print("There are only ", drivers, " buses availale today")
print("There will be ", buses_not_driven ," buses not riding today")
print("We can transport ", passenger_capacity , " person today")
print("We have ", passengers , " today")
print("Aveerge person per bus is ", int(average_passengers_per_bus))
