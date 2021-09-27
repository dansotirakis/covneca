import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
BASE_API_URL = os.environ("BASE_API_URL")
BISCOINT = os.environ("BISCOINT_API_URL")
PHOEMUR = os.environ("FUNDAMENTUS")
COINLIB = os.environ['COINLIB']
OKANE = os.environ("OKANE")