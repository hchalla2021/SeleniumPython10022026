import openpyxl

def read_excel(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name] if sheet_name else workbook.active
    data = []
    header = [cell.value for cell in sheet[1]]
    for row in sheet.iter_rows(min_row=2, values_only=True):
        row_data = {header[i]: row[i] for i in range(len(header))}
        data.append(row_data)
    return data