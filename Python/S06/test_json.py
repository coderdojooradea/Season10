import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
print(todos)
print(40*"-")
print(len(todos))
print(40*"=")
print(todos[0])