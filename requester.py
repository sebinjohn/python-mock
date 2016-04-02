import requests


def call(url):
    response = requests.get(url, timeout=2)
    return response.status_code
