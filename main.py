def get_last_row(sheet):
    last_row = 0
    cols = sheet.range(1, 1, sheet.row_count, 999)

    for cell in cols:
        if cell.value != "":
            last_row = cell.row

    if last_row > 0:
        return last_row
    else:
        return last_row + 1

