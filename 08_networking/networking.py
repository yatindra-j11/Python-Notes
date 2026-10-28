# ==========================================
# PHASE 12: NETWORKING DEMO
# Banking REST API Client
# ==========================================

import os
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


# 1. GET — Fetch data from an API
def get_user(user_id):
    try:
        response = requests.get(
            f"{BASE_URL}/users/{user_id}",
            timeout=5
        )

        response.raise_for_status()
        user = response.json()

        print("User:", user["name"])
        print("Email:", user["email"])
        print("Status:", response.status_code)

    except requests.exceptions.Timeout:
        print("Request timed out")

    except requests.exceptions.HTTPError as e:
        print("HTTP error:", e)

    except requests.exceptions.RequestException as e:
        print("Network error:", e)

    except ValueError:
        print("Response was not valid JSON")


# 2. POST — Send JSON data to an API
def create_transaction():
    data = {
        "type": "deposit",
        "amount": 1000,
        "userId": 1
    }

    try:
        response = requests.post(
            f"{BASE_URL}/posts",
            json=data,
            timeout=5
        )

        response.raise_for_status()

        print("Created resource:", response.json())
        print("Status:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)


# 3. QUERY PARAMETERS — Filter or paginate results
def get_posts():
    try:
        response = requests.get(
            f"{BASE_URL}/posts",
            params={"userId": 1, "_limit": 3},
            timeout=5
        )

        response.raise_for_status()

        for post in response.json():
            print(post["id"], post["title"])

        print("Final URL:", response.url)

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)


# 4. SESSION — Reuse configuration across requests
def session_demo():
    with requests.Session() as session:
        session.headers.update({
            "Accept": "application/json"
        })

        response = session.get(
            f"{BASE_URL}/users/1",
            timeout=5
        )

        response.raise_for_status()
        print("Session request:", response.json()["name"])


# 5. AUTHENTICATION HEADER — Example pattern
def authenticated_request():
    token = os.environ.get("API_TOKEN")

    if not token:
        print("Set the API_TOKEN environment variable first")
        return

    try:
        response = requests.get(
            "https://api.example.com/account",
            headers={"Authorization": f"Bearer {token}"},
            timeout=5
        )

        response.raise_for_status()
        print(response.json())

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)


# Run the demos
if __name__ == "__main__":
    get_user(1)
    print()

    create_transaction()
    print()

    get_posts()
    print()

    session_demo()

    # authenticated_request()  # Requires a real API and token
