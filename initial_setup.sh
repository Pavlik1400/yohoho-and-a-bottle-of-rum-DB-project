cd api
echo "Creating virtual enviroment..."
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

echo "Creating DB..."
dropdb --if-exists -U postgres vutvereznyk
psql -U postgres -c "CREATE DATABASE vutvereznyk"
cd ..

echo "Filling DB..."
psql -U postgres -d vutvereznyk -f initialization/CREATE_TABLES.sql
psql -U postgres -d vutvereznyk -f initialization/CREATE_TRIGGERS.sql
psql -U postgres -d vutvereznyk -f initialization/CREATE_INDEXES.sql
psql -U postgres -d vutvereznyk -f initialization/INSERT_DATA.sql
