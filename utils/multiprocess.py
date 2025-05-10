import requests
from multiprocessing import Pool
import logging

logger = logging.getLogger(__name__)

def fetch_single_api(api_config, city, units):
    try:
        params = {}
        mapping = api_config.get('params_mapping', {})

        if mapping.get('city'):
            params[mapping['city']] = city
        if mapping.get('units') and units:
            params[mapping['units']] = units

        if api_config.get('api_key'):
            params['appid' if api_config['name'] == 'openweathermap' else 'key'] = api_config['api_key']

        response = requests.get(api_config['url'], params=params, timeout=5)
        response.raise_for_status()

        return {
            'api': api_config['name'],
            'data': response.json(),
            'error': None
        }
    except Exception as e:
        logger.error(f"Error fetching from {api_config['name']}: {str(e)}")
        return {
            'api': api_config['name'],
            'data': None,
            'error': str(e)
        }

def fetch_weather_from_apis(city, units, api_configs):
    with Pool(processes=len(api_configs)) as pool:
        args = [(config, city, units) for config in api_configs]

        results = pool.starmap(fetch_single_api, args)

    return results
