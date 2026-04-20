import requests
import sys

def master_search(query):
    api_url = f"https://apibay.org/q.php?q={query.replace(' ', '%20')}"
    try:
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            return response.json()
    except:
        return []
