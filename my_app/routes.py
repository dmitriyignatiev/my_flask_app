from my_app import app, render_template

@app.route('/')
def index():
    return render_template('index.html')
