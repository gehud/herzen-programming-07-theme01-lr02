from flask import Blueprint, jsonify, request
from utils.storage import get_request_history, get_city_statistics
import logging

history_bp = Blueprint('history', __name__)
logger = logging.getLogger(__name__)

@history_bp.route('/user/<user_id>', methods=['GET'])
def get_user_history(user_id):
    try:
        history = get_request_history(user_id)
        return jsonify({"user_id": user_id, "history": history})
    except Exception as e:
        logger.error(f"Error fetching user history: {str(e)}")
        return jsonify({"error": str(e)}), 500

@history_bp.route('/statistics', methods=['GET'])
def get_statistics():
    try:
        limit = request.args.get('limit', default=5, type=int)
        stats = get_city_statistics(limit)
        return jsonify({"statistics": stats})
    except Exception as e:
        logger.error(f"Error fetching statistics: {str(e)}")
        return jsonify({"error": str(e)}), 500
