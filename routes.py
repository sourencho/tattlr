from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True  # Only include this while you are testing your app

@app.route("/")
def hello():
    return "Fuck you souren"

if __name__ == "__main__":
    app.run(host="0.0.0.0")