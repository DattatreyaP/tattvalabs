from flask import Flask, render_template,redirect, url_for, request

app = Flask(__name__)


@app.route('/cal' )
def index():
    return render_template("index.html")


@app.route('/submit',  methods=['GET', 'POST'])
def index1():
    v1 = request.form.get('value1', type=int)
    v2 = request.form.get('value2', type=int)
    return "Addition is "+str(v1+v2)

@app.route('/submit1',  methods=['GET', 'POST'])
def index2():
    value1 = request.form['value1']
    value2 = request.form['value2']
    v1 = request.form.get('value1', type=int)
    v2 = request.form.get('value2', type=int)
    return "Subtraction  is " + str(v1 - v2)


@app.route('/submit2',  methods=['GET', 'POST'])
def index3():
    value1 = request.form['value1']
    value2 = request.form['value2']
    v1 = request.form.get('value1', type=int)
    v2 = request.form.get('value2', type=int)
    return "Mul is " + str(v1 * v2)


@app.route('/submit3',  methods=['GET', 'POST'])
def index4():
    value1 = request.form['value1']
    value2 = request.form['value2']
    v1 = request.form.get('value1', type=int)
    v2 = request.form.get('value2', type=int)
    return "Division is " + str(v1 / v2)






if __name__ == "__main__":
    app.run(port=8080)