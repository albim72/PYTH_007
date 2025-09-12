import json

data = {"name":"Mateusz","wiek":27,"waga":98}
json_str = json.dumps(data)
print(json_str)
print(type(json_str))

#czytanie danych json
parsed_json = json.loads(json_str)
print(parsed_json)
print(type(parsed_json))
