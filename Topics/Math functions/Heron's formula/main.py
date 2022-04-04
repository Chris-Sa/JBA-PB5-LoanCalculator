# put your python code here
import math

side_1 = int(input())
side_2 = int(input())
side_3 = int(input())

p = (side_1 + side_2 + side_3) / 2

first = p - side_1
second = p - side_2
third = p - side_3

squared = p * first * second * third

area = math.sqrt(squared)

print(area)