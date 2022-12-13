from urllib.error import HTTPError
import requests
from dotenv import load_dotenv
import os
import logging

logger = logging.getLogger("concert_buddies.credentials")
logger.info("send help pls creds")

load_dotenv()

SP_DC_COOKIE = os.getenv('SP_DC_COOKIE')


def get_access_token():
    get_access_token_url = "https://open.spotify.com/get_access_token?reason=transport&productType=web_player"
    try:
        response = requests.get(get_access_token_url,
                                headers={
                                    "Cookie": "sp_dc={0}".format(SP_DC_COOKIE),
                                },
                                )
    except HTTPError as http_err:
        logger.error(f'HTTP error: {http_err}')
    except Exception as err:
        logger.error(f'Unkown error: {err}')
    else:
        logger.info("got web player access token")
        return response.json().get('accessToken')
