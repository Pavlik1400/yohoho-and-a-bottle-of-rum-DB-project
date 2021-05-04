from flask_restful import Api, Resource, reqparse, abort
from tables import *
from database import loadSession


db_session = loadSession()


class AlcoholicAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("id_alc", type=int, help="Id of the alcoholic is required", required=True)
    parser.add_argument("fname", type=str, help="First name")
    parser.add_argument("lname", type=str, help="Last name")

    def get(self, id_alc):
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