from app import flaskApp

@flaskApp.route("/")
@flaskApp.route("/index")
def index():
    return "hello world!"