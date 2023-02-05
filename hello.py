from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)
app.secret_key = b'oiuhdiofus87y4'

@app.route('/contact/', methods=("GET", "POST"))
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        body = request.form['body']
        print(name, email, body)
        flash("Formularz został ptrzetworzony", "end")
        # redirector
    else:
        flash("Twój formularz nie został wysłany", "start")
    return render_template('contact.html')

@app.route('/redirect/')
def test_redirect():
    return redirect(url_for('main_view'))

@app.route('/main/')
def main_view():
    return render_template('main.html')

@app.route('/check/<string:value>/')
def check_str_value(value):
    return f"Wartość string: {value}"

@app.route('/check/<int:value>/')
def check_int_value(value):
    return f"Wartość int: {value}"

@app.route('/suma/<int:a>/<int:b>/')
def sum_view(a, b):
    return f"Suma {a} + {b} =  {a+b}"

@app.route('/hello1/')
@app.route('/hello/')
def hello():
    return render_template('hello.html', a=201, msg="wiadomosc", b=[1, 2, 3, 4, 5])

@app.route('/base/')
def base_view():
    return render_template('base.html')

def test_hello():
    return "NOWY TEST !!!!!"

#app.add_url_rule('/test/', view_func=test_hello)
app.add_url_rule('/test/', endpoint='test_name', view_func=test_hello)

if __name__ == "__main__":
    app.run(debug=True)