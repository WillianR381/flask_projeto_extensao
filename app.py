from flask import Flask

app = Flask("projeto")

@app.route("/")
def foi():
    return "foi"

app.run()