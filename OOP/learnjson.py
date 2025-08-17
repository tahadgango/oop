import json

d = {"name": "taha", "age": 19, "grade": 1}

with open("OOP/first.json", "w") as f:
    json.dump(d, f, indent=4)