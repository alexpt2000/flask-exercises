git init

git add .

git commit -m "first commit"

git remote add origin https://github.com/alexpt2000/flask-exercises.git

git push -u origin master

***Task 1
Done


***Task 2

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()


python hello.py

***Task 3
Done

***Task 4
@app.route('/hello/<name>')
def TypeName(name=None):
    return render_template('index.html', name=name)


***Task 5
# Take the value for GET methods
@app.route('/hello/', methods=['GET'])
def SubmitNameByGET():
	return render_template('index.html', name = request.args.get('name'))


***Task 6
# Take the value for POST methods
@app.route('/hello/', methods=['POST'])
def SubmitNameByPOST():
    return render_template('index.html', name=request.form['name'])


