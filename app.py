from flask import Flask

app = Flask("projeto")

@app.route("/")
def home():
    return "Homepage"

if __name__ == "__main__":
    app.run()