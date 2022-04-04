

income = int(input())

tax = 0
percent = 0
calculated_tax = 0

if income <= 15527:
    percent = 0
elif income <= 42707:
    percent = 0.15
elif income <= 132406:
    percent = 0.25
else:
    percent = 0.28

calculated_tax = round(income * percent)
percent = int(percent * 100)

print("The tax for {} is {}%. That is {} dollars!".format(income, percent, calculated_tax))