from flask import (Flask,
                   render_template,
                   send_from_directory,
                   url_for,
                   request,
                   redirect)
import babelFlask
import dbHandler
import email_sender

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
        email_sender.EmailSender(data)
        dbHandler.DbHandler.write_to_file(data)
        # return redirect("form_acceptance")
        return render_template("form_acceptance.html", data=data)
    else:
        return "oops"

