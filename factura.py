from fpdf import FPDF
import datetime

def crearFactura(idCompra, idCliente, tracks, subtotales, total, trackNames):
    totalInfo = 'Total: $ ' + str('{:.2f}'.format(total))
    
    dateInfo = 'Fecha: ' + str(datetime.datetime.now())

    clientInfo = 'ID Cliente: ' + str(idCliente)
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="FACTURA COMPRA TRACKS", ln=1, align="L")
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt=dateInfo, ln=1, align="L")
    pdf.cell(200, 10, txt=clientInfo, ln=1, align="L")

    tracksInfo = ''

    i = 0

    while i < len(trackNames): 
        tracksInfo = str(trackNames[i]) + ' - $ ' + str(subtotales[i]) 
        pdf.cell(200, 10, txt=tracksInfo, ln=1, align="L")
        i = i + 1

    pdf.cell(200, 10, txt=totalInfo, ln=1, align="L")
    
    docName = 'factura' + str(idCompra) + 'cliente' + str(idCliente) + '.pdf'
    pdf.output(docName)


