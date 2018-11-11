# 1:
print("1:")
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies")

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('apple' in requested_toppings)

# 2:
print("\n2:")
requested_toppings = ['mushrooms', 'green peppers', 'pineapple']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

# 3:
print("\n3:")
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# 4:
print("\n4:")
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")