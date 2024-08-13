from flask import Blueprint
from app.controllers.energy_controller import get_usage, add_usage


energy_bp = Blueprint('energy', __name__)

energy_bp.route('/usage', methods=['GET'])(get_usage)
energy_bp.route('/usage', methods=['POST'])(add_usage)
