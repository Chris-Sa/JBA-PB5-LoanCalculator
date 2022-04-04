
offset = int(input())

# reference time = 10:30 Tuesday
# <= -11 Monday
# -10 to + 13 Tuesday
# >= +14 Wednesday

if offset <= -11:
    print("Monday")
elif offset <= 13:
    print("Tuesday")
else:
    print("Wednesday")
