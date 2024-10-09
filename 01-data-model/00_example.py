user_information = {
    "name":"john",
    "lastname":"doe"
}

print(user_information["name"])
print(user_information.get("name"))
print(user_information.__getitem__("name"))