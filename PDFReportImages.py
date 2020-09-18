from PIL import Image

from PDFReport import PDFReport


# ---The class inherits from the PDFReport class
# ---there are two functions for inserting images (after each other or in a row)
# ---the size of the A4 page is 210*297 mm
class PDFReportImages(PDFReport):
    x_global, y_global = 10, 45  # set x, y right after the title(name)

    # ---overriding a superclass constructor (name is added)---
    def __init__(self, headertext, footertext, name, logo_flag):
        super().__init__(headertext, footertext, logo_flag)
        self.name = name
        self.add_page()
        self.set_name(name)

    # ---adds single images separately under each other---
    def add_image(self, image, width):

        im = Image.open(image, 'r')
        width_original, height_original = im.size  # get the pixels of an image
        cor_height_to_width = round(height_original / width_original, 2)  # get a correlation between height and width

        if PDFReportImages.y_global + cor_height_to_width * width > (
                # check if there is enough place for one more row on a page
                297 - 15) and self.accept_page_break():  # 297 mm is width of A4, 5+10 mm from the bottom to the footer
            self.add_page(self.cur_orientation)
            PDFReportImages.x_global, PDFReportImages.y_global = 10, 20  # set coordinates right below the header
            self.image(image, x=PDFReportImages.x_global, y=PDFReportImages.y_global, w=width)
            PDFReportImages.y_global += (cor_height_to_width + 0.1) * width  # distinct to a next image
        else:
            self.image(image, x=PDFReportImages.x_global, y=PDFReportImages.y_global, w=width)
            PDFReportImages.y_global += (cor_height_to_width + 0.1) * width  # distinct to a next image

    # ---takes a list of images and a number of images per row
    # ---insert images after each other till the number per row is reached
    def fill_with_images(self, list_of_images, no_per_row):

        width_row_limit = 190  # the width of an A4 page is 210 mm, left and right margins are 10 mm : (210-10*2)

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
                        x, y = PDFReportImages.x_global, PDFReportImages.y_global
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
                x, y = 10, 20  # set coordinates right below the header

        PDFReportImages.x_global = x
        PDFReportImages.y_global = y


pdf = PDFReportImages("header", "footer", "Name of the report", logo_flag=True)

pdf.add_image('images/bild1.png', 60)
pdf.fill_with_images(['images/bild1.png', 'images/bild2.png',
                      'images/bild1.png', 'images/bild2.png',
                      'images/bild1.png', 'images/image.png',
                      'images/bild1.png', 'images/bild2.png',
                      'images/bild1.png', 'images/bild2.png',
                      'images/bild1.png', 'images/bild2.png',
                      'images/image.png', 'images/bild2.png',
                      'images/bild1.png', 'images/bild2.png'],
                     no_per_row=5)  # the second argument is the number of images to be placed in one row
pdf.add_image('images/bild1.png', 60)
pdf.add_image('images/bild1.png', 60)
pdf.add_image('images/image.png', 60)
pdf.add_image('images/image.png', 60)
pdf.add_image('images/bild1.png', 60)
pdf.add_image('images/image.png', 60)

pdf.output('ReportImages.pdf', dest='F')  # name the pdf file and store it in the project's folder
