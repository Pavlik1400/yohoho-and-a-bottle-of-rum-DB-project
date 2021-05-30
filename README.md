# yohoho-and-a-bottle-of-rum-DB-project
This repository is project for DB course at UCU

[Here](./docs/vutvereznuk.pdf) is the db diagram

[Here](https://docs.google.com/presentation/d/e/2PACX-1vS_3QxUVFzwp1ZslXd1UHUVn1Pn98InevlZaJiEi0i6M6kH-ZRrAcXuspQAG2F06wmjDeAz_YqFZrYx/pub?start=false&loop=false&delayms=3000) midterm presentation

## Usage
1) initial setup of venv and database (make sure you have user 'postgres'):
```bash
sudo chmod +x ./initial_setup.sh
./initial_setup.sh
```   
2) start application:
```bash
python3 ./api/main.py
```
## Requirements
- python3.8+
- postgres installed with user named 'postgres'