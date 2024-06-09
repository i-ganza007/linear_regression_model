from re import T
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_font('Arial',style='B',size=24)
pdf.cell(200,10,txt="Hello",ln=1,align="C")
pdf.output("app.pdf")
