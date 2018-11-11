# 1:
print("1:")
alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# 2:
print("\n2:")
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 3:
print("\n3:")
alien_0  = {}

alien_0['color'] = 'red'
alien_0['points'] = 4

print(alien_0)

# 4:
print("\n4:")
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0 = {'color': 'red'}
print("The alien is " + alien_0['color'] + ".")

# 5:
print("\n5:")
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x_position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

# 6:
print("\n6:")
alien_0 = {'color': 'green', 'point': 5}
alien_1 = {'color': 'yellow', 'point': 10}
alien_2 = {'color': 'red', 'point': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# 7:
print("\n7:")
aliens = []

for alien_number in  range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alilen['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print("...")

print("Total  number of aliens: " + str(len(aliens)))