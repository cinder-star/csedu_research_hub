import os
from hashlib import md5
from zipfile import ZipFile
from latex import build_pdf
from pybtex import format_from_file

from csedu_research_hub.settings import BASE_DIR

def hash(string):
    return md5(string.encode()).hexdigest()

def extract_filepath_and_destination(filename):
    filepath = os.path.join(BASE_DIR, "media", filename)
    directory = os.path.splitext(filename)[0]
    destination_path = os.path.join(BASE_DIR, "extracted", directory)
    return filepath, destination_path

def unzip_file(filename):
    filepath, destination = extract_filepath_and_destination(filename)
    with ZipFile(filepath, "r") as zipref:
        zipref.extractall(destination)
    return destination

def make_pdf(folderpath):
    filename = os.path.basename(os.path.normpath(folderpath))+".pdf"
    aux_file = os.path.basename(os.path.normpath(folderpath))+".aux"
    destination = os.path.join(BASE_DIR, "pdfs", filename)
    filepath = os.path.join(folderpath, "main.tex")
    pdf = build_pdf(open(filepath), texinputs=[folderpath, ''])
    pdf.save_to(destination)
    # format_from_file(aux_file_name = aux_file, filename="main.bib", style=None)
    dir1 = os.path.basename(destination)
    dir2 = os.path.split(os.path.dirname(destination))[1]
    return os.path.join("/",dir2, dir1)