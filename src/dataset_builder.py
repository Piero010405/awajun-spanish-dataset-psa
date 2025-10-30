import pandas as pd
from src.books_dict import BOOKS
from src.aligner import align_chapters
from src import config

def build_dataset():
    rows = []
    for book, info in BOOKS.items():
        for ch in range(1, info["chapters"] + 1):
            aligned = align_chapters(book, ch)
            if aligned:
                rows.extend(aligned)
    df = pd.DataFrame(rows)
    df.to_csv(f"{config.OUTPUT_DIR}/merged/awajun_spanish.csv", index=False, encoding="utf-8-sig")
    return df
