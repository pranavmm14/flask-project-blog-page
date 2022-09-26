from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World! \nThis is Pranav!</p>"
    return render_template("index1.html")

@app.route("/about")
def about():
    name1 ="<Custom name>"
    # return "<p>Hey Pranav!</p>"
    return render_template("about1.html", name= name1)

app.run(debug=True)