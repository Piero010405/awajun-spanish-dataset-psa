import os
import requests
import logging
from src import config

def setup_logger():
    logging.basicConfig(
        filename="data/logs/scraping.log",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )

def safe_request(url, timeout):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response
    except Exception as e:
        logging.warning(f"Error al obtener {url}: {e}")
        return None

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)
