a = input("Enter the a value")
b = input("Enter the b value")

a = int(input("Enter the a value"))
b = int(input("Enter the b value"))

print(type(a), type(b))

# type casting
a = int(a)
b = int(b)
print(type(a), type(b))
if a > b:
    print("True")
else:
    print("False")

# nested condition
age = int(input())
if age >= 18:
    print("You are eligible for vote, do you have nid?")
    nid = int(input())
    passport = int(input())
    # if else ladder
    if nid == 1:
        print("Ok you can give your vote")
    elif passport == 1:
        print("You can take admission")
    else:
        print("your age is perfect but you don't have nid")
else:
    print("Your age is under 18")

gpa = 2.5
if gpa > 1 and gpa < 2:
    print("D")
elif gpa > 2 and gpa < 3:
    print("C")
