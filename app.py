from flask import Flask, render_template, request, redirect, url_for
from database import db
from models import Helper, Booking
from assignment import assign_helper
from assignment import auto_reassign

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///helpers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/dashboard')
def dashboard():
    helpers = Helper.query.all()
    return render_template("dashboard.html", helpers=helpers)


@app.route('/toggle_status/<int:helper_id>')
def toggle_status(helper_id):
    helper = Helper.query.get(helper_id)
    if helper.status == "Available":
        helper.status = "Busy"
    else:
        helper.status = "Available"
    db.session.commit()
    return redirect(url_for('dashboard'))


@app.route('/add_helper_page')
def add_helper_page():
    return render_template("add_helper.html")


@app.route('/add_helper', methods=['POST'])
def add_helper():
    helper = Helper(
        name=request.form['name'],
        skill=request.form['skill'],
        latitude=float(request.form['latitude']),
        longitude=float(request.form['longitude']),
        rating=float(request.form['rating']),
        status="Available"
    )
    db.session.add(helper)
    db.session.commit()
    return redirect(url_for('dashboard'))


@app.route('/book', methods=['POST'])
def book_service():
    booking = Booking(
        user_name=request.form['name'],
        service_type=request.form['service'],
        latitude=float(request.form['latitude']),
        longitude=float(request.form['longitude'])
    )

    db.session.add(booking)
    db.session.commit()

    helper = assign_helper(booking)

    if not helper:
        helper = auto_reassign(booking)

    return render_template("result.html", helper=helper)


if __name__ == '__main__':
    app.run(debug=True)
