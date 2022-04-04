# put your python code here

num_1 = (input())
num_2 = (input())
operator = input()

# print(num_1)
# print(num_2)
# print(operator)

expression = ''
if operator in ['/', 'mod', 'div'] and float(num_2) == 0.0:
    print("Division by 0!")
elif operator == "pow":
    print(pow(float(num_1), float(num_2)))
else:
    if operator == "mod":
        operator = "%"
    elif operator == "div":
        operator = "//"

    expression = num_1 + operator + num_2
    result = eval(expression)

    print(result)
