from my_app import app, render_template, url_for

@app.route('/')
def index():
    return render_template('index.html')
