car_price = int(input("What is the base price of the car?"))

car_price_total = car_price / 100 * 115


print("Your car price plus tax is..")
print(car_price_total)

# Do not use "'s either side of car_price / 100 * 115

print("Your service charge is 3%")

car_price_tsc = car_price_total / 100 * 103

print(car_price_tsc)

print("Your monkey charge is 2%")

m_c = car_price_total / 100 * 3

print(m_c)

print("Your sample piece of cheese was 100%")

c_c = car_price_total * 1

print(c_c)

print("Because you smell we charged you 10%")

s_c = car_price_total * 1.1

print(s_c)

print("Your car's total price is...")


print(car_price_total + car_price_tsc + m_c + c_c + s_c)


