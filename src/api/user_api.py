from dotenv import load_dotenv
from os import getenv
import requests

load_dotenv()
api_url = getenv("API_URL")


async def get_user_by_tg_id(tgID):
    requests.post(api_url, )