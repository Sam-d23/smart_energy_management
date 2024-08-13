from flask import Blueprint, jsonify, request
from app import db


energy_bp = Blueprint('energy', __name__)

def get_usage():
    from app.models.energy import EnergyUsage
    usage = EnergyUsage.query.all()
    return jsonify([u.serialize for u in usage])

def add_usage():
    data = request.get_json()
    new_usage = EnergyUsage(**data)
    db.session.add(new_usage)
    db.session.commit()
    return jsonify(new_usage.serialize), 201
