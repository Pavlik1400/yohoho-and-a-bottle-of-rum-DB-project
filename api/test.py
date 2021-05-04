import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE + "alcoholic/16")
# print(response.json())

# data = {'id_alc': 16, 'fname': 'Pasha', 'lname': 'Hilei'}
# response = requests.put(BASE + "alcoholic/16", data)
# print(response)

response = requests.delete(BASE + "alcoholic/16")
print(response)
