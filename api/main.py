from flask import Flask, request, render_template, url_for, session, flash
from flask_restful import Api, Resource, reqparse, abort
from werkzeug.utils import redirect
from api.tables import TABLE_CLASSES
from apis import *
from additional_info import AddInfo
import requests

template_dir = '../templates'
app = Flask(__name__, template_folder=template_dir)
api = Api(app)
app.secret_key = "vutvereznyk"
BASE = "http://127.0.0.1:5000/"

add_info = AddInfo()

#api_backend.add_resource(Hello, "/hello")
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
    tables = TABLE_CLASSES

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
    cols = TABLE_COLUMNS[table][1:]

    if request.method == "POST":
        data = request.form["input_row"].split(",")
        print(data)
        try:
            if (len(data) != len(cols)):
                flash(f"Invalid number of arguments")
            else:
                data_for_query = dict(zip(cols, data))
                print(data_for_query)
                query_string = BASE + "edit/{}?".format(table)
                for key in data_for_query:
                    query_string += key + "=" + data_for_query[key] + "&"
                print(query_string[:-1])
                requests.delete(query_string[:-1]).json()
                flash(f"Data removed from table {table}")
        except:
            flash(f"Invalid input data")

    return render_template("edit_form.html", table=table, cols=cols)


@app.route("/insert_data", methods=["POST", "GET"])
def insert_data():
    table = session["table_to_edit"]
    cols = TABLE_COLUMNS[table][1:]

    if request.method == "POST":
        data = request.form["input_row"].split(",")
        print(data)
        try:
            if (len(data) != len(cols)):
                flash(f"Invalid number of arguments")
            else:
                data_for_query = dict(zip(cols, data))
                print(data_for_query)
                query_string = BASE + "edit/{}?".format(table)
                for key in data_for_query:
                    query_string += key + "=" + data_for_query[key] + "&"
                print(query_string[:-1])
                requests.put(query_string[:-1]).json()
                flash(f"New row inserted into table {table}")
        except:
            flash(f"Invalid input data")

    return render_template("edit_form.html", table=table, cols=cols)


# @app.route("/alcoholic_queries.html")
# def alcoholic_queries():
#     return render_template("alcoholic_queries/alcoholic_queries.html")

@app.route("/alcoholic_queries_output.html", methods = ['POST'])
def alcoholic_queries_output():
    if request.method == 'POST':
        add_info.clear()
        form_data = request.form
        question_num = form_data['query_button']
        add_info.id = question_num
        if question_num in ['1', '9']:
            return render_template("alcoholic_queries/alcoholic_queries_output1110.html")
        elif question_num in ['2', '4', '12', '13']:
            return render_template("alcoholic_queries/alcoholic_queries_output1010.html")
        elif question_num in ['3']:
            return render_template("alcoholic_queries/alcoholic_queries_output0111.html")
        elif question_num in ['8']:
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
            print('----------------------------')
            print(data)
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
        if add_info.id in ['1', '9']:
            data = requests.get(f'http://127.0.0.1:5000/query/{add_info.id}?id_alc={form_data["alc_id"]}&N={form_data["times"]}&from_date={form_data["start_date"]}&to_date={form_data["end_date"]}')
        elif add_info.id in ['2', '4', '12', '13']:
            data = requests.get(f'http://127.0.0.1:5000/query/{add_info.id}?id_alc={form_data["alc_id"]}&from_date={form_data["start_date"]}&to_date={form_data["end_date"]}')
        elif add_info.id in ['3']:
            data = requests.get(f'http://127.0.0.1:5000/query/{add_info.id}?N={form_data["times"]}&from_date={form_data["start_date"]}&to_date={form_data["end_date"]}&id_ins={form_data["inspector"]}')
        elif add_info.id in ['8']:
            data = requests.get(f'http://127.0.0.1:5000/query/{add_info.id}?id_alc={form_data["alc_id"]}&from_date={form_data["start_date"]}&to_date={form_data["end_date"]}&id_ins={form_data["inspector"]}')
        elif add_info.id in ['6', '7']:
            data = requests.get(f'http://127.0.0.1:5000/query/{add_info.id}?N={form_data["times"]}&from_date={form_data["start_date"]}&to_date={form_data["end_date"]}')
        elif add_info.id == '17':
            data = requests.get(f'http://127.0.0.1:5000/query/{add_info.id}?job_name={form_data["job"]}');
        elif add_info.id == '5':
            data = requests.get(f'http://127.0.0.1:5000/query/{add_info.id}?id_alc={form_data["alc_id"]}')
        elif add_info.id == '11':
            data = requests.get(f'http://127.0.0.1:5000/query/{add_info.id}?from_date={form_data["start_date"]}&to_date={form_data["end_date"]}&id_ins={form_data["inspector"]}')
        data = data.json()
        print('----------------------------')
        print(data)
        if (data != []):
            data = data['reponse']
            return render_template("alcoholic_queries/query_result.html", data=data)
        else:
            return render_template("alcoholic_queries/none_result.html")

@app.route("/inspector_output.html", methods = ['POST'])
def inspector_output():
    if request.method == 'POST':
        form_data = request.form
        data1 = requests.get(f'http://127.0.0.1:5000/query/21?fname={form_data["fname"]}&lname={form_data["lname"]}')
        data2 = requests.get(f'http://127.0.0.1:5000/query/22?fname={form_data["fname"]}&lname={form_data["lname"]}')
        data1 = data1.json()
        data2 = data2.json()
        data1 = data1['reponse']
        data2 = data2['reponse']
        return render_template("inspector_output.html", data1=data1, data2=data2)
    
@app.route("/search_alc.html", methods = ['POST'])
def alcoholic_output():
    if request.method == 'POST':
        form_data = request.form
        data = requests.get(f'http://127.0.0.1:5000/query/23?fname={form_data["fname"]}&lname={form_data["lname"]}')
        print(data.content)
        data = data.json()
        data = data['reponse']
        return render_template("search_alc.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)
