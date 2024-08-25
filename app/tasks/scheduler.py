from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler()


def job_function():
    from app import create_app
    from app.utils.data_generator import generate_energy_data

    try:
        app = create_app()
        with app.app_context():
            generate_energy_data()
    except Exception as e:
        print(f"Error in job function: {e}")


def start_scheduler():
    scheduler.add_job(func=job_function, trigger="interval", minutes=5)
    scheduler.start()
