# put your python code here
group_1 = int(input())
group_2 = int(input())
group_3 = int(input())

desks_1 = group_1 // 2 + group_1 % 2
desks_2 = group_2 // 2 + group_2 % 2
desks_3 = group_3 // 2 + group_3 % 2

total = desks_1 + desks_2 + desks_3

print(total)