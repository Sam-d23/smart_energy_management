from apscheduler.schedulers.background import BackgroundScheduler
from app.utils.data_generator import generate_energy_data


scheduler = BackgroundScheduler()

def start_scheduler():
    scheduler.add_job(func=generate_energy_data, trigger="interval", minutes=5)
    scheduler.start()
