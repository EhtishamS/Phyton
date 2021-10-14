import openpyxl

# cartella = openpyxl.Workbook()
# file = cartella.active
# file.title = "guardiamo"
# cartella.save(filename="mkc.xlsx")

cartella = openpyxl.load_workbook("export_14032021-1703.xlsx")
file = cartella["title1"]