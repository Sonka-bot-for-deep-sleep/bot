import requests
import logging
from os import getenv

api_url = getenv("SERVICE_URL")

async def get_user_by_tg_id(tgID):
    res = requests.post(api_url, json={"tgID": tgID})

    if res.status_code == 404:
        logging.error("Ошибка, пользователь не найден")
        return None
    
    if res.status_code != 200:
        logging.error(f"Ошибка запроса: {res.status_code} {res.text}")
        return None

    return res.json()
