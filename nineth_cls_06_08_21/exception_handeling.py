print("welcome")

print(10/3)

try:
    # logic statement

    print("before the error")
    print(10 / 0)
except Exception as e:
    # what type of error
    print(e)

print("After the error")
print(100/20)
try:
    var = input("enter value")
    print(type(var))
    print(var / 2)
except Exception as e:
    print(e)

print("After the second error")
print(100/10)
