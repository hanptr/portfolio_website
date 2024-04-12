from flask import (Flask,
                   render_template,
                   send_from_directory,
                   url_for,
                   request)
import babelFlask


app = Flask(__name__)
babel = babelFlask.BabelFlask(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def generic(page_name):
    return render_template(f"{page_name}.html")


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        return "form submitted with data"
    else:
        return "oops"

