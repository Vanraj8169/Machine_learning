from flask import Flask, render_template, request

app = Flask(__name__)
'''
Jinja Template
{# .... #} - comments
{{}} - expression to print output in html
{%%} - Condition
'''

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')


## Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template('result.html', results=res)


if __name__ == "__main__":
    app.run(debug=True)
