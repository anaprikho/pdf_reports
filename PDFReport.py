import pandas as pd
from fpdf import FPDF
import numpy as np

#global headertext, footertext
class PDFReport(FPDF):

    # def __init__(self, headertext, footertext, name):
    #     super().__init__()
    #     self.headertext = headertext
    #     self.footertext = footertext
    #     self.name = name
    #     self.add_page()
    #     self.set_header(headertext)
    #     self.set_name(name)
    #     self.set_footer(footertext)

    def header(self):
        headertext

        self.set_font('arial', 'I', 12)
        self.cell(0, 10, headertext, 1, 0, 'C')
        self.image('logo.png', x=175, y=10, w=15, type='', link='')
        self.ln(25)

    def footer(self):
        global footertext

        self.set_font('arial', 'I', 12)
        self.set_y(-20)
        self.cell(0, 10, footertext + "/Page " + str(self.page_no()), 1, 0, 'C')

    # def set_header(self, headertext):
    #     self.set_font('arial', 'I', 12)
    #     self.cell(0, 10, headertext, 1, 0, 'C')
    #     self.image('logo.png', x=175, y=10, w=15, type='', link='')
    #     self.ln(25)
    #
    # def set_footer(self, footertext):
    #     self.set_y(297)
    #     self.set_font('arial', 'I', 12)
    #     self.set_y(-20)
    #     self.cell(0, 10, footertext + "/Page " + str(self.page_no()), 1, 0, 'C')

    def set_name(self, name):
        self.set_xy(0, 0)
        self.set_font('arial', 'B', 20)
        self.cell(10)  # move to 10 cm to the right
        self.cell(0, 50, " ", 1, 2, 'C')
        self.cell(0, 20, '%s' % str(name), 1, 2, 'C')
        self.cell(0, 15, " ", 1, 2, 'C')

    def table(self, df):
        self.set_xy(10, 85)
        self.set_font('arial', 'B', 12)
        self.cell(30, 10, 'Number', 1, 0, 'C')
        self.cell(30, 10, 'A', 1, 0, 'C')
        self.cell(30, 10, 'B', 1, 2, 'C')
        self.cell(-60)

        self.set_font('arial', '', 12)
        for i in range(0, len(df)):  # create a table from the given dataframe
            self.cell(30, 10, '%s' % (df['Number'].iloc[i]), 1, 0, 'C')  # str placeholder
            self.cell(30, 10, '%s' % (df['A'].iloc[i]), 1, 0, 'C')
            self.cell(30, 10, '%s' % (df['B'].iloc[i]), 1, 2, 'C')  # 1-frame visible, 2-to the next line
            # pdf.cell(30, 10, '%s' % (str(df.B.iloc[i])), 1, 0, 'C')
            # pdf.cell(30, 10, '%s' % (str(df.A.iloc[i])), 1, 2, 'C')
            self.cell(-60)

        self.ln(10)

    def insert_image(self, image, width):
        self.image(image, x=None, y=None, w=width, type='', link='') #x=130, y=90

    # def insert_image(self, image, i):
    #     if i == 1:
    #         self.image(image, x=None, y=None, w=40, type='', link='')
    #     else:
    #         for i in range(0, i-1):
    #             self.image(image, x=None, y=None, w=80, type='', link='')

    def write_left_from_textfile(self, txtfile):
        self.set_xy(10, 155)
        self.set_font('arial', '', 12)
        f = open(txtfile, "r")
        for x in f:
            self.multi_cell(w=90, h=10, txt=x, border=1,
                           align='L', fill=False)

    def write_right(self, text):
        self.set_xy(110, 155)
        self.set_font('arial', '', 12)
        self.multi_cell(w=90, h=10, txt=text, border=1,
                       align='L', fill=False)

    def write_from_excel(self):
        df_1 = pd.DataFrame(np.random.randn(10, 2), columns=list('AB'))
        writer = pd.ExcelWriter('testtable.xlsx')
        df_1.to_excel(writer)
        writer.save()

        df_2 = pd.read_excel('testtable.xlsx')
        self.set_font('arial', 'B', 12)
        #pdf.cell(10)
        self.cell(70, 10, 'Writing a table from excel', 0, 2, 'C')
        # pdf.cell(-40)
        self.cell(30, 10, 'Index Column', 1, 0, 'C')
        self.cell(30, 10, 'Col A', 1, 0, 'C')
        self.cell(30, 10, 'Col B', 1, 2, 'C')
        self.cell(-60)
        self.set_font('arial', '', 12)

        for i in range(0, len(df_2) - 1):
            self.cell(30, 10, '%s' % str(i), 1, 0, 'C')
            self.cell(30, 10, '%s' % str(df_2.A.iloc[i]), 1, 0, 'C')
            self.cell(30, 10, '%s' % str(df_2.B.iloc[i]), 1, 2, 'C')
            self.cell(-60)

df = pd.DataFrame()
df['Number'] = ["1", "2", "3", "4"]
df['A'] = [3, 4, 5, 3]
df['B'] = [3, 3, 4, 4]

name = "Name of the report"
#image = 'image.png'
txtfile = 'text.txt'
text = "Placeholder for the text. Overwrite the line with your text." \
       "Placeholder for the text. Overwrite the line with your text." \
       "Placeholder for the text. Overwrite the line with your text." \
       "Placeholder for the text. Overwrite the line with your text." \
       "Placeholder for the text. Overwrite the line with your text." \
       "Placeholder for the text. Overwrite the line with your text." \
       "Placeholder for the text. Overwrite the line with your text." \
       "Placeholder for the text. Overwrite the line with your text." \
       "Placeholder for the text. Overwrite the line with your text." \
       "Placeholder for the text. Overwrite the line with your text."

headertext = "Header"
footertext = "Footer"

pdf = PDFReport()
pdf.add_page()
# pdf.set_margins(left=10, top=10, right=10)
# #pdf.line(105, 0, 105, 297) #line in the middle of the page A4 (210 mm * 297 mm)
# pdf.set_xy(0, 0)

# pdf.title(title)
# pdf.table(df)
# #pdf.insert_image(image)
# pdf.write_left_from_textfile(txtfile)
# pdf.write_right(text)
#
# pdf.ln(20)
# pdf.write_from_excel()

pdf.output('Report.pdf', dest='F') #local file