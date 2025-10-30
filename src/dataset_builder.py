import os
import pandas as pd
from src.books_dict import BOOKS
from src.aligner import align_chapters
from src import config

def build_dataset():
    os.makedirs(f"{config.OUTPUT_DIR}/merged", exist_ok=True)
    rows = []

    for book, info in BOOKS.items():
        chapters = info["chapters"]

        # Si es int → genera un rango. Si es lista → úsala directamente.
        if isinstance(chapters, int):
            chapters = range(1, chapters + 1)

        for ch in chapters:
            aligned = align_chapters(book, ch)
            if aligned:
                rows.extend(aligned)

    if not rows:
        print("⚠️ No se generaron datos alineados (revisa si hay HTMLs válidos).")
        return None

    df = pd.DataFrame(rows)
    output_path = f"{config.OUTPUT_DIR}/merged/awajun_spanish.csv"
    df.to_csv(output_path, index=False, encoding="utf-8-sig")
    print(f"✅ Dataset generado correctamente: {output_path}")
    return df
