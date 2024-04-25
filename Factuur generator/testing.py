from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet
import json
import os

def pagina(json_file, logo_path, logo_width, logo_height):
    styles = getSampleStyleSheet()

    # Extract data from JSON file
    with open(json_file, 'r') as j:
        data = json.load(j)

    ordernummer = data['order']['ordernummer']
    orderdatum = data['order']['orderdatum']
    betaaltermijn = data['order']['betaaltermijn']

    klant_naam = data['order']['klant']['naam']
    klant_adres = data['order']['klant']['adres']
    klant_postcode = data['order']['klant']['postcode']
    klant_stad = data['order']['klant']['stad']
    klant_kvk = data['order']['klant']['KVK-nummer']

    # print("Ordernummer:", ordernummer)
    # print("Orderdatum:", orderdatum)
    # print("Betaaltermijn:", betaaltermijn)

    # print("Klant naam:", klant_naam)
    # print("Klant adres:", klant_adres)
    # print("Klant postcode:", klant_postcode)
    # print("Klant stad:", klant_stad)
    # print("Klant KVK-nummer:", klant_kvk)

    # producten = data['order']['producten']
    # for product in producten:
    #     productnaam = product['productnaam']
    #     aantal = product['aantal']
    #     prijs_per_stuk_excl_btw = product['prijs_per_stuk_excl_btw']
    #     btw_percentage = product['btw_percentage']
    j.close()


    # Create a new PDF file for each JSON file
    pdf_file = os.path.splitext(os.path.basename(json_file))[0] + ".pdf"
    directory_pdfs = './pdfs'
    c = canvas.Canvas(os.path.join(directory_pdfs, pdf_file), pagesize=A4)

    # Drawing the "Factuur" paragraph
    Title_style = styles["Normal"]
    Title_style.fontName = 'Helvetica-Bold'
    Title_style.fontSize = 36
    Title_style.textColor = HexColor("#5E5B95")
    p = Paragraph("Factuur", Title_style)
    # Draw the paragraph on the canvas
    p.wrapOn(c, 200, 100)
    p.drawOn(c, 75, 680)

    factuurdata = [
        ['', '', '', ''],
        ['DATUM:', '', 'AAN:', klant_naam],
        [orderdatum, betaaltermijn, '', klant_adres],
        ['', '', '', klant_postcode],
        ['FACTUURNR:', '', '', klant_stad],
        [ordernummer],
        [''],
        ['KVKNUMMER:'],
        [klant_kvk],
        ['', '', '', '']]

    # Maak de tabel
    table = Table(factuurdata, colWidths=[1.6 * inch] * len(factuurdata[0]))

    # Maak stijl voor de tabel
    style = TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.purple),  # Tekstkleur van de eerste rij
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),  # Tekstkleur van alle andere cellen
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),  # Achtergrondkleur van de eerste rij
        ('BACKGROUND', (0, -1), (-1, -1), colors.lightblue),  # Achtergrondkleur van de laatste rij
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Uitlijning van alle cellen naar links
        ('ALIGN', (3, 1), (3, -1), 'LEFT'),  # Uitlijning van "Exemple" in de laatste kolom naar links
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),  # Lettertype van alle cellen naar vetgedrukt
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Onderste padding van de eerste rij
        ('GRID', (0, 1), (-1, -2), 1, colors.transparent)  # Rasterlijnen instellen
    ])

    # Maak de stijl voor de gekleurde woorden
    word_color_style = TableStyle([
        ('FONTNAME', (2, 1), (2, 1), 'Helvetica-Bold'),  # Lettertype van "AAN:"
        ('TEXTCOLOR', (0, 1), (0, 1), HexColor("#5E5B95")),  # Kleur van "DATUM:"
        ('TEXTCOLOR', (2, 1), (2, 1), HexColor("#5E5B95")),  # Kleur van "AAN:"
        ('TEXTCOLOR', (0, 4), (0, 4), HexColor("#5E5B95")),  # Kleur van "FACTUURNR:"
        ('TEXTCOLOR', (0, 7), (0, 7), HexColor("#5E5B95")),  # Kleur van "KLANTNUMMER::"
        ('ALIGN', (2, 1), (2, 1), 'RIGHT'),  # Uitlijning van "AAN:" naar het midden
])

    # Pas de stijlen toe op de tabel
    table.setStyle(style)
    table.setStyle(word_color_style)
    table.wrapOn(c, inch, inch)
    table.drawOn(c, 75, 460)
    
    # Add logo to the PDF
    c.drawImage(logo_path, x=428, y=650, width=logo_width, height=logo_height)

    # Drawing the table
    factuurdata = [['verkoper', 'E-mail', 'Tel', 'Postcode'],
                   [verkoper_naam, verkoper_email, verkoper_Tel, verkoper_postcode]]
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.transparent),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.purple),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (1, 1), (-1, -1), HexColor('#F2F2F2')),
                        ('GRID', (0, 1), (-1, -2), 1, colors.black),
                        ('LINEAFTER', (0, 0), (0, -1), 1, colors.black)])
    table = Table(factuurdata, colWidths=[1.6 * inch] * len(factuurdata[0]))
    table.setStyle(style)
    table.wrapOn(c, inch, inch)
    table.drawOn(c, 75, 410)

    factuurdata = [['HVH', 'beschrijving', 'BTW %', 'prijs per eenheid']]
    print(factuurdata)

    y_position = 310  # Initial y-coordinate for drawing the table
    prijzen_excl = []
    prijzen_incl = []

    producten = data['order']['producten']
    for product in producten:
        productnaam = product['productnaam']
        aantal = product['aantal']
        prijs_per_stuk_excl_btw = product['prijs_per_stuk_excl_btw']
        prijzen_excl.append(prijs_per_stuk_excl_btw)
        btw_percentage = product['btw_percentage']
        
        # Append product details to factuurdata
        productlijst = [aantal, productnaam, btw_percentage, prijs_per_stuk_excl_btw]
        factuurdata.append(productlijst)

        btw = (prijs_per_stuk_excl_btw / 100) * btw_percentage
        prijs_incl = prijs_per_stuk_excl_btw + btw
        prijzen_incl.append(prijs_incl)

        # Update y_position for the next table
        y_position -= 16  # Move down by 20 units


    separator = ['']
    Subtotaal =  ['', '', 'SUBTOTAAL', f'€ {sum(prijzen_excl)}']
    Totaal = ['', '', 'TOTAAL', f'€ {round(sum(prijzen_incl), 2)}']
    factuurdata.append(separator)
    factuurdata.append(Subtotaal)
    factuurdata.append(Totaal)

    # Define table style
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.transparent),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.purple),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Alleen de tekst links uitlijnen
        ('ALIGN', (2, 0), (2, -1), 'CENTER'),  # BTW % in het midden uitlijnen
        ('ALIGN', (3, 1), (3, -1), 'CENTER'),  # Prijs per eenheid in het midden uitlijnen
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (1, 1), (0, 16), 1, colors.black),  # Verticale gridlijnen
        ('GRID', (0, 1), (-1, 0), 1, colors.black),  # Horizontale gridlijnen voor tweede laag
        ('GRID', (0, 17), (-1, 0), 1, colors.black),  # Onderste horizontale gridlijn
        
        ('GRID', (2, 17), (3, -1), 1, colors.transparent)  # Tweede grid
    ])

    # Create table object
    table = Table(factuurdata, colWidths=[1.6 * inch] * len(factuurdata[0]))

    # Apply style to table
    table.setStyle(style)
    table.wrapOn(c, inch, inch)
    table.drawOn(c, 75, y_position)

    c.save()


# Replace 'output.pdf' with your desired output file name
pdf_file = "output.pdf"
logo_path = "TimeRobo-01.png"
logo_width = 100  # Adjust according to your logo size
logo_height = 100  # Adjust according to your logo size

verkoper_naam = input('Voer uw naam en achternaam in: ')
verkoper_email = input('Voer uw E-mail adress in: ')
verkoper_Tel = input('Voer je telefoonNummer in: ')
verkoper_postcode = input('Voer uw postcode in: ')

# Directory containing JSON files
json_directory = './test_set_softwareleverancier'

# Iterate over JSON files in the directory
for filename in os.listdir(json_directory):
    if filename.endswith('.json'):
        json_file = os.path.join(json_directory, filename)
        pagina(json_file, logo_path, logo_width, logo_height)