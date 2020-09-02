from PDFReport import PDFReport

#---The class create an object of the PDFReport class
#---and placed images at the specific coordinates (the size of the A4 page is 210*297 mm)
class PDFReportImages(PDFReport):

    headertext = "Placeholder for the header"  # set text for the header
    footertext = "Placeholder for the footer"  # set text for the footer
    name = "Report only with images"  # title placed in the report

    pdf = PDFReport(headertext, footertext)  # create a PDFReport object
    pdf.add_page()
    pdf.set_name(name, 30)  # the second argument is an 'y' coordinate of the title cell, the 'x' is already set as 10

    x1 = 10  # position of the left column
    x2 = 110  # position of the right column
    w = 90  # the width of an imgage, the height will be calculated automatically
    y1 = pdf.get_y()  # an 'y' coordinate of the first line
    y2 = y1 + w + 10  # an 'y' coordinate of the second line

    # ---the fisrt line, first page, 2 images---
    pdf.image('image.png', x=x1, y=y1, w=w)  # left column
    pdf.image('image.png', x=x2, y=y1, w=w)  # right column

    # ---the second line, first page, 2 images---
    pdf.image('image.png', x=x1, y=y2, w=w)  # left column
    pdf.image('image.png', x=x2, y=y2, w=w)  # right column

    pdf.add_page()  # add new page
    y3 = pdf.get_y() + 15  # get an 'y' value after adding header

    # ---the first line, second page, 2 images---
    pdf.image('image.png', x=x1, y=y3, w=w)  # left column
    pdf.image('image.png', x=x2, y=y3, w=w)  # right column

    pdf.output('ReportImages.pdf', dest='F')  # name the pdf file and store it in the projet's folder