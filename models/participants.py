from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Participants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Participants(id={self.id}, Name={self.Name}, Surname={self.Surname}, email={self.email})"
