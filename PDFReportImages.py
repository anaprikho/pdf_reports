from PDFReport import PDFReport
from PIL import Image


# ---The class create an object of the PDFReport class
# ---and placed images at the specific coordinates (the size of the A4 page is 210*297 mm)
class PDFReportImages(PDFReport):

    def __init__(self, headertext, footertext, name):
        super().__init__(headertext, footertext)
        self.headertext = headertext
        self.footertext = footertext
        self.name = name
        self.add_page()
        #self.set_auto_page_break(35)
        self.set_name(name)

    def add_single_image(self, image, width):
        self.image(image, x=None, y=None, w=width)
        self.ln(5)

    def fill_with_images(self, list_of_images, no_per_site):

        # width_list = []
        # height_list = []
        # for img in list_of_images:
        #     im = Image.open(img, 'r')
        #     width, height = im.size
        #     width_list.append(width)
        #     height_list.append(height)
        #     max_height = max(height_list)
        # print(max_height)

        width_row_limit = 190 #the width of an A4 page is 210 mm, left and right margins are 10 mm : (210-10*2)
        no_per_column = 3

        if (no_per_site % no_per_column) == 0:
            no_per_row = int(no_per_site / no_per_column)
        else:
            no_per_row = int(no_per_site / no_per_column + 1)

        width_of_image = int((width_row_limit - 5 * (no_per_row - 1)) / no_per_row)  # 5 mm distance between images in a row
        #x, y = self.get_x(), self.get_y()

        for j in range(0, no_per_column):
            for i in range(0, no_per_row):

                try:
                    if i == 0 and j == 0:
                        x, y = 10, self.get_y()
                    self.image(list_of_images[i + no_per_row * j], x=x, y=y, w=width_of_image)
                    x, y = x + width_of_image + 5, y

                except IndexError as error:
                    pass

            x, y, = 10, y + (width_of_image * 2.3)
            if (y + 3 * width_of_image > 290 and self.accept_page_break()):
                self.add_page(self.cur_orientation)
                x, y = 10, 30

pdf = PDFReportImages("header", "footer", "Name of the report")
# pdf.add_single_image('images/image.png', width = 60)
# pdf.add_single_image('images/image.png', width = 60)
# pdf.add_single_image('images/image.png', width = 60)
# pdf.add_single_image('images/image.png', width = 60)


pdf.fill_with_images(['images/bild1.png', 'images/bild2.png',
                      'images/bild1.png', 'images/bild2.png',
                      'images/bild1.png', 'images/image.png',
                      'images/bild1.png', 'images/bild2.png',
                      'images/bild1.png', 'images/bild2.png',
                      'images/bild1.png', 'images/bild2.png',
                      'images/image.png', 'images/bild2.png',
                      'images/bild1.png', 'images/bild2.png'], no_per_site=10) # the second argument is the number of images placed on a page
                                                                                # uneven number will be rounded up.

#pdf.fill_with_images(['images/bild1.png', 'images/bild2.png'],5)
pdf.output('ReportImages.pdf', dest='F')  # name the pdf file and store it in the projet's folder
