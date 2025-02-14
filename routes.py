from flask import render_template, request, redirect, flash, session
from app import app
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/")
def start():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            return redirect("/reservation")
    else:
        return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email já cadastrado!", "error")
            return redirect("/signup")

        else:
            hashed_password = generate_password_hash(password)
            new_user = User(name, email, hashed_password)

            db.session.add(new_user)
            db.session.commit()
            return redirect("/login")
    else:
        return render_template("signup.html")

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect("/")

@app.route("/reservation")
def reservation():
    if "user_id" in session:
        return render_template("reservation.html")
    else:
        return redirect("/login")