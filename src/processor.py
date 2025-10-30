import json
import os
from src import config
from src.utils import ensure_dir

def save_verses(verses, lang, book, chapter):
    ensure_dir(f"{config.OUTPUT_DIR}/{lang}/")
    filename = config.FILENAME_TEMPLATE.format(lang=lang, book=book, chapter=chapter)
    path = os.path.join(config.OUTPUT_DIR, lang, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(verses, f, ensure_ascii=False, indent=2)
