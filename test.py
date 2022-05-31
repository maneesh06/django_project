import requests

# response = requests.get("http://127.0.0.1:8000/user?page=1")
res = requests.post("http://127.0.0.1:8000/user",{'first_name':'prasahnt','last_name':'singh'})