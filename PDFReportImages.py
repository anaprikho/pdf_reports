from PDFReport import PDFReport


# ---The class create an object of the PDFReport class
# ---and placed images at the specific coordinates (the size of the A4 page is 210*297 mm)
class PDFReportImages(PDFReport):

    def __init__(self, headertext, footertext, name):
        super().__init__(headertext, footertext)
        self.name = name
        self.add_page()
        self.set_name(name)

    def add_single_image(self, image, width):
        self.image(image, x=None, y=None, w=width)
        self.ln(5)

    def fill_with_images(self, list_of_images, no_per_site):

        width_row_limit = 190  # the width of an A4 page is 210 mm, left and right margins are 10 mm : (210-10*2)
        no_per_column = 2  # desired number of columns on one page, may differ to the real number if there is not
        # enough place due to calculated width

        if (no_per_site % no_per_column) == 0:  # calculated a number of images to be placed in a row
            # no_per_row is actually the number of columns
            no_per_row = int(no_per_site / no_per_column)
        else:
            no_per_row = int(no_per_site / no_per_column + 1)

        width_of_image = int(  # calculate a width of a single image, a height will be then automatically calculated
            (width_row_limit - 5 * (no_per_row - 1)) / no_per_row)  # 5 mm distance between images in a row

        if (len(list_of_images) % no_per_row) == 0:  # calculate a number of rows will be needed based on lenght of
            # the image list and number of images per row
            rows_sum = int(len(list_of_images) / no_per_row)
        else:
            rows_sum = int(len(list_of_images) / no_per_row + 1)

        for j in range(0, rows_sum):  # for each row
            for i in range(0, no_per_row):  # for each column (no_per_row is

                try:
                    if i == 0 and j == 0:  # set coordinates for the very first row
                        x, y = 10, self.get_y()
                    self.image(list_of_images[i + no_per_row * j], x=x, y=y, w=width_of_image)  # place an image
                    x, y = x + width_of_image + 5, y  # 5 mm distinct between images within a row

                except IndexError as error:  # catches error if there is no more images to be placed in a row but the
                    # no_per_row was not reached yet
                    pass

            x, y, = 10, y + (width_of_image * 2.3)  # distinct to the next row

            if (j != rows_sum - 1) and y + 2.7 * width_of_image > (
            # check if there is enough place for one more row on a page
                    297 - 15) and self.accept_page_break():  # 297 mm is width of A4, 5+10 mm from the bottom to the footer
                self.add_page(self.cur_orientation)
                x, y = 10, 30  # set coordinates right below the header


pdf = PDFReportImages("header", "footer", "Name of the report")

pdf.fill_with_images(['images/bild1.png', 'images/bild2.png',
                      'images/bild1.png', 'images/bild2.png',
                      'images/bild1.png', 'images/image.png',
                      'images/bild1.png', 'images/bild2.png',
                      'images/bild1.png', 'images/bild2.png',
                      'images/bild1.png', 'images/bild2.png',
                      'images/image.png', 'images/bild2.png',
                      'images/bild1.png', 'images/bild2.png'],
                     no_per_site=8)  # the second argument is the number of images placed on a page
# uneven number will be rounded up.
pdf.output('ReportImages.pdf', dest='F')  # name the pdf file and store it in the projet's folder
