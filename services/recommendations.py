from flask import Blueprint, jsonify, request
import logging

recommendations_bp = Blueprint('recommendations', __name__)
logger = logging.getLogger(__name__)

@recommendations_bp.route('/get', methods=['GET'])
def get_recommendations():
    weather_data = request.get_json()

    if not weather_data:
        return jsonify({"error": "Weather data is required"}), 400

    try:
        recommendations = generate_recommendations(weather_data)
        return jsonify({"recommendations": recommendations})
    except Exception as e:
        logger.error(f"Error generating recommendations: {str(e)}")
        return jsonify({"error": str(e)}), 500

def generate_recommendations(weather_data):
    recommendations = []

    weather_condition = weather_data.get('weather', [{}])[0].get('main', '').lower()
    temperature = weather_data.get('main', {}).get('temp')

    if 'rain' in weather_condition:
        recommendations.append("Take an umbrella")
    if temperature < 10:
        recommendations.append("Wear a warm jacket")
    elif temperature > 25:
        recommendations.append("Wear light clothing and sunscreen")
    if 'cloud' in weather_condition:
        recommendations.append("Might be a good day for photography")
    if 'clear' in weather_condition:
        recommendations.append("Great day for outdoor activities")

    if not recommendations:
        recommendations.append("Weather conditions are moderate, enjoy your day!")

    return recommendations
