# API = application programming interface 
# CRUD=create,update,read,delete
import requests
# api=requests.get("http://arkprocoder.com/api/technolgies/3")
api=requests.get("https://api.github.com/users")
print(api)
print(api.content)
print(api.headers)
print(api.json())