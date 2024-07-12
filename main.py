from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def films():
    return render_template("index.html") # Внутри () пишем название html-файла в кавычках

@app.route("/person/")
def person():
    return render_template("main.html") # Внутри () пишем название html-файла в кавычках

if __name__ == '__main__':
    app.run()