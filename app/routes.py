from flask import render_template
from app import app

useroffers = [
    {'title': 'I can help debug Python files.'},
    {'title': 'I can peer-review academic writing.'},
    {'title': 'Down to give advice on your resume!'}
]

userrequests = [
    {'title': 'I need help fixing my doornob.'},
    {'title': 'I need help with my math homework.'},
    {'title': 'Teach me to bake a cake.'},
]



@app.route("/")
@app.route("/index")
def index():
    return render_template("mainpage.html", useroffers=useroffers, userrequests=userrequests)