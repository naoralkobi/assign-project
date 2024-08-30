import csv


# next step -> read from MySQL
def get_soldiers_list(path="soldiers.csv", columns=None, department_condition=None):
    soldiers_list = []

    # Open the CSV file and read its contents
    with open(path, mode='r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:

            # Filter based on the department_condition
            if department_condition and row.get('department') != department_condition:
                continue

            if columns:
                soldier = {col: row[col] for col in columns if col in row}
            else:
                # If no columns specified, return the entire row
                soldier = row

            soldiers_list.append(soldier)
    return soldiers_list
