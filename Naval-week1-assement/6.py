import requests
import sys

url = "https://api.github.com/users/anthropics"

try:
    response = requests.get(url, timeout=10)

    # Check if request was successful
    if response.status_code != 200:
        print(f"Error: Request failed with status code {response.status_code}")
        sys.exit(1)

    data = response.json()

    name = data.get("name")
    public_repos = data.get("public_repos")
    followers = data.get("followers")

    print("Name:", name)
    print("Public Repos:", public_repos)
    print("Followers:", followers)

except requests.exceptions.RequestException as e:
    print("Error: Unable to complete the request.")
    print("Details:", e)
    sys.exit(1)