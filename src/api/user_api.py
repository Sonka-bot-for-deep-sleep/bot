from dotenv import load_dotenv
from os import getenv
import requests
import logging

load_dotenv()
api_url = getenv("API_URL")

async def get_user_by_tg_id(tgID):
    req = {
        "tgID": tgID
    }
    res = requests.post(api_url, req)

    if res.status == 404:
        logging.error("Ошибка, пользователь не найден")
        return 
    
    logging.info(res.json())