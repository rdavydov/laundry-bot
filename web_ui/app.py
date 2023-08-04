from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/laundry.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, unique=True, nullable=False)
    room_number = db.Column(db.String(10), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(5), nullable=False)
    # 0: On time, 15: 15 minutes before
    notification_preference = db.Column(db.Integer, default=0)


@app.route('/')
def index():
    reservations = Reservation.query.all()
    return render_template('index.html', reservations=reservations)


@app.route('/edit/<int:reservation_id>', methods=['GET', 'POST'])
def edit_reservation(reservation_id):
    reservation = Reservation.query.get(reservation_id)

    if request.method == 'POST':
        # Update reservation data in the database
        date = request.form['date']
        time = request.form['time']
        notification_preference = int(request.form['notification_preference'])
        reservation.date = date
        reservation.time = time
        reservation.notification_preference = notification_preference
        db.session.commit()
        return redirect('/')

    return render_template('edit_reservation.html', reservation=reservation)


if __name__ == '__main__':
    app.run(debug=True)
