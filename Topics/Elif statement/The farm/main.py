
budget = int(input())

if budget < 23:
    print("None")
elif budget < 678:
    number = budget // 23
    if number > 1:
        animal = "chickens"
    else:
        animal = "chicken"
    print(str(number), animal)
elif budget < 1296:
    number = budget // 678
    if number > 1:
        animal = "goats"
    else:
        animal = "goat"
    print(str(number), animal)
elif budget < 3848:
    number = budget // 1296
    if number > 1:
        animal = "pigs"
    else:
        animal = "pig"
    print(str(number), animal)
elif budget < 6769:
    number = budget // 3848
    if number > 1:
        animal = "cows"
    else:
        animal = "cow"
    print(str(number), animal)
elif budget >= 6769:
    number = budget // 6769
    print(str(number), "sheep")
