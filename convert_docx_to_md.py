from pathlib import Path
from docx import Document
import re

INPUT_DIR = Path("Nivel1_Leccion1")  # Ajusta si usas otro nombre
OUTPUT_DIR = Path("markdown_nivel1_leccion1")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

HEADING_MAP = {
    "heading 1": "#",
    "heading 2": "##",
    "heading 3": "###",
    "heading 4": "####"
}

def map_heading(style_name: str):
    if not style_name:
        return None
    ln = style_name.lower()
    for k, sym in HEADING_MAP.items():
        if k in ln or k.replace(" ", "") in ln or "título" in ln and k.split()[-1] in ln:
            return sym
    return None

def clean_filename(name: str) -> str:
    base = Path(name).stem
    base = re.sub(r"[^\w\-]+", "_", base)
    return base + ".md"

def paragraphs_to_markdown(doc: Document) -> str:
    lines = []
    for p in doc.paragraphs:
        text = p.text.strip()
        if not text:
            lines.append("")
            continue
        heading = map_heading(p.style.name if p.style else "")
        if heading:
            lines.append(f"{heading} {text}")
        else:
            lines.append(text)

    # Compactar múltiples líneas en blanco
    cleaned = []
    prev_blank = False
    for l in lines:
        if l.strip() == "":
            if not prev_blank:
                cleaned.append("")
            prev_blank = True
        else:
            cleaned.append(l)
            prev_blank = False

    return "\n".join(cleaned).strip() + "\n"

def convert_all():
    docs = list(INPUT_DIR.glob("*.docx"))
    if not docs:
        print(f"No se encontraron .docx en {INPUT_DIR.resolve()}")
        return
    for docx_file in docs:
        doc = Document(docx_file)
        md_text = paragraphs_to_markdown(doc)
        out_file = OUTPUT_DIR / clean_filename(docx_file.name)
        out_file.write_text(md_text, encoding="utf-8")
        print(f"Convertido: {docx_file.name} -> {out_file}")

if __name__ == "__main__":
    convert_all()