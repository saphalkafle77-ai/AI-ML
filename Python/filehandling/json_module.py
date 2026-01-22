import json

py_obj = {"kathmandu": 120000, "pokhara": 210000, "sindhuli": 50000}
with open("conceptual/filehandling/cities.json", "w") as f:
    json.dump(py_obj, f)
with open("conceptual/filehandling/cities.json", "r") as f:
    json_str = json.load(f)
    print(json_str)
city = input("enter city ")
population = int(input("enter population"))
json_str[city] = population

with open("conceptual/filehandling/cities.json", "w") as f:
    json.dump(json_str, f)
print(json_str)
