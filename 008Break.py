val = int(input("Enter a value: "))

if val == 0:
    print(0)
elif val > 0:
    for i in range(0, val+1):
        if i > 6 and i % 7 == 0:
            break
        print(i)
else:
    for i in range(0, val-1, -1):
        if i < -6 and i % 7 == 0:
            break
        print(i)


