from flask import Flask, request, render_template
from flask_restful import Api, Resource, reqparse, abort
from apis import *

template_dir = '../templates'
app = Flask(__name__, template_folder=template_dir)

# app = Flask(__name__)
api = Api(app)


# api.add_resource(Hello, "/hello")
api.add_resource(AlcoholicAPI, "/alcoholic/<int:id_alc>")
api.add_resource(InspectorAPI, "/inspector/<int:id_ins>")

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

@app.route("/alcoholic_queries.html")
def alcoholic_queries():
    return render_template("alcoholic_queries.html")

@app.route("/alcoholic_queries_output.html", methods = ['POST', 'GET'])
def alcoholic_queries_output():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        print(form_data)
        return render_template("alcoholic_queries_output.html", form_data = form_data)

if __name__ == '__main__':
    app.run(debug=True)
