# src/config.py

BASE_URL_AWAJUN = "https://ebible.org/agr/"
BASE_URL_SPANISH = "https://ebible.org/spabes/"

TIMEOUT = 20
OUTPUT_DIR = "data/processed/"
RAW_DIR = "data/raw/"

# Estructura de los archivos generados
FILENAME_TEMPLATE = "{lang}_{book}_{chapter:02d}.json"
