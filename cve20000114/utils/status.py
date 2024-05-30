import requests


def check_internet_connection():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False

