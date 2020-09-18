import pandas as pd
from fpdf import FPDF
import numpy as np


# ---The class defines all the functions used for creation a pdf report
# ---to hide the cell frames change '1' to '0' in the self.cell() in header, footer, set_name functions
class PDFReport(FPDF):

    # constructor of the class takes parameters as headertext, footertext and name(title) of the report
    def __init__(self, headertext, footertext, logo_flag=False):
        super().__init__()
        self.headertext = headertext
        self.footertext = footertext
        if logo_flag:
            self.logo_flag = True
        self.set_margins(left=10, top=5, right=10)

    def header(self):
        self.set_font('arial', 'I', 12)
        self.cell(0, 10, self.headertext, 1, 0, 'C')  # !change '1' to '0' to hide the cell frame
        if self.logo_flag:
            self.image('logo.png', x=187, y=3, w=10, type='', link='')
        self.ln(15)

    def footer(self):
        self.set_font('arial', 'I', 12)
        self.set_y(-15)
        self.cell(0, 10, self.footertext, 1, 0, 'C')  # !change '1' to '0' to hide the cell frame

    # set a report's title
    def set_name(self, name):
        self.set_xy(10, self.get_y())
        self.set_font('arial', 'B', 20)
        self.cell(0, 20, '%s' % str(name), 1, 2, 'C')  # !change '1' to '0' to hide the cell frame
        self.ln(15)

    # create a table from a dataframe
    def table(self, df):
        self.set_xy(10, 85)
        self.set_font('arial', 'B', 12)
        self.cell(30, 10, 'Number', 1, 0, 'C')
        self.cell(30, 10, 'A', 1, 0, 'C')
        self.cell(30, 10, 'B', 1, 2, 'C')
        self.cell(-60)

        # for each value in the dataframe set a new cell 30*10
        self.set_font('arial', '', 12)
        for i in range(0, len(df)):
            self.cell(30, 10, '%s' % (df['Number'].iloc[i]), 1, 0, 'C')  # str placeholder
            self.cell(30, 10, '%s' % (df['A'].iloc[i]), 1, 0, 'C')
            self.cell(30, 10, '%s' % (df['B'].iloc[i]), 1, 2, 'C')  # 1-frame visible, 2-to the next line
            # pdf.cell(30, 10, '%s' % (str(df.B.iloc[i])), 1, 0, 'C')
            # pdf.cell(30, 10, '%s' % (str(df.A.iloc[i])), 1, 2, 'C')
            self.cell(-60)

        self.ln(10)

    # insert an image at the current position (x,y) and specify its width
    def insert_image(self, image, width):
        self.image(image, x=None, y=None, w=width, type='', link='')

    # def insert_image(self, image, i):
    #     if i == 1:
    #         self.image(image, x=None, y=None, w=40, type='', link='')
    #     else:
    #         for i in range(0, i-1):
    #             self.image(image, x=None, y=None, w=80, type='', link='')

    # write a text from a txt file in the left column
    def write_left_from_textfile(self, txtfile):
        self.set_xy(10, 155)
        self.set_font('arial', '', 12)
        f = open(txtfile, "r")
        for x in f:
            self.multi_cell(w=90, h=10, txt=x, border=1,
                            align='L', fill=False)

    # write text from a string in the right column
    def write_right(self, text):
        self.set_xy(110, 155)
        self.set_font('arial', '', 12)
        self.multi_cell(w=90, h=10, txt=text, border=1,
                        align='L', fill=False)

    # create a table in excel and write it
    def write_from_excel(self):
        df_1 = pd.DataFrame(np.random.randn(10, 2), columns=list('AB'))
        writer = pd.ExcelWriter('testtable.xlsx')
        df_1.to_excel(writer)
        writer.save()

        df_2 = pd.read_excel('testtable.xlsx')
        self.set_font('arial', 'B', 12)
        # pdf.cell(10)
        self.cell(70, 10, 'Writing a table from excel', 0, 2, 'C')
        # pdf.cell(-40)
        self.cell(30, 10, 'Index Column', 1, 0, 'C')
        self.cell(30, 10, 'Col A', 1, 0, 'C')
        self.cell(30, 10, 'Col B', 1, 2, 'C')
        self.cell(-60)
        self.set_font('arial', '', 12)

        # for each value in a table create a new cell 30*10
        for i in range(0, len(df_2) - 1):
            self.cell(30, 10, '%s' % str(i), 1, 0, 'C')
            self.cell(30, 10, '%s' % str(df_2.A.iloc[i]), 1, 0, 'C')
            self.cell(30, 10, '%s' % str(df_2.B.iloc[i]), 1, 2, 'C')
            self.cell(-60)

# df = pd.DataFrame()
# df['Number'] = ["1", "2", "3", "4"]
# df['A'] = [3, 4, 5, 3]
# df['B'] = [3, 3, 4, 4]
# txtfile = 'text.txt'
# text = "Placeholder for the text. Overwrite the line with your text." \
#        "Placeholder for the text. Overwrite the line with your text." \
#        "Placeholder for the text. Overwrite the line with your text." \
#        "Placeholder for the text. Overwrite the line with your text." \
#        "Placeholder for the text. Overwrite the line with your text." \
#        "Placeholder for the text. Overwrite the line with your text." \
#        "Placeholder for the text. Overwrite the line with your text." \
#        "Placeholder for the text. Overwrite the line with your text." \
#        "Placeholder for the text. Overwrite the line with your text." \
#        "Placeholder for the text. Overwrite the line with your text."
#
# pdf.set_margins(left=10, top=10, right=10)
# #pdf.line(105, 0, 105, 297) #line in the middle of the page A4 (210 mm * 297 mm)

# pdf.output('Report.pdf', dest='F') #local file
