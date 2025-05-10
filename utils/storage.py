from collections import defaultdict
import time
import threading

_request_history = defaultdict(list)
_city_requests = defaultdict(int)
_lock = threading.Lock()

def save_request_to_history(user_id, city):
    timestamp = int(time.time())
    with _lock:
        _request_history[user_id].append({
            'city': city,
            'timestamp': timestamp
        })
        _city_requests[city] += 1

def get_request_history(user_id, limit=10):
    with _lock:
        return _request_history.get(user_id, [])[-limit:]

def get_city_statistics(limit=5):
    with _lock:
        sorted_cities = sorted(_city_requests.items(), key=lambda x: x[1], reverse=True)
        return [{'city': city, 'requests': count} for city, count in sorted_cities[:limit]]
