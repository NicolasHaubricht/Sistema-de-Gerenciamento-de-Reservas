from flask import request, redirect, url_for, render_template, flash, session
from app import app
from models import db, User, Reservation
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

@app.route("/")
def home():
    return render_template("welcome.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            return redirect(url_for("reservation_list"))
        
        return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            return redirect(url_for("signup"))

        hashed_password = generate_password_hash(password)
        new_user = User(name, email, hashed_password)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("signup.html")

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("home"))

@app.route("/reservations", methods=["GET"])
def reservation_list():
    if "user_id" not in session:
        return redirect(url_for("login"))

    reservas = Reservation.query.all()
    return render_template("reservations.html", reservas=reservas)

@app.route("/create-reservation", methods=["GET", "POST"])
def create_reservation():
    if "user_id" not in session:
        return redirect(url_for("login"))
    else:
        if request.method == "POST":
            restaurant_name = request.form.get("restaurant_name")
            date_time_str = request.form.get("date_time")
            num_people = request.form.get("num_people")

            if not restaurant_name or not date_time_str or not num_people:
                return redirect(url_for("create_reservation"))

            try:
                date_time = datetime.strptime(date_time_str, "%Y-%m-%dT%H:%M")
                num_people = int(num_people)
            except ValueError:
                return redirect(url_for("create_reservation"))

            new_reservation = Reservation(restaurant_name=restaurant_name, date_time=date_time,num_people=num_people)

            db.session.add(new_reservation)
            db.session.commit()

            return redirect(url_for("reservation_list"))
        
        return render_template("create_reservation.html")


@app.route("/edit-reservation/<int:id>", methods=["GET", "POST"])
def edit_reservation(id):
    reservation = Reservation.query.get_or_404(id)

    if request.method == "POST":
        reservation.restaurant_name = request.form["restaurant_name"]
        reservation.date_time = datetime.strptime(request.form["date_time"], "%Y-%m-%dT%H:%M")
        reservation.num_people = int(request.form["num_people"])
        db.session.commit()
        return redirect(url_for("reservation_list"))

    return render_template("edit_reservation.html", reservation=reservation)

@app.route("/delete-reservation/<int:id>")
def delete_reservation(id):
    reservation = Reservation.query.get_or_404(id)
    db.session.delete(reservation)
    db.session.commit()

    return redirect(url_for("reservation_list"))