user = {
    "id": 1,
    "name": "Leanne Graham",
    "username":"Bret",
    "email":"Sincere@april.biz",
    "address": {
        "street":"Kulas Light",
        "suite":"Apt. 556",
        "city":"Gwenborough",
        "zicode":"123-456",
        "geo": {
            "lat":"-37.3159",
            "lng":"81.1234"
        }

    }
}
print(user)
print(user["id"])
print(user["username"])
print(user["email"])
print(user["address"])
print(user["address"]["street"])
print(user["address"]["geo"])
print(user["address"]["geo"]["lat"])
print(user["address"]["geo"]["lng"])

print(user)
print(type(user))
print("\nubah dict ke json")
import json
result = json.dumps(user)
print(type(result))
print(result)

with open("result.json","w") as file:
    json.dump(user, file)