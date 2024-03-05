import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and data.get("success") and "data" in data:
        user_data = data["data"]
        
        # Extracting user information from the response data
        full_name = f"{user_data['name']['title']} {user_data['name']['first']} {user_data['name']['last']}"
        username = user_data["login"]["username"]
        email = user_data["email"]
        gender = user_data["gender"]
        city = user_data["location"]["city"]
        state = user_data["location"]["state"]
        country = user_data["location"]["country"]

        return {
            "full_name": full_name,
            "username": username,
            "email": email,
            "gender": gender,
            "city": city,
            "state": state,
            "country": country
        }
    else:
        # Handle API error response
        raise Exception("Failed to fetch random user!")

def main():
    try:
        random_user = fetch_random_user()
        print(random_user)
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()
