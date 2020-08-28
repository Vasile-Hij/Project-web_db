from flask import Flask, render_template, url_for, request, redirect
from flask import send_from_directory
import csv
app = Flask(__name__)
print(__name__)

@app.route('/') #template
def my_home():
    return render_template('index.html')

#automatisation of pages
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

#creating a databases.txt with messages from CONTACT
#def write_to_file(data):
 #   with open('database.txt', mode='a') as database:
    #    email = data["email"]
    #    subject = data["subject"]
    #    message = data["message"]
    #    file = database.write(f'\n{email},{subject},{message}')

#creating a databases.csv with messages from CONTACT
#https://docs.python.org/3/library/csv.html
def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

#CONTACT page form
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #write_to_file(data)
            write_to_csv(data)
            return redirect('/Thankyou.html')
        except:
            return 'Did not saved to DB'
    else:
        return 'Something went wrong. Try again!'



#get original from
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#accessing-request-data