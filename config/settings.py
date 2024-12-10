import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("MAKE_BASE_URL")
apiVersion = os.getenv("MAKE_API_VERSION")