# awajun-spanish-dataset-psa
First Awajún-Spanish Dataset for ML and DL translate models

This project builds a bilingual dataset aligned verse by verse between the Awajún Bible and the Spanish Bible.

## Structure
- Scraping from `https://ebible.org/agr/` y `https://ebible.org/spabes/`
- Cleaning, UTF-8 normalization, and alignment by verse.
- Export to `data/processed/merged/awajun_spanish.csv`

## Use
```bash
pip install -r requirements.txt
python main.py
