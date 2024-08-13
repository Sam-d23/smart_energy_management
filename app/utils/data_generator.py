def generate_energy_data():
    import random
    from datetime import datetime

    from app import db
    from app.models import EnergyUsage


    devices = ['device_1', 'device_2', 'device_3']
    for device in devices:
        usage = random.uniform(0.1, 5.0)
        new_usage = EnergyUsage(
                device_id=device,
                usage=usage,
                timestamp=datetime.now()
        )
        db.session.add(new_usage)
    db.session.commit()
