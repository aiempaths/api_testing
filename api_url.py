Python
import requests

url = "http://YOUR-IP:5002/predict"
payload = {
    "window": [1.2, 3.4, 0.8, 2.1, 4.5, 1.9]
}

try:
    response = requests.post(url, json=payload)
    response.raise_for_status() # Raise an error for bad status codes
    print("Response from server:", response.json())
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
