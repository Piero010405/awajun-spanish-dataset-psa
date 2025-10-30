import json
import os
from src import config

def align_chapters(book, chapter):
    file_awa = os.path.join(config.OUTPUT_DIR, "awajun", config.FILENAME_TEMPLATE.format(lang="awajun", book=book, chapter=chapter))
    file_spa = os.path.join(config.OUTPUT_DIR, "spanish", config.FILENAME_TEMPLATE.format(lang="spanish", book=book, chapter=chapter))

    if not os.path.exists(file_awa) or not os.path.exists(file_spa):
        return None

    with open(file_awa, encoding="utf-8") as f:
        awa = json.load(f)
    with open(file_spa, encoding="utf-8") as f:
        spa = json.load(f)

    aligned = []
    for v in awa.keys():
        if v in spa:
            aligned.append({
                "book": book,
                "chapter": chapter,
                "verse": v,
                "awajun": awa[v],
                "spanish": spa[v]
            })
    return aligned
