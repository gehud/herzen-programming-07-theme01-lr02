from flask import Blueprint, jsonify, request
from utils.multiprocess import fetch_weather_from_apis
from utils.storage import save_request_to_history
import logging
import secret

weather_bp = Blueprint('weather', __name__)
logger = logging.getLogger(__name__)

WEATHER_APIS = [
    {
        'name': 'openweathermap',
        'url': 'https://api.openweathermap.org/data/2.5/weather',
        'api_key': secret.OPEN_WEATHER_API,
        'params_mapping': {
            'city': 'q',
            'units': 'units'
        }
    },
    {
        'name': 'weatherapi',
        'url': 'http://api.weatherapi.com/v1/current.json',
        'api_key': secret.WEATHER_API,
        'params_mapping': {
            'city': 'q',
            'units': None
        }
    }
]

@weather_bp.route('/current', methods=['GET'])
def get_current_weather():
    city = request.args.get('city')
    units = request.args.get('units', 'metric')
    user_id = request.args.get('user_id', 'anonymous')

    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    try:
        save_request_to_history(user_id, city)

        results = fetch_weather_from_apis(city, units, WEATHER_APIS)

        successful_responses = [r for r in results if not r.get('error')]
        if not successful_responses:
            logger.error("All weather APIs failed")
            return jsonify({"error": "All weather APIs failed", "details": results}), 500

        return jsonify(successful_responses[0]['data'])

    except Exception as e:
        logger.error(f"Error fetching weather data: {str(e)}")
        return jsonify({"error": str(e)}), 500
