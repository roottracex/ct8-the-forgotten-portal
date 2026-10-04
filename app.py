from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/old-portal/")
def old_portal():
    return render_template("old_portal.html")


@app.route("/robots.txt")
def robots():
    return app.send_static_file("robots.txt")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)