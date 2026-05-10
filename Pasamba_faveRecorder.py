import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active

sheet['A1'] = 'Product'
sheet['B1'] = 'Price'
sheet['C1'] = 'Quantity'
sheet['D1'] = 'Total Amount'
sheet['A2'] = 'Pencil'
sheet['B2'] = 15
sheet['C2'] = 4

workbook.save('favorite_people.xlsx')