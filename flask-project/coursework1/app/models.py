from app import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    module = db.Column(db.String(100), nullable=False)
    deadline = db.Column(db.Date)
    description = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(100))
    completed = db.Column(db.Boolean, default=False)