from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker, mapper
from tables import *


def loadSession():
    engine = create_engine('postgresql://postgres::postgres@localhost:5432/vutvereznyk')
    metadata = MetaData(engine)

    for table_name in table_names:
        mapper(table_names[table_name], Table(table_name, metadata, autoload=True))

    Session = sessionmaker(bind=engine)
    session = Session()
    return session


if __name__ == '__main__':
    session = loadSession()
    res = session.query(Inspector).filter(Inspector.id_ins == 10).all()
    print(res)