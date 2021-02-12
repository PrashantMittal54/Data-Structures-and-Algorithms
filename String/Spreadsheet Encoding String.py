# convert the column IDs in a spreadsheet into an integer in Python.
# For Example “AA” equals 27 because it represents the 27th column.


def spreadsheet_encode_column(col_str):
    idx = 0
    power = len(col_str) - 1
    num = 0
    while idx < len(col_str):
        num += (ord(col_str[idx]) + 1 - ord('A')) * (26**power)
        power -= 1
        idx += 1
    return num


print(spreadsheet_encode_column("ZZ"))
