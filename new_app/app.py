from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:Njoroge@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Create the tables
with app.app_context():
    db.create_all()

# Add a new user to the User table
with app.app_context():
    new_user = User(name="Jane Doe", email="janedoe@example.com")
    db.session.add(new_user)
    db.session.commit()

# Verify the data addition
with app.app_context():
    user = User.query.filter_by(email="janedoe@example.com").first()
    print(user.name)  # Output: Jane Doe

if __name__ == "__main__":
    app.run(debug=True)

