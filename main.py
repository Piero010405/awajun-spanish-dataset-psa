from src.scraper import get_verses, build_url
from src.books_dict import BOOKS
from src.processor import save_verses
from src.dataset_builder import build_dataset
from src import config

def main():
    for book, info in BOOKS.items():
        chapters = info["chapters"]

        # Validacion por si tenemos Libros completos o solo numero de capitulos
        if isinstance(chapters, int):
            chapters = range(1, chapters + 1)

        for ch in chapters:
            for lang in ["awajun", "spanish"]:
                url = build_url(lang, book, ch)
                print(f"Descargando {book} {ch} ({lang}) → {url}")

                verses = get_verses(url, lang, book, ch, timeout=config.TIMEOUT)
                if verses:
                    save_verses(verses, lang, book, ch)

    print("Construyendo dataset final...")
    build_dataset()
    print("✅ Dataset generado correctamente.")


if __name__ == "__main__":
    main()
