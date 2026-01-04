from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

# --- Routing ---

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

# --- Data Persistence ---

def write_to_file(data):
  with open('database.txt', mode='a') as database:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        # Define dangerous characters that trigger formulas in Excel/Calc
        dangerous_chars = ('=', '+', '-', '@', '\t', '\r')
        
        # Sanitize each field
        processed_data = []
        for key in ["email", "subject", "message"]:
            value = data[key]
            # If the value starts with a dangerous char, prepend a single quote
            if value.startswith(dangerous_chars):
                value = f"'{value}" 
            processed_data.append(value)

        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(processed_data)

# --- Form Handling ---

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
      try:
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
      except:
        return 'did not save to database'
    else:
      return 'something went wrong. Try again!!'
