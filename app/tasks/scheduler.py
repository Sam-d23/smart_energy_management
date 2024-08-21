from apscheduler.schedulers.background import BackgroundScheduler
from app.utils.data_generator import generate_energy_data


scheduler = BackgroundScheduler()


def start_scheduler():
    from app import db
    from app.models import EnergyUsage

    def job_function():

        generate_energy_data()
    
    scheduler.add_job(func=job_function, trigger="interval", minutes=5)
    scheduler.start()
