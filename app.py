from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


# @app.route("/<string:page_name>")
# def html_page(page_name):
#     return render_template(page_name)

@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/works.html")
def works():
    return render_template("works.html")


@app.route("/work.html")
def work():
    return render_template("work.html")


@app.route("/contact.html")
def home():
    return render_template("contact.html")


@app.route("/thankyou.html")
def thankyou():
    return render_template("thankyou.html")


if __name__ == "__main__":
    app.run()
