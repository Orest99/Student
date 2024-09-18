dict1 ={
    "Key": " Para 1",
    "Key2": "Para 2",
    "Key3": "Para 3",
    "Key4": "Para 4",
    "Key5": "Para 5",
    "Key6": "Para 6",
    "Key7": "Para 7",
    "Key8": "Para 8",
    "Key9": "Para 9",
    "Key10": "Para 10"
    }
dict1["Key2"] = "Test"
dict1["Key7"] = "Beta test"
dict1.pop("Key3")
dict1.pop("Key4")
print(dict1)
