from flask import Flask, jsonify
from services.weather import weather_bp
from services.recommendations import recommendations_bp
from services.history import history_bp
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

app.register_blueprint(weather_bp, url_prefix='/weather')
app.register_blueprint(recommendations_bp, url_prefix='/recommendations')
app.register_blueprint(history_bp, url_prefix='/history')

@app.route('/')
def health_check():
    return jsonify({"status": "healthy", "message": "Weather Aggregator System is running"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
