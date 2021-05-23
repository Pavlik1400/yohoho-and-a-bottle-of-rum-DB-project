from flask import Flask, request, render_template, url_for, session, flash
from flask_restful import Api, Resource, reqparse, abort
from werkzeug.utils import redirect
#from apis import *
from additional_info import AddInfo
#import requests

template_dir = '../templates'
app = Flask(__name__, template_folder=template_dir)
api = Api(app)
app.secret_key = "vutvereznyk"

add_info = AddInfo()

# api_backend.add_resource(Hello, "/hello")
#api.add_resource(AlcoholicAPI, "/alcoholic/<int:id_alc>")
#api.add_resource(InspectorAPI, "/inspector/<int:id_ins>")
#api.add_resource(QueryAPI, "/query/<int:query_id>")
#api.add_resource(EditAPI, "/edit/<string:table_name>")


@app.route("/")
@app.route("/index.html")
def index():
    return render_template('index.html')


@app.route("/queries.html")
def queries():
    return render_template('alcoholic_queries/alcoholic_queries.html')


@app.route("/alcoholics.html")
def alcoholics():
    return render_template('alcoholics.html')


@app.route("/inspectors.html")
def inspectors():
    return render_template('inspectors.html')


@app.route("/edit.html", methods=["POST", "GET"])
def edit():

    #get tables as list
    tables = ["Table1", "Table2", "Table3"]

    if request.method == "POST":
        session["table_to_edit"] = request.form["table_name"]
        edit_type = request.form["edit_type"]
        if edit_type == "insert":
            return redirect(url_for("insert_data"))
        else:
            return redirect(url_for("remove_data"))
    else:
        return render_template('edit.html', tables=tables)


@app.route("/remove_data", methods=["POST", "GET"])
def remove_data():
    table = session["table_to_edit"]

    if request.method == "POST":
        index = request.form["table_index"]
        try:
            #remove row with index
            flash(f"Row with index {index} removed from the table {table}")
        except:
            flash(f"Index {index} invalid")

    return render_template("edit_remove.html")


@app.route("/insert_data", methods=["POST", "GET"])
def insert_data():
    table = session["table_to_edit"]
    cols = ["col1", "col2", "col3"]
    
    if request.method == "POST":
        data = request.form["input_row"]
        try:
            if (len(data) != len(cols)):
                flash(f"Invalid number of arguments")
            else:
                data_for_query = dict(zip(cols, data.split(", ")))
                print(data_for_query)
                flash(f"New row inserted into table {table}")
        except:
            flash(f"Invalid input data")

    return render_template("edit_insert.html", table=table, cols=cols)


# @app.route("/alcoholic_queries.html")
# def alcoholic_queries():
#     return render_template("alcoholic_queries/alcoholic_queries.html")

@app.route("/alcoholic_queries_output.html", methods = ['POST'])
def alcoholic_queries_output():
    if request.method == 'POST':
        add_info.clear()
        form_data = request.form
        question_num = form_data['query_button']
        print(question_num)
        add_info.id = question_num
        if question_num in ['1']:
            return render_template("alcoholic_queries/alcoholic_queries_output1110.html")
        elif question_num in ['2', '4', '9', '12', '13']:
            return render_template("alcoholic_queries/alcoholic_queries_output1010.html")
        elif question_num in ['3', '8']:
            return render_template("alcoholic_queries/alcoholic_queries_output1011.html")
        elif question_num in ['6', '7']:
            return render_template("alcoholic_queries/alcoholic_queries_output0110.html")
        elif question_num == '17':
            return render_template("alcoholic_queries/alcoholic_queries_output_job.html")
        elif question_num == '5':
            return render_template("alcoholic_queries/alcoholic_queries_output1000.html")
        elif question_num == '11':
            return render_template("alcoholic_queries/alcoholic_queries_output0011.html")
        else:
            if question_num in ['10', '14', '15', '16', '18', '19', '20']:
                data = requests.get(f'http://127.0.0.1:5000/query/{question_num}')
            data = data.json()
            if (data != []):
                data = data['reponse']
                print(data)
                return render_template("alcoholic_queries/query_result.html", data=data)
            else:
                return render_template("alcoholic_queries/none_result.html")

@app.route("/none_result.html")
def none_result():
    return render_template("alcoholic_queries/none_result.html")

@app.route("/query_result.html", methods = ['POST'])
def query_result():
    if request.method == 'POST':
        form_data = request.form
        print(add_info.id)
        if add_info.id in ['1']:
            data = requests.get(f'http://127.0.0.1:5000/query/{add_info.id}?id_alc={form_data["alc_id"]}&N={form_data["times"]}&from_date={form_data["start_date"]}&to_date={form_data["end_date"]}')
        elif add_info.id in ['2', '4', '9', '12', '13']:
            data = requests.get(f'http://127.0.0.1:5000/query/{add_info.id}?id_alc={form_data["alc_id"]}&from_date={form_data["start_date"]}&to_date={form_data["end_date"]}')
        elif add_info.id in ['3', '8']:
            data = requests.get(f'http://127.0.0.1:5000/query/{add_info.id}?id_alc={form_data["alc_id"]}&from_date={form_data["start_date"]}&to_date={form_data["end_date"]}&id_ins={form_data["inspector"]}')
        elif add_info.id in ['6', '7']:
            data = requests.get(f'http://127.0.0.1:5000/query/{add_info.id}?N={form_data["times"]}*from_date={form_data["start_date"]}&to_date={form_data["end_date"]}')
        elif add_info.id == '17':
            pass
        elif add_info.id == '5':
            data = requests.get(f'http://127.0.0.1:5000/query/{add_info.id}?id_alc={form_data["alc_id"]}')
        elif add_info.id == '11':
            data = requests.get(f'http://127.0.0.1:5000/query/{add_info.id}?from_date={form_data["start_date"]}&to_date={form_data["end_date"]}&id_ins={form_data["inspector"]}')
        data = data.json()
        if (data != []):
            data = data['reponse']
            return render_template("alcoholic_queries/query_result.html", data=data)
        else:
            return render_template("alcoholic_queries/none_result.html")

@app.route("/inspector_queries.html")
def inspector_queries():
    return render_template("inspector_queries.html")

@app.route("/inspector_output.html", methods = ['POST', 'GET'])
def inspector_output():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        print(form_data)
        return render_template("inspector_output.html", form_data = form_data)

if __name__ == '__main__':
    app.run(debug=True)
