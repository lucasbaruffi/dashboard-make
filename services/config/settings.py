import os
from dotenv import load_dotenv

load_dotenv()

MAKE_BASE_URL = os.getenv("MAKE_BASE_URL")
MAKE_API_VERSION = os.getenv("MAKE_API_VERSION")
MAKE_URL = os.getenv("MAKE_URL")
MAKE_TOKEN = os.getenv("MAKE_TOKEN")
MAKE_ORGANIZATION_ID = os.getenv("MAKE_ORGANIZATION_ID")