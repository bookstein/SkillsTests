from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def display_home():
	return render_template("index.html")


@app.route("/new/madlib")
def display_madlib():
	name = request.args.get("person")
	adjective = request.args.get("adjective")
	return render_template("index.html", name=name, adjective=adjective)


if __name__ == "__main__":
	app.run(debug=True)