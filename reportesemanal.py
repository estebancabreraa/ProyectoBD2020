from fpdf import FPDF
import datetime

def generarReporte(comp, rep):
    
    dateInfo = 'Fecha: ' + str(datetime.datetime.now())

    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="REPORTE SEMANA COMPRA TRACKS", ln=1, align="L")
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt=dateInfo, ln=1, align="L")
    pdf.cell(200, 10, txt="Compras:", ln=1, align="L")

    tracksInfo = ''

    i = 0

    while i < len(comp): 
        Info = comp[i]
        text2 = Info.encode('latin-1', 'replace').decode('latin-1')
        pdf.cell(200, 10, txt=text2, ln=1, align="L")
        i = i + 1

    pdf.cell(200, 10, txt="Reproducciones:", ln=1, align="L")

    i = 0

    while i < len(rep): 
        Info = rep[i]
        text2 = Info.encode('latin-1', 'replace').decode('latin-1')
        pdf.cell(200, 10, txt=text2, ln=1, align="L")
        i = i + 1
    
    docName = 'Reporte Semanal.pdf'
    pdf.output(docName)

    print(len(rep))
