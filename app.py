from flask import Flask, render_template, request, redirect

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


def write_to_file(data):
    with open('db.txt', mode="a") as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f"\n{email},{subject},{message}")


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect("thankyou.html")
    else:
        print("something went wrong, please try again")


if __name__ == "__main__":
    app.run()
