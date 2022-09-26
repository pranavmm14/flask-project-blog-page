#Random bootstrap code file

#use /bootstrap end point to see the change from tut1.py file


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

@app.route("/bootstrap")
def bootstrap():
    name ="Pranav"
    return render_template("bootstrap_code.html", name2=name)


app.run(debug=True)