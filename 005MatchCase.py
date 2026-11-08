age = int(input("Enter your age: "))

match age:
    case x if x < 0:
        print("Invalid age")
    case x if x < 13:
        print("Child")
    case x if x < 18:
        print("Teenager")
    case x if x < 65:
        print("Adult")
    case _:
        print("Senior")
