import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE + "alcoholic/0?fname=John&lname=Doe")
# print(response)
# print(response.json())

# data = {'id_alc': 16, 'fname': 'Pasha', 'lname': 'Hilei'}
# response = requests.put(BASE + "alcoholic/16", data)
# print(response)

# response = requests.delete(BASE + "alcoholic/16")
# print(response)


# response = requests.get(BASE + "query/12?id_alc=4&id_ins=8&from_date=2020-04-29 12:00:00&to_date=2021-05-10 22:30:00&N=0")
# print(response.text)

response = requests.get(BASE + "query/12?id_alc=4&id_ins=8&from_date=2020-04-29 12:00:00&to_date=2021-05-10 22:30:00&N=0")
print(response.text)