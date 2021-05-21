# import flask.scaffold
# flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api, Resource, reqparse, abort
from tables import *
from database import loadSession
import sqlalchemy
from queries import *
from pprint import pprint
from sqlalchemy import func


db_session = loadSession()

class AlcoholicAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("id_alc", type=int, help="Id of the alcoholic is required")
    parser.add_argument("fname", type=str, help="First name")
    parser.add_argument("lname", type=str, help="Last name")

    def get(self, id_alc):
        args = self.parser.parse_args()
        if args['fname'] and args['lname']:
            q_res = db_session.query(Alcoholic).filter(
                Alcoholic.fname == args['fname'] and Alcoholic.lname == args['lname']
            ).all()
        else:
            q_res = db_session.query(Alcoholic).filter(Alcoholic.id_alc == id_alc).all()
        if q_res:
            alco = q_res[0]
            return {'id_alc': alco.id_alc, 'fname': alco.fname, 'lname': alco.lname}
        else:
            abort(404, message=f"There is no alcoholic with id: {id_alc}")

    def put(self, id_alc):
        q_res = db_session.query(Alcoholic).filter(Alcoholic.id_alc == id_alc).all()
        if q_res:
            abort(409, message=f"There already is alcoholic with id: {id_alc}")
        else:
            args = self.parser.parse_args()
            new_alcoholic = Alcoholic()
            new_alcoholic.id_alc = id_alc
            new_alcoholic.fname = args['fname']
            new_alcoholic.lname = args['lname']
            db_session.add(new_alcoholic)
            db_session.commit()
            return '', 201

    def delete(self, id_alc):
        q_res = db_session.query(Alcoholic).filter(Alcoholic.id_alc == id_alc).all()
        if not q_res:
            abort(404, message=f"There is no alcoholic with id: {id_alc}")
        else:
            alco = db_session.query(Alcoholic).filter(Alcoholic.id_alc == id_alc).one()
            db_session.delete(alco)
            db_session.commit()
            return '', 200


class InspectorAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("id_ins", type=int, help="Id of the Inspector is required", required=True)
    parser.add_argument("fname", type=str, help="First name")
    parser.add_argument("lname", type=str, help="Last name")

    def get(self, id_ins):
        args = self.parser.parse_args()
        if args['fname'] and args['lname']:
            q_res = db_session.query(Inspector).filter(
                Inspector.fname == args['fname'] and Inspector.lname == args['lname']
            ).all()
        else:
            q_res = db_session.query(Inspector).filter(Inspector.id_ins == id_ins).all()
        if q_res:
            insp = q_res[0]
            print(insp)
            return {'id_ins': insp.id_ins, 'fname': insp.fname, 'lname': insp.lname}
        else:
            abort(404, message=f"There is no inspector with id: {id_ins}")

    def put(self, id_ins):
        q_res = db_session.query(Inspector).filter(Inspector.id_ins == id_ins).all()
        if q_res:
            abort(409, message=f"There already is inspector with id: {id_ins}")
        else:
            args = self.parser.parse_args()
            new_inspector = Inspector()
            new_inspector.id_ins = id_ins
            new_inspector.fname = args['fname']
            new_inspector.lname = args['lname']
            db_session.add(new_inspector)
            db_session.commit()
            return '', 201

    def delete(self, id_ins):
        q_res = db_session.query(Inspector).filter(Inspector.id_ins == id_ins).all()
        if not q_res:
            abort(404, message=f"There is no inspector with id: {id_ins}")
        else:
            inspector = db_session.query(Inspector).filter(Inspector.id_ins == id_ins).one()
            db_session.delete(inspector)
            db_session.commit()
            return '', 200


class QueryAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("id_alc", type=int, help="Id of the alcoholic")
    parser.add_argument("id_ins", type=str, help="id of inspector")

    # date format 2020-01-29 12:00:00
    parser.add_argument("from_date", type=str, help="begin date")
    parser.add_argument("to_date", type=str, help="begin date")
    parser.add_argument("N", type=int, help="Number needed for requests")

    def get(self, query_id):
        if query_id < 1 or query_id > 12:
            abort(400, message=f"query id should be in range [1:12]")

        args = self.parser.parse_args()

        # check if all required arguments are passed
        for param in QUERIES_REQUIRED_ARGS[query_id]:
            if args[param] is None:
                abort(400, message=f"Parameter {param} is required for query {query_id}")

        responce = QUERY_FUNCS[query_id](args, db_session)
        return responce, 200


class EditAPI(Resource):
    parser = reqparse.RequestParser()

    all_columns = [column for table_columns in TABLE_COLUMNS.values() for column in table_columns]
    for column in all_columns:
        parser.add_argument(column, type=str, required=False)

    def put(self, table_name):
        """
        Adds entry to table. All columns except PK are required as arguments
        """
        if table_name not in TABLE_CLASSES:
            abort(404, message=f"There is no table {table_name} in data base")
        cls = TABLE_CLASSES[table_name]
        args = self.parser.parse_args()

        row = {}
        for column in TABLE_COLUMNS[table_name]:
            if args[column] is None and column != TABLE_PRIMARY_KEYS[table_name]:
                abort(400, message=f"column {column} is required")
            row[column] = args[column]

        if args[TABLE_PRIMARY_KEYS[table_name]] is None:
            max_PK = db_session.query(func.max(cls.__dict__[TABLE_PRIMARY_KEYS[table_name]])).scalar()
            row[TABLE_PRIMARY_KEYS[table_name]] = max_PK + 1

        try:
            new_entry = cls()

            new_entry.__dict__ |= row
            db_session.add(new_entry)
            db_session.commit()
        except Exception as err:
            abort(409, message=f"Error happened in datavase: {str(err)}")
        return '', 201

    def delete(self, table_name):
        """
        Deletes value from the table
        parameters will go to 'where' part in delete statement
        """
        args = self.parser.parse_args()
        non_none_args = {k: v for k, v in args.items() if v is not None}
        for column in non_none_args:
            if column not in TABLE_COLUMNS[table_name]:
                abort(400, message=f"There is no column {column} in table {table_name}")

        execute_script = f"delete from {table_name} where "
        for column in non_none_args:
            execute_script += f"{column}='{args[column]}' AND " if type(args[column]) != int else \
                f"{column}={args[column]} AND "
        execute_script = execute_script.removesuffix(" AND ")
        execute_script += ";"
        print(execute_script)
        db_session.execute(execute_script)
        db_session.commit()
        return '', 200
