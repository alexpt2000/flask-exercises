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


