from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def check_number(number):
    try:
        num = int(number)
        if num % 2 == 0:
            return f"{num} is an even number."
        else:
            return f"{num} is an odd number."
    except ValueError:
        return "Not a valid integer."

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("number")
        return redirect(url_for("result", number=user_input))
    return render_template("index.html")

@app.route("/result")
def result():
    user_input = request.args.get("number")
    if user_input is None:
        return render_template("result.html", error="No query parameter provided.")
    message = check_number(user_input)
    return render_template("result.html", user_input=user_input, message=message)

if __name__ == "__main__":
    app.run(debug=True)
