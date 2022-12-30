import json

import requests

base_url = "https://randomuser.me/api/"

try:
    r = requests.get(base_url, timeout=10)
except requests.exceptions.ConnectionError:
    print("Invalid URL.")
    exit(1)

if r.status_code != 200:
    print("Invalid query.")
    exit(1)

response = r.json()

data = response.get("results")[0]

gender = data.get("gender")
name_data = data.get("name")
name = f'{name_data.get("title")}. {name_data.get("first")} {name_data.get("last")}'
email = data.get("email")
phone = data.get("phone")

print(
    """
Name: {name}
Gender: {gender}
Email: {email}
Phone: {ph}
""".format(
        name=name, gender=gender, email=email, ph=phone
    )
)
