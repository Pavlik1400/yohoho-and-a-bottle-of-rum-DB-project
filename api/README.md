### USAGE
start API server: 
```python3 main.py```

Before starting make sure that there is 'vutvereznyk' database, CREATE_TABLES.sql is executed. Script expects postgresql server on 5432 port of localhost

### Examples
alcoholic API resource: "/alcoholic/\<int:id_alc\>"
- get alcoholic:
```python
BASE = "http://127.0.0.1:5000/"
requests.get(requests.get(BASE + "inspector/1").json())
>>> {'id_alc': 1, 'fname': 'John', 'lname': 'Doe'}
# if you dont't know the id you can set id=0, and specify fname and lname as arguments to get request:
requests.get(requests.get(BASE + "alcoholic/0?fname=John&lname=Doe").json())
>>> {'id_alc': 1, 'fname': 'John', 'lname': 'Doe'}
```
- add alcoholic:
```python
requests.put(BASE + "alcoholic/12", {'id_ins': 12, 'fname': 'Pasha', 'lname': 'Hilei'})
>>> <Response [201]>
```

- remove alcoholic
```python
requests.delete(BASE + "alcoholic/12")
<Response [200]>
```

inspector API resource: "/inspector/\<int:id_ins\>" (Just the same as the alcoholic API)

Queries API:
```python
response = requests.get(BASE + "query/10?id_alc=4&id_ins=8&from_date=2020-04-29 12:00:00&to_date=2021-05-10 22:30:00&N=0")
>>> {
    "reponse": [
        {
            "count": 8,
            "date_part": 5.0
        },
        {
            "count": 3,
            "date_part": 4.0
        }
    ]
}
```
returns 400 if query id is bad or not all needed parameters are provided

Otherwise return json with responce key having as value a list, where each entry is row, and in each entry keys and values - names of columns-value.

