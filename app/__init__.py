from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from apscheduler.schedulers.background import BackgroundScheduler
from app.config import Config, TestingConfig


db = SQLAlchemy()
migrate = Migrate()
scheduler = BackgroundScheduler()


def initialize_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def initialize_scheduler(app):
    env = app.config.get('ENV', 'development')
    if env in ['production', 'development']:
        with app.app_context():
            from app.tasks.scheduler import start_scheduler
            start_scheduler()


def initialize_blueprints(app):
    from app.controllers.energy_controller import energy_bp
    app.register_blueprint(energy_bp, url_prefix='/api')


def create_app(config_name=None):
    from flask import Flask
    from app.config import Config

    app = Flask(__name__)

    if config_name == 'testing':
        app.config.from_object(TestingConfig)
    else:  
        app.config.from_object(config_name or Config)

    # Initialize extensions
    initialize_extensions(app)

    # Initialize scheduler
    initialize_scheduler(app)

    # Initialize blueprints
    initialize_blueprints(app)

    return app
