# Chamada da API
import sys
from pathlib import Path

# Adiciona o diretório pai ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from config.settings import url, apiVersion

import requests
from ..config.settings import url, apiVersion

print(url, apiVersion)