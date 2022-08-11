from flask import Flask, render_template

app = Flask("projeto")

@app.route("/")
def home():
    return render_template('home.html', context={"msg":"Sucesso"})

if __name__ == "__main__":
    app.run(debug=True)