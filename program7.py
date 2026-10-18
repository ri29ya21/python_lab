#Program 7: Functional Data Filtering & Matrix Transformation Suite.

def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []

    # Input matrix elements from terminal
    print("Enter matrix elements row by row:")
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))

        while len(row) != cols:
            print(f"Please enter exactly {cols} numbers.")
            row = list(map(int, input(f"Row {i + 1}: ").split()))

        matrix.append(row)

    print("\nOriginal Matrix:")
    for row in matrix:
        print(row)

    # Remove negative values using filter()
    filtered_matrix = [
        list(filter(lambda x: x >= 0, row))
        for row in matrix
    ]

    print("\nMatrix after removing negative values:")
    for row in filtered_matrix:
        print(row)

    # Square each element using map()
    squared_matrix = [
        list(map(lambda x: x ** 2, row))
        for row in filtered_matrix
    ]

    print("\nSquared Matrix:")
    for row in squared_matrix:
        print(row)

    # Flatten matrix using list comprehension
    values = [x for row in filtered_matrix for x in row]

    # Sort values using sorted()
    sorted_values = sorted(values)

    print("\nSorted Values:", sorted_values)

    # Take tuple records from terminal
    n = int(input("\nEnter number of student records: "))
    records = []

    for i in range(n):
        name = input(f"Enter student {i + 1} name: ")
        marks = float(input(f"Enter marks of {name}: "))
        records.append((name, marks))

    # Sort tuples by marks in descending order
    sorted_records = sorted(
        records, key=lambda item: item[1], reverse=True
    )

    print("\nStudent Records Sorted by Marks:")
    for record in sorted_records:
        print(record)


if __name__ == "__main__":
    main()