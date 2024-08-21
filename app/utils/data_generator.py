from app.models import EnergyUsage
from datetime import datetime, timedelta
import random


def generate_energy_data():
    from app import db
    devices = ['device_1', 'device_2', 'device_3']
    
    # Define the start date and end date for one week
    start_date = datetime(2024, 1, 1, 0, 0, 0)
    end_date = start_date + timedelta(days=6, hours=23, minutes=59, seconds=59)

    # Loop through each hour in the week
    current_time = start_date
    while current_time <= end_date:
        for device in devices:
            usage = round(random.uniform(0.5, 5.0), 2)
            temperature = round(random.uniform(18, 35), 1)
            humidity = round(random.uniform(30, 90), 1)

            new_usage = EnergyUsage(
                device_id=device,
                usage=usage,
                timestamp=current_time,
                temperature=temperature,
                humidity=humidity
            )

            db.session.add(new_usage)
        
        # Move to the next hour
        current_time += timedelta(hours=1)

    db.session.commit()
