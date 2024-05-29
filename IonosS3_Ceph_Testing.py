import requests
import time
import uuid as UUID
from datetime import datetime

# Authentication token (replace with your actual token)
TOKEN = ''

# Headers for authentication
HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'
}

# API URL
BASE_URL = 'https://s3.ionos.com/accesskeys'
payload = {
    "metadata": {},
    "properties": {
        "description": "Access key details"
    }
}

# Function to create an access key
def create_access_key():
    response = requests.post(BASE_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()

# Funtion to create access key manually
def create_manualy_access_key():
    access_key_id = str(UUID.uuid4())
    url = f"{BASE_URL}/{access_key_id}"
    payload = {
            "id": access_key_id,
            "metadata": { },
            "properties": {
                "description": "Access key details"
                }
            }
    print(payload)
    response = requests.put(url, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()

# Function to verify the access key
def verify_access_key(access_key_id):
    print(access_key_id)
    url = f"{BASE_URL}/{access_key_id}"
    response = requests.get(url, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()

# Function to delete the access key
def delete_access_key(access_key_id):
    url = f"{BASE_URL}/{access_key_id}"
    response = requests.delete(url, headers=HEADERS, json=payload)
    response.raise_for_status()

# Function to measure the time until the key is available
def measure_key_availability():
    start_time = datetime.now()

    # Create access key
    created_key = create_access_key()
    access_key_id = created_key['id']

    # Verify access key
    while True:
        try:
            verified_key = verify_access_key(access_key_id)
            if verified_key['metadata']['status'] == 'AVAILABLE':
                break
        except requests.exceptions.HTTPError as e:
            pass  # Keep trying until the key is available
        time.sleep(1)

    end_time = datetime.now()
    time_difference = (end_time - start_time).total_seconds()

    # Delete access key
    delete_access_key(access_key_id)

    return time_difference

# Main function
def main():
    num_iterations = 10
    time_differences = []

    for i in range(num_iterations):
        time_diff = measure_key_availability()
        time_differences.append(time_diff)
        print(f"Time difference for iteration {i+1}: {time_diff} seconds")

    print("All time differences:", time_differences)
    average_time = sum(time_differences) / num_iterations
    print(f"Average time taken for the access key to be available: {average_time} seconds")

if __name__ == "__main__":
    main()
