
score = int(input())
maximum = int(input())

percent = score / maximum

A = 1
B = 0.9
C = 0.8
D = 0.7
F = 0.6

if percent < F:
    print("F")
elif percent < D:
    print("D")
elif percent < C:
    print("C")
elif percent < B:
    print("B")
else:
    print("A")