#Variable de base
car = 100
seat = 4
driver = 35
passenger = 60

#Variable pour autres situations
unused_car = (car - driver)
transported_passengers = (seat - 1) * driver
waiting_passengers = passenger - transported_passengers
travels = passenger // transported_passengers + 1

print(f"There are {car} cars available")

print(f"There are {driver} drivers available")

print(f"There are {unused_car} that won't be used")

print(f"There are {transported_passengers} passengers that can be transported during each travel")

print(f"There are {waiting_passengers} waiting for the next turn")

print(f"We need to do {travels} travels for transporting all passengers")