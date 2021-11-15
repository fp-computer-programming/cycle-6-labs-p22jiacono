#Author:JTI 11/15/21

colors = ['blue', 'white', 'red', 'black']


colors.extend(['grey', 'pink', 'purple'])

print(colors)

print(colors.count('yellow'))

colors.insert(3, "gold")
print(colors)

colors.clear()
print(colors)

print(colors.count('red'))