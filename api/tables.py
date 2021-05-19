from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table


Base = declarative_base()


class ActiveAlcoholic:
    pass


class Alcoholic:
    pass


# class Alcoholic(Base):
#     __table__ = Table('alcoholic', Base.metadata,
#                       autoload=True, autoload_with=engine)


class Bed:
    pass


class Bribe:
    pass


class Drink:
    pass


class Escape:
    pass


class GroupChekIn:
    pass


class GroupInfo:
    pass


class Inspector:
    pass


class Job:
    pass


class Log:
    pass


class Unconsciousness:
    pass


TABLE_CLASSES = {
    'active_alcoholic': ActiveAlcoholic,
    'alcoholic': Alcoholic,
    'bed': Bed,
    'bribe': Bribe,
    'drink': Drink,
    'escape': Escape,
    'group_check_in': GroupChekIn,
    'group_info': GroupInfo,
    'inspector': Inspector,
    'job': Job,
    'log': Log,
    'unconsciousness': Unconsciousness
}

TABLE_COLUMNS = {}

TABLE_PRIMARY_KEYS = {}