# serve.py

from flask import Flask
from flask import render_template
# import pandas as pd
# creates a Flask application, named app
app = Flask(__name__)
# prediction = pd.read_csv('notebook/data/Rossman_predictions.csv')
# a route where we will display a welcome message via an HTML template


@app.route("/")
def home():
    return render_template('home.html', message="")


# a route where we will display a welcome message via an HTML template
@app.route("/predict")
def predict():
    """
    For rendering result on HTML GUI
    """
    return render_template('index.html', message="")

# a route where we will display a welcome message via an HTML template


@app.route("/about")
def about():
    message = "sami"
    return render_template('about.html', message=message)

# a route where we will display a welcome message via an HTML template


@app.route("/visual")
def visual():
    message = "sami"
    return render_template('visual.html', message=message)


# run the application
if __name__ == "__main__":
    app.run(debug=True)
