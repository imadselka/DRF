import requests

endpoint = "http://localhost:8000/api/"

headers = {
    "Content-Type": "application/json"
}

get_response = requests.post(endpoint, json={"product_id": 123}, headers=headers)

# Uncomment the following lines to print the response headers and text
# print(get_response.headers)
# print(get_response.text)

if get_response.text:
    try:
        print(get_response.json())
    except ValueError:
        print("Response is not in JSON format")
else:
    print("Empty Response")
