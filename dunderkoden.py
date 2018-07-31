# Andreas dunderkod, johan är noob
from flask import render_template
from flask import Flask
app = Flask("Server")

@app.route("/")
def hello():
	return render_template('hemsida.html')


