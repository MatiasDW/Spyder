from openpyxl import Workbook
"""from openpyxl.styles import Font
import time"""

book = Workbook()
sheet = book.active

sheet['A1'] = 5
sheet['A2'] = 10

book.save('prueba_escritura.xlsx')