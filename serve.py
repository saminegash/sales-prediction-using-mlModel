# serve.py

from flask import Flask
from flask import render_template

# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template


@app.route("/")
def home():
    message = "sami"
    return render_template('home.html', message=message)


# a route where we will display a welcome message via an HTML template
@app.route("/predict")
def predict():
    message = "sami"
    return render_template('index.html', message=message)

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
