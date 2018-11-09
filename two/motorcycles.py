motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(3, 'yahu')
print(motorcycles)

del motorcycles[2]
print(motorcycles)

# 2:
popped_motorcycle = motorcycles.pop()
print("\n2 : \npopped_motorcycle")
print(motorcycles)

# 3:
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop(1)
print("\n3:\nThis last motorcycle I owned was a " + last_owned.title() + ".")

# 4:
print("\n4:")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")