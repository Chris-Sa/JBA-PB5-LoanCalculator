
count = 0
namelist = []
name = input()

while name != '.':
    namelist.append(name)
    count += 1
    name = input()

print(namelist)
print(count)
