import requests

base_url = "https://catfact.ninja/fact"

try:
    r = requests.get(base_url, timeout=10)
except requests.exceptions.ConnectionError:
    print("Invalid URL.")
    exit(1)

if r.status_code != 200:
    print("Invlaid query.")
    exit(1)

response = r.json()

print(f'Fact: {response.get("fact")}\nLength: {response.get("length")}')
