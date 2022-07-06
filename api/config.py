import os

from dotenv import load_dotenv

load_dotenv()

appid = os.getenv("appid")

"""Периоды рассылки"""
UPDATE_PERIODS = [1, 3, 6, 12]


"""API к current weather data"""
API_URL = os.getenv("API_URL")

# """Парметры, передаваемые в запрос"""
# API_URL_PARAMS = {
#     'q': 'city',
#     'units': 'metric',
#     'APPID': 'appid',
# }
