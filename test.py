import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import ftfy

TIME_OUT = 20

def get_verses(url, timeout):
    html = requests.get(url,timeout=timeout).content.decode("utf-8", errors="ignore")
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

print(get_verses("https://ebible.org/spabes/GEN04.htm", TIME_OUT))