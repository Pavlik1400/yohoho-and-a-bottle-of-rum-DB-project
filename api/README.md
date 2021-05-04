### USAGE
start API server: 
```python3 main.py```

Before starting make sure that there is 'vutvereznyk' database, CREATE_TABLES.sql is executed. Script expects postgresql server on 5432 port of localhost

### Examples
alcoholic API resource: "/alcoholic/\<int:id_alc\>"
- get alcoholic:
```python
BASE = "http://127.0.0.1:5000/"
requests.get(requests.get(BASE + "inspector/12").json())
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

alcoholic API resource: "/inspector/\<int:id_ins\>"
