import csv


def get_index(prompt: str, max_index: int) -> int:
    while True:
        try:
            index = int(input(prompt)) - 1
            if 0 <= index < max_index:
                return index
            print(f"Please enter a number between 1 and {max_index}.")
        except ValueError:
            print("Please enter a valid number.")


file_path = input("Enter the path of the CSV file you wish to parse: ")
parsed_csv_dict: dict[str, dict[str, str]] = {}

try:
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        column_names = reader.fieldnames or []

        if not column_names:
            raise ValueError("The CSV file has no header row.")

        print("Available column names to make primary key from:\n")
        for index, column in enumerate(column_names, start=1):
            print(f"{index}. {column}")

        primary_key_index = get_index(
            "\nEnter the index of the column you wish to make primary key of: ",
            len(column_names),
        )
        primary_key = column_names[primary_key_index]

        print(f"\n'{primary_key}' has been set as the primary key!")

        for row in reader:
            key = row[primary_key]
            parsed_csv_dict[key] = row

    selected_item = input("\nEnter the record primary key: ")

    if selected_item in parsed_csv_dict:
        needed_value = input("\nWhat do you wish to retrieve from the CSV file?: ")
        record = parsed_csv_dict[selected_item]

        if needed_value in record:
            print(f"\n{needed_value} for {selected_item}: {record[needed_value]}")
        else:
            print(f"The dataset doesn't contain a column named '{needed_value}'.")
    else:
        print(f"Record with primary key '{selected_item}' not found.")

except FileNotFoundError:
    print(f"File at '{file_path}' not found.")
except (ValueError, IndexError) as error:
    print(f"Could not parse the CSV file: {error}")
