from sqlalchemy import create_engine, Table, MetaData, inspect
from sqlalchemy.orm import sessionmaker, mapper
from tables import *


def loadSession():
    engine = create_engine('postgresql://postgres::postgres@localhost:5432/vutvereznyk')
    metadata = MetaData(engine)

    for table_name in TABLE_CLASSES:
        mapper(TABLE_CLASSES[table_name], Table(table_name, metadata, autoload=True))
        TABLE_PRIMARY_KEYS[table_name] = Table(table_name, metadata).primary_key.columns.values()[0].name

    Session = sessionmaker(bind=engine)
    session = Session()

    inspector = inspect(engine)
    schemas = inspector.get_schema_names()

    for schema in schemas:
        for table_name in inspector.get_table_names(schema=schema):
            if table_name in TABLE_CLASSES:
                for column in inspector.get_columns(table_name, schema=schema):
                    if table_name in TABLE_COLUMNS:
                        TABLE_COLUMNS[table_name].append(column['name'])
                    else:
                        TABLE_COLUMNS[table_name] = [column['name']]
    return session


if __name__ == '__main__':
    session = loadSession()
    res = session.query(Inspector).filter(Inspector.id_ins == 10).all()
    print(res)