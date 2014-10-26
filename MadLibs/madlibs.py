from flask import Flask, render_template, request, redirect, url_for
from random import choice, sample

app = Flask(__name__)

COMPLIMENTS = ["pretty", "smart", "joyful", "gracious"]

@app.route("/")
def display_home():
	return render_template("index.html")


@app.route("/new/madlib")
def display_madlib():
	name = request.args.get("person")
	adjective = request.args.get("adjective")
	wants_compliments = request.args.get("compliments")

	if not name or not adjective:
		return "Please fill out all fields!"

	if wants_compliments:
		compliment_list = make_compliments()
	else:
		compliment_list = None

		# how do I get rid of the form data from the URL??
	return render_template("index.html", name=name, adjective=adjective, compliments=compliment_list)
	# return redirect("index.html", name=name, adjective=adjective, compliments=compliment_list)

def make_compliments():
	compliments = sample(COMPLIMENTS, 3)
	return compliments

if __name__ == "__main__":
	app.run(debug=True)