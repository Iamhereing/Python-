# 1:
print("1:")
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

# 2:
print("\n2:")
age = 12
if age < 4:
    price = 0
if age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")