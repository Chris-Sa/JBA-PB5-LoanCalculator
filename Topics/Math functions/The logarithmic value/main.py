import math

value_1 = int(input())
value_2 = int(input())

if value_2 < 2:
    result = math.log(value_1)
else:
    result = math.log(value_1, value_2)


print(round(result, 2))
