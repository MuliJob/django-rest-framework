"""Basic Client API"""
import requests

endpoint = "http://localhost:8000/api/products/4/update/"

data = {
  "title": "hello world my fiend again and again",
  "price": 46.37,
  "content": "Content cannot be null"
}
get_response = requests.put(endpoint, json=data)
print(get_response.json())
