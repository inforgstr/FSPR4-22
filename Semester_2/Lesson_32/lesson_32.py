import pypdf
import re


from collections import Counter
from pathlib import Path


pdf_path = Path().absolute() / "practice_files" / "Pride_and_Prejudice.pdf"


def common_word(pdf_path, page_num):
    pdf_reader = pypdf.PdfReader(pdf_path)

    try:
        page = pdf_reader.pages[page_num - 1].extract_text()
    except IndexError as error:
        return error

    words = re.split(r'[\n ?;:,."]+', page)[1:-1]

    word_counts = Counter(words)

    max_count = max(word_counts.values())

    most_common_words = [
        word for word, count in word_counts.items() if count == max_count
    ]

    return ", ".join(most_common_words)


print(common_word(pdf_path, 2))
