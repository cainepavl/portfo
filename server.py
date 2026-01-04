from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

# -- Routing --

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

# -- Data Persistence --

def write_to_csv(data):
    """
    Persists contact form data to CSV with sanitization to prevent CSV Injection.
    """
    # Dangerous characters that can trigger formula execution in Excel/Calc
    dangerous_chars = ('=', '+', '-', '@')
    
    with open('database.csv', mode='a', newline='', encoding='utf-8') as database2:
        email = data.get("email", "")
        subject = data.get("subject", "")
        message = data.get("message", "")

        # Sanitize inputs: if a field starts with a dangerous char, prepend a single quote
        # This forces spreadsheet software to treat the field as literal text
        sanitized_row = []
        for field in [email, subject, message]:
            if field.startswith(dangerous_chars):
                field = f"'{field}"
            sanitized_row.append(field)

        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(sanitized_row)

# -- Form Handling --

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            # Convert immutable multidict to standard dict for processing
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except Exception as e:
            # Log the error internally (in a real app) and return a generic error
            return 'System error: Data could not be saved.'
    else:
        return 'Invalid request method. Please use the contact form.'

if __name__ == "__main__":
    app.run(debug=True)
