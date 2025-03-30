import openpyxl

def get_test_data(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):  # Skipping header
        data.append(row)

    workbook.close()
    return data
