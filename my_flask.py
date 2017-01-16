from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	with open("/var/log/syslog",'r')as inp:
		f=inp.readlines()
		for i in range(-1,-6,-1):
			print f[i]
	return "Hello World!"

if __name__ == "__main__":
    app.run()
