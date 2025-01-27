"""Basic Client API"""
import requests

endpoint = "http://localhost:8000/api/products/"
data = {
  "title": "This is a new product",
  "price": 64.27
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())
