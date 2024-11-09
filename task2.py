from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/players")
def players_page():
    return render_template("players.html")

@app.route("/contacts")
def contact_page():
    return render_template("contacts.html")

if __name__ == "__main__":
    app.run()