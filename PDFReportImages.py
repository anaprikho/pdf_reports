from PDFReport import PDFReport
from PIL import Image

#---The class create an object of the PDFReport class
#---and placed images at the specific coordinates (the size of the A4 page is 210*297 mm)
class PDFReportImages(PDFReport):

    def __init__(self, headertext, footertext, name):
        super().__init__(headertext, footertext)
        self.headertext = headertext
        self.footertext = footertext
        self.name = name
        self.add_page()
        self.set_name(name, 30) #the second argument is an 'y' coordinate of the title cell, the 'x' is already set as 10

    def add_single_image(self, image, width):
        self.image(image, x = None, y = None, w = width)

    def fill_with_images(self, list_of_images, no_per_site):
        width_list = []
        height_list = []
        width_row_limit = 190

        no_per_column = 2
        if (no_per_site % 2) == 0:
            no_per_row = int(no_per_site / 2)
        else:
            no_per_row = int(no_per_site / 2 + 1)

        width_of_image = int((width_row_limit - 5 * (no_per_row - 1)) / no_per_row) #5 mm distance between images in a row
        x, y = self.get_x(), self.get_y()

        for j in range(0, no_per_column):
            for i in range(0, no_per_row):

                if j == 0:
                    try:
                        #if i == 0: x, y = self.get_x(), self.get_y()
                        self.image(list_of_images[i],x = x, y = y, w = width_of_image)
                        x, y = x + width_of_image + 5, y
                    except IndexError as error:
                        pass

                if j == 1:
                    try:
                        if i == 0: x, y = 10, y + 115
                        self.image(list_of_images[i + no_per_row], x=x, y=y, w=width_of_image)
                        x, y = x + width_of_image + 5, y
                    except IndexError as error:
                        # Output expected IndexErrors.
                        pass
        print(no_per_row)



        # for img in list_of_images:
        #
        #     x, y = self.get_x(), self.get_y()
        #     print(x, y)
        #
        #     im = Image.open(img, 'r')
        #     width, height = im.size
        #     width_list.append(width)
        #     height_list.append(height)
        #
        #     self.image(img)
        #     self.set_xy(x=x + width + 10, y=y + height + 10)
        # print(width_list)

    # x1 = 10  # position of the left column
    # x2 = 110  # position of the right column
    # w = 90  # the width of an imgage, the height will be calculated automatically
    # y1 = pdf.get_y()  # an 'y' coordinate of the first line
    # y2 = y1 + w + 10  # an 'y' coordinate of the second line
    #
    # # ---the fisrt line, first page, 2 images---
    # pdf.image('image.png', x=x1, y=y1, w=w)  # left column
    # pdf.image('image.png', x=x2, y=y1, w=w)  # right column
    #
    # # ---the second line, first page, 2 images---
    # pdf.image('image.png', x=x1, y=y2, w=w)  # left column
    # pdf.image('image.png', x=x2, y=y2, w=w)  # right column
    #
    # pdf.add_page()  # add new page
    # y3 = pdf.get_y() + 15  # get an 'y' value after adding header
    #
    # # ---the first line, second page, 2 images---
    # pdf.image('image.png', x=x1, y=y3, w=w)  # left column
    # pdf.image('image.png', x=x2, y=y3, w=w)  # right column
    #
    # pdf.output('ReportImages.pdf', dest='F')  # name the pdf file and store it in the projet's folder

pdf = PDFReportImages("header", "footer", "Name of the report")
#pdf.add_single_image('image.png', width = 60)
pdf.fill_with_images(['images/bild1.png', 'images/bild2.png',
                      'images/bild1.png', 'images/bild2.png',
                      'images/bild1.png', 'images/image.png'], 7)
pdf.output('ReportImages.pdf', dest='F')  # name the pdf file and store it in the projet's folder