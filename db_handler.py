import csv


# next step -> read from MySQL
def get_soldiers_list(path="soldiers.csv", columns=None):
    soldiers_list = []

    # Open the CSV file and read its contents
    with open(path, mode='r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            if columns:
                soldier = {col: row[col] for col in columns if col in row}
            else:
                # If no columns specified, return the entire row
                soldier = row

            soldiers_list.append(soldier)

    return soldiers_list
