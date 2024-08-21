from app import db


class EnergyUsage(db.Model):
    __tablename__ = 'devices'  # Corrected to use __tablename__
    
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, nullable=False)
    usage = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<EnergyUsage {self.device_id} - {self.usage}>"
