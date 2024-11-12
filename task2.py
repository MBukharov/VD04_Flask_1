from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    content = {
        'active_page1' : 'active'
    }
    return render_template("index.html", **content)

@app.route("/players")
def players_page():
    content = {
        'active_page2': 'active'
    }
    return render_template("players.html", **content)

@app.route("/contacts")
def contact_page():
    content = {
        'active_page3': 'active'
    }
    return render_template("contacts.html", **content)

if __name__ == "__main__":
    app.run()