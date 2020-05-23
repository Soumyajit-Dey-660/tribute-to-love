from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html', title="Special-gift")

@app.route('/funny')
def funny():
    return render_template('funny.html', title="Funny")

@app.route('/story')
def story():
    return render_template('story.html', title="Story")

@app.route('/special')
def special():
    return render_template('special.html', title="Special")

@app.route('/developer')
def developer():
    return render_template('developer.html', title="Developer")

if __name__ == "main":
    app.run(debug=True)