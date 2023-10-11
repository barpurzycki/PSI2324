import requests
import json

def check_url(url:str) -> bool:
    check = requests.get(url)
    if check.status_code < 200 or check.status_code > 299:
        return False
    return True

print(check_url('https://api.gios.gov.pl/pjp-api/rest/station/findAll'))
