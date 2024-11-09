from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def timenow():
    now = datetime.now()
    date = now.strftime("%d.%m.%Y")
    time = now.strftime("%H:%M:%S")
    html = f"""
        <div style='text-align: center; font-size:50px;margin-top:100px;color:#111111'>
        <h1> {time}</h1>
        <h1> {date}</h1>
        </div>
    """
    return html

if __name__ == "__main__":
    app.run()