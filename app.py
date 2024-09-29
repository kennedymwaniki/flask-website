from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


# @app.route("/<string:page_name>")
#this will render the page based on the #\n name passed in the url.
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


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        fieldnames = ['email', 'subject', 'message']
        csv_writer = csv.DictWriter(database, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerow({
            'email': data['email'],
            'subject': data['subject'],
            'message': data['message']
        })


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    try:
        if request.method == 'POST':
            data = request.form.to_dict()
            write_to_csv(data)
            # write_to_file(data)
            return redirect("thankyou.html")
        else:
            print("something went wrong, please try again")
    except:
        return "could not save to database"


if __name__ == "__main__":
    app.run()
