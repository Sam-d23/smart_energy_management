from app import db


class EnergyUsage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String(50))
    usage = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)
