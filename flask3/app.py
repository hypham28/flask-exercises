from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

registered_users = {}

valid_organizations = [
    "Organization 1",
    "Organization 2",
    "Organization 3",
    "Organization 4",
    "Organization 5",
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/registration")
def registration():
    return render_template("registration.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    organization = request.form.get("organization")

    if not name or not organization:
        return "Both name and organization are required. <a href='/registration'>Back to registration</a>"

    if organization not in valid_organizations:
        return "Invalid organization selected. <a href='/registration'>Back to registration</a>"

    registered_users[name] = organization
    return redirect(url_for("user_list"))

@app.route("/user_list")
def user_list():
    return render_template("user_list.html", users=registered_users)

if __name__ == "__main__":
    app.run(debug=True)
