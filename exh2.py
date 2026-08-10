info = {
    "name": "bipul",
    "age": 25,
}

try:
    print(info["phone_no"])
except KeyError:
    print("Phone number not found.")
except Exception:
    print("An error occurred.")