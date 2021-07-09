# key value pair

dic = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

print(dic)
print(type(dic))

l = [1, 2, 3, 4]

print(dic['key1'], dic['key2'])

for i in dic.items():
    print(i[0], i[1])

dic = {
    "Name": "Mr Abir",
    "Age": 26,
    "Address": {
        "Present": "Dhaka",
        "Permanent": {
            "Home1": "Sylhet",
            "Home2": "USA"
        }
    }
}

print(dic['Name'], dic['Address']['Permanent']['Home1'])

df = {
    "Name": ["Abir", "Zoha", "Masud", "Akram"],
    "Dept": ["CSE", "IT", "BBA", "EEE"],
    "Sem": ["1st", "4th", "3rd", "8th"],
}

for i, j in df.items():
    print(i, ":", j)

print(df.values())
print(df.keys())

print(df.get("Name"))

dic_update = {"Address": {"Present": "Comilla"}}

dic.update(dic_update)
print(dic)
