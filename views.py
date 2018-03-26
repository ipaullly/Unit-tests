from Project2 import app

@app.route('/')
def index():
    return 'Hello World!'