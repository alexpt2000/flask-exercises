from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/hello/<name>')
def TypeName(name=None):
    return render_template('index.html', name=name)


# Take the value for GET methods
@app.route('/hello/', methods=['GET'])
def SubmitNameByGET():
	return render_template('index.html', name = request.args.get('name'))


# Take the value for POST methods
@app.route('/hello/', methods=['POST'])
def SubmitNameByPOST():
    return render_template('index.html', name=request.form['name'])

if __name__ == "__main__":
	app.run()
