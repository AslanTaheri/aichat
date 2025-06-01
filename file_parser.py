from typing import Union
import fitz
import docx
import json


def parse_pdf(file) -> str:
    text = ""
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text()
    return text


def parse_docx(file) -> str:

    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])


def parse_json(file) -> str:
    data = json.load(file)
    return json.dumps(data, indent=2)


def parse_uploaded_file(file) -> Union[str, None]:
    filename = file.name
    if filename.endswith(".pdf"):
        return parse_pdf(file)
    elif filename.endswith(".docx"):
        return parse_docx(file)
    elif filename.endswith(".json"):
        return parse_json(file)
    else:
        return "Unsupported file type."
