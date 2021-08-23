from csp import CSP

# Hilfsfunktion: alle Werte einer Zeile oder Spalte ermitteln
def filter_dict_by_key(dict_to_filter, condition):
    filtered_list = []
    for key in dict_to_filter:
        if condition(key):
            filtered_list.append(dict_to_filter[key])
    return filtered_list

# Bedingungen: keine Dubletten in Zeilen, Spalten oder 3x3-Teilblöcken
def sudoku_constraint(assignment):
    # Zeilen
    for line in range(0, 9):
        line_fields = filter_dict_by_key(assignment, lambda key: key[0] == line)
        if len(line_fields) > len(set(line_fields)):
            return False
    # Spalten
    for column in range(0, 9):
        column_fields = filter_dict_by_key(assignment, lambda key: key[1] == column)
        if len(column_fields) > len(set(column_fields)):
            return False
    # 3x3-Felder
    for start_line in range(0, 10, 3):
        for start_column in range(0, 10, 3):
            square_fields = []
            for line in range(start_line, start_line + 3):
                for column in range(start_column, start_column + 3):
                    if (line, column) in assignment:
                        square_fields.append(assignment[(line, column)])
            if len(square_fields) > len(set(square_fields)):
                return False
    return True

# Das fertige Sudoku ausgeben
def print_sudoku(assignment):
    for line in range(0, 9):
        print('+-+-+-+-+-+-+-+-+-+')
        print('|', end='')
        for column in range(0, 9):
            if (line, column) in assignment:
                print(assignment[(line, column)], end='')
            else:
                print(' ', end = '')
            print('|', end = '')
        print()
    print('+-+-+-+-+-+-+-+-+-+')

sudoku_variables = []
sudoku_domains = {}
for line in range(0, 9):
    for column in range(0, 9):
        field = (line, column)
        sudoku_variables.append(field)
        sudoku_domains[field] = list(range(1, 10))
sudoku_csp = CSP(sudoku_variables, sudoku_domains, sudoku_constraint)
solution = sudoku_csp.solve()
if solution:
    print_sudoku(solution)
else:
    print("Keine Lösung gefunden.")
