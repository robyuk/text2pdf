from pathlib import Path
import fpdf
from glob import glob

_debug_ = False

if __name__ == '__main__':
    filepaths = glob('txtfiles/*.txt')

    if _debug_:
        print(filepaths)

    for filepath in filepaths:
        filename = Path(filepath).stem
        if _debug_:
            print(filename)

        with open(filepath, 'r') as file:
            content = file.read()

        pdf = fpdf.FPDF(orientation="P", unit='mm', format='A4')
        pdf.add_page()
        pdf.set_font(family='Arial', style="B", size=18)
        pdf.cell(w=0, h=18, ln=1, txt=filename.title())
        pdf.set_font(family='Arial', size=12)
        pdf.multi_cell(w=0, h=6, align='J', txt=content)

        pdf.output(f'PDFs/{filename}.pdf')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
