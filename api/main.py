from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from apis import *


app = Flask(__name__)
api = Api(app)


# api.add_resource(Hello, "/hello")
api.add_resource(AlcoholicAPI, "/alcoholic/<int:id_alc>")
api.add_resource(InspectorAPI, "/inspector/<int:id_ins>")


if __name__ == '__main__':
    app.run(debug=True)
