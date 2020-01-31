import os

from latex import build_pdf

# we need to supply absolute paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
current_dir = os.path.join(BASE_DIR, "pdfs")

# we are adding an empty string to include the default locations (this is
# described on the tex manpage)
def make_pdf(pdf_dir):
    filepath = os.path.join(current_dir, "main.tex")
    pdf = build_pdf(open(filepath), texinputs=[current_dir, ''])
    pdf.save_to('ex3.pdf')