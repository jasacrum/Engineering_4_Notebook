from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

app = Flask(__name__)

Blue = False
Green = False

@app.route("/", methods=["GET","POST"])
def index():
	Blue = GPIO.input(17)
	Green = GPIO.input(18)
	if request.method == "POST":
		msg = request.form.get("submitBtn")
		if msg == " ":
		#	msg = "Blue is "+ ("off" if Blue else "on")+" Green is "+ ("off" if Green else "off")
			Blue = not Blue
			GPIO.output(17,Blue)
		elif msg == "  ":
		#	msg = "Blue is "+ ("off" if Blue else "off")+" Green is "+ ("off" if Green else "on")
			Green = not Green
			GPIO.output(18,Green)

	else:
		GPIO.output(17,GPIO.LOW)
		GPIO.output(18,GPIO.LOW)

		msg = "Both lights off"
	Booten = "Turn Blue "+ ("off" if Blue else "on")
	Looten = "Turn Green "+ ("off" if Green else "on")
	msg = "Blue is "+ ("on" if Blue else "off")+" Green is "+ ("on" if Green else "off")
	return render_template("index.html", msg=msg, Booten=Booten, Looten=Looten)

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=80)
