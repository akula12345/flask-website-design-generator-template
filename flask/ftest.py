from flask import Flask, render_template, redirect ,url_for
import random

app = Flask(__name__)


bodyStyles = ["body-yellow-blue", "body-beige-white", "body-blue-pink", "body-pink-orange"]
windowStyles = ["window-1", "window-2", "window-3", "window-4"]
btnStyles = ["btn-1", "btn-2", "btn-3", "btn-4"]


@app.route("/")
def index():
    randomStyle = [bodyStyles[random.randint(0,3)], windowStyles[random.randint(0, 3)], btnStyles[random.randint(0, 3)]]
    return render_template('index.html', bodyStyle=randomStyle[0], windowStyle=randomStyle[1], btnStyle=randomStyle[2])

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for("index")), 404

if __name__ == "__main__":
    app.run(debug=True)