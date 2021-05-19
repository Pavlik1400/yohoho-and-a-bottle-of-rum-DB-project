from flask import Flask, request, render_template
# from flask_restful import Api, Resource, reqparse, abort
from apis import *

template_dir = '../templates'
app = Flask(__name__, template_folder=template_dir)
api = Api(app)

# api_backend.add_resource(Hello, "/hello")
api.add_resource(AlcoholicAPI, "/alcoholic/<int:id_alc>")
api.add_resource(InspectorAPI, "/inspector/<int:id_ins>")
api.add_resource(QueryAPI, "/query/<int:query_id>")
api.add_resource(EditAPI, "/edit/<string:table_name>")


@app.route("/")
@app.route("/index.html")
def index():
    return render_template('index.html')


@app.route("/queries.html")
def queries():
    return render_template('queries.html')


@app.route("/alcoholics.html")
def alcoholics():
    return render_template('alcoholics.html')


@app.route("/inspectors.html")
def inspectors():
    return render_template('inspectors.html')


@app.route("/edit.html")
def edit():
    return render_template('edit.html')


if __name__ == '__main__':
    app.run(debug=True)
