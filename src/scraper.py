import os
from bs4 import BeautifulSoup, NavigableString, Tag
import ftfy
from src import config
from src.utils import safe_request, ensure_dir

# --- SCRAPING ---
def save_raw_html(html, lang, book, chapter):
    """
    Guarda el HTML crudo en data/raw/<lang>/<BOOK><chapter>.htm
    """
    ensure_dir(f"{config.RAW_DIR}/{lang}/")
    filename = f"{book}{chapter:02d}.htm"
    path = os.path.join(config.RAW_DIR, lang, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

def build_url(language: str, book: str, chapter: int) -> str:
    base = config.BASE_URL_AWAJUN if language == "awajun" else config.BASE_URL_SPANISH
    return f"{base}{book}{chapter:02d}.htm"

def get_verses(url, lang, book, chapter, timeout=config.TIMEOUT):
    """
    Descarga y parsea los versículos de un capítulo.
    También guarda el HTML crudo en data/raw/ por idioma.
    """
    response = safe_request(url, timeout)
    if response is None:
        return {}  # si falla la descarga

    html = response.content.decode("utf-8", errors="ignore")

    # Guardar copia del HTML crudo
    save_raw_html(html, lang, book, chapter)

    soup = BeautifulSoup(html, "html.parser")

    verses = {}
    current_verse = None
    buffer = []

    # Iteramos por todos los divs válidos (p y q)
    valid_divs = soup.find_all("div", class_=lambda c: c in ["p", "q"])

    for div in valid_divs:
        for element in div.descendants:
            if isinstance(element, Tag):
                # Si es un nuevo versículo
                if element.name == "span" and "verse" in element.get("class", []):
                    # Guardar el anterior si hay
                    if current_verse and buffer:
                        text_clean = ftfy.fix_text(" ".join(buffer)).strip()
                        text_clean = text_clean.lstrip("0123456789 ").strip()
                        verses[current_verse] = text_clean
                        buffer = []

                    # Nuevo versículo
                    current_verse = element.get("id", "").replace("V", "").strip()

            elif isinstance(element, NavigableString):
                # Solo acumular texto si estamos dentro de un versículo
                text = element.strip()
                if text and current_verse:
                    buffer.append(text)

    # Guardar el último versículo
    if current_verse and buffer:
        text_clean = ftfy.fix_text(" ".join(buffer)).strip()
        text_clean = text_clean.lstrip("0123456789 ").strip()
        verses[current_verse] = text_clean

    return verses