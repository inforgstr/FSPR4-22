import pypdf


from pathlib import Path

current_path = Path().absolute() / "practice_files"

pdf_path = current_path / "Pride_and_Prejudice.pdf"

# Merge method
# merger = pypdf.PdfMerger()
# merger.append("result2.pdf")
# merger.merge(2, Path().absolute() / "result2.pdf")
# merger.write("result.pdf")
# merger.close()



# Append method
# pdf_paths = [
#     current_path / f
#     for f in os.listdir(current_path)
#     if f.endswith("pdf")
# ]


# merger = pypdf.PdfMerger()

# for path in pdf_paths:
#     merger.append(path)
    
# merger.write("result.pdf")
# merger.close()



# Extracting latest page from pdf file and saving to last_page.pdf
# pdf_writer = pypdf.PdfWriter()

# reader = pypdf.PdfReader(pdf_path)
# latest_page = reader.pages[-1]

# pdf_writer.add_page(latest_page)
# pdf_writer.write("last_page.pdf")
# pdf_writer.close()
