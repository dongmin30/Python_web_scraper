from flask import Flask

app = Flask("JobScrapper")

@app.route("/")
def home():
    return 'hey there!'

app.run("127.0.0.1")