"""Basic Client API"""
import requests

endpoint = "http://localhost:8000/api/products/7686543/"

get_response = requests.get(endpoint)
print(get_response.json())
