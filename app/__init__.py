import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from apscheduler.schedulers.background import BackgroundScheduler

from .config import Config
from .tasks.scheduler import start_scheduler

db = SQLAlchemy()
migrate = Migrate()
scheduler = BackgroundScheduler()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
            'DATABASE_URI',
            'postgresql://user:password@localhost:5432/energy_db'
    )

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    start_scheduler()

    with app.app_context():
        from .controllers.energy_controller import energy_bp
        app.register_blueprint(energy_bp, url_prefix='/api')

        from .models.energy import EnergyUsage

    return app
