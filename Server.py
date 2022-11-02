import csv
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:any_page>")
def any(any_page):
    return render_template(any_page)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wong'

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])