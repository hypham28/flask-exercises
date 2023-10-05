from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        number = request.form.get("number")
        if number.isdigit():
            number = int(number)
            return redirect(url_for("result", number=number))
    return render_template("index.html")

@app.route("/result/<int:number>")
def result(number):
    is_even = "Even" if number % 2 == 0 else "Odd"
    return render_template("result.html", number=number, is_even=is_even)

if __name__ == "__main__":
    app.run(debug=True)
