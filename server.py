from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def main_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def home(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        with open('database.txt', 'a') as file:
            file.write(str(data))
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong!! '
