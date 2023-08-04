import random
from datetime import datetime, timedelta
from bot.bot import db, User, Reservation

# Example data for students' names in Russian and English
student_names_ru = [
    "Иван Иванов", "Петр Смирнов", "Александр Кузнецов", "Максим Морозов", "Сергей Васильев"
]
student_names_en = [
    "John Smith", "Alice Johnson", "Michael Brown", "Emily Davis", "William Wilson"
]

# Generate example data for users


def generate_users():
    users = []

    for i in range(5):
        name_ru = random.choice(student_names_ru)
        name_en = random.choice(student_names_en)
        phone = f"+7{random.randint(1000000000, 9999999999)}"
        room = f"Room {random.randint(100, 199)}"
        user = User(chat_id=random.randint(1000000000, 9999999999),
                    room_number=room, phone_number=phone)
        users.append(user)

    return users

# Generate example data for reservations


def generate_reservations(users):
    reservations = []
    now = datetime.now()

    for user in users:
        for _ in range(random.randint(3, 8)):
            date = now.strftime("%Y-%m-%d")
            time = f"{random.randint(8, 20)}:00"
            notification_preference = random.choice([0, 15])
            reservation = Reservation(
                user_id=user.id, date=date, time=time, notification_preference=notification_preference)
            reservations.append(reservation)
            now += timedelta(days=random.randint(1, 7))

    return reservations


# Run the script to generate and insert example data into the database
if __name__ == "__main__":
    db.create_all()
    example_users = generate_users()
    db.session.add_all(example_users)
    db.session.commit()

    example_reservations = generate_reservations(example_users)
    db.session.add_all(example_reservations)
    db.session.commit()
