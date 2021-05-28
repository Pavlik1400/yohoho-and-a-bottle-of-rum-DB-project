cd api
python3 -m venv venv
pip3 install -r requirements.txt
dropdb --if-exists -U postgres vutvereznyk
psql -U postgres -c "CREATE DATABASE vutvereznyk"
cd ..
psql -U postgres -d vutvereznyk -f initialization/CREATE_TABLES.sql
psql -U postgres -d vutvereznyk -f initialization/CREATE_TRIGGERS.sql
psql -U postgres -d vutvereznyk -f initialization/CREATE_INDEXES.sql
psql -U postgres -d vutvereznyk -f initialization/INSERT_DATA.sql
