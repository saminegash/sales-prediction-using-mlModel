# serve.py

from flask import Flask
from flask import render_template
from flask import request
import csv
from datetime import datetime
from flask import json
import pandas as pd
# import pandas as pd
# creates a Flask application, named app
app = Flask(__name__)
# prediction = pd.read_csv('notebook/data/Rossman_predictions.csv')
# a route where we will display a welcome message via an HTML template
# data = pd.read_csv('.data/avgpredfile.csv')
# date_column = data['Date'].to_list()
# sales_column = data['Sales'].to_list()
# sales_column = ["{:.2f}".format(x) for x in sales_column]
# date_columns = json.dumps({'date': date_column})
# sales_columns = json.dumps({'sales': sales_column})


@app.route("/")
def home():
    return render_template('home.html')


# a route where we will display a welcome message via an HTML template
# @app.route("/predict", methods=['POST', 'GET'])
# def predict():
#     """
#     For rendering result on HTML GUI
#     """
#     with open('.data/predictionfile.csv') as csv_file:
#         data = csv.DictReader(csv_file, delimiter=',')
#         plot_file = data

#     if request.method == "GET":
#         message = "Select date and click on pridict button to see the average sales prediction"

#     elif request.method == "POST":
#         date_fet = request.form.get('pred_date')
#         prediction = None
#         with open('.data/avgpredfile.csv') as csv_file:
#             data = csv.DictReader(csv_file, delimiter=',')
#             for row in data:
#                 if row['Date'] == date_fet:
#                     prediction = row['Sales']
#                     prediction = "{:.2f}".format(float(prediction))
#         if(prediction):
#             message = "Sales Prediction for date {} is {}".format(
#                 date_fet, prediction)
#         else:
#             message = "Incorrect Date: you have to select date between: 01 Aug, 2015(2015-08-01) and 17 Sep, 2015(2015-09-17)"
#     return render_template('index.html', message=message, labels=date_columns, data=sales_columns)

# a route where we will display a welcome message via an HTML template


@app.route("/about")
def about():
    return render_template('about.html')

# a route where we will display a welcome message via an HTML template


# @app.route("/visual")
# def visual():
#     message = "sami"
#     return render_template('visual.html', message=message)


# run the application
if __name__ == "__main__":
    app.run(debug=True)
