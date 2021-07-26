def func_name():
    return "Custom Function"


def another_func():
    print("Another Function")


def send_num(num):
    return num * 2


def myget(key):
    value = ""
    dic = {
        "Name": "Md Abir",
        "Age": "20",
        "Address": "Dhaka"
    }

    return dic[key]


# myget()
print(myget("Address"))


def mysum(a, b):
    return a + b


print(mysum(10, 30))

