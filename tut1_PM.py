from flask import Flask,render_template

app = Flask(__name__)


import write_name

@app.route("/")
def hello_world():
    # return "<p>Hello, World! \nThis is Pranav!</p>"
    return render_template("index_PM.html")

@app.route("/about")
def about():
    # name1 = "<Custom name>"
    file_obj = open("User.txt","r")
    name1 = file_obj.readline()
    name1= name1.strip("Name : ")
    if name1 == "":
        name1 ="Unnamed"
    name1 = name1[:25]
    # name1 = input("Enter Name to proceed to about page:")
    # return "<p>Hey Pranav!</p>"
    return render_template("about_PM.html", name= name1)

app.run(debug=True)