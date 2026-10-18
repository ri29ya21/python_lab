
# Program 8: Custom Flexible Student Grade & Statistics Calculator

def calculate_statistics(*args, **kwargs):
    if not args:
        return None, None, None, {}

    minimum = min(args)
    maximum = max(args)
    average = sum(args) / len(args)

    # Calculate letter grades
    grades = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    for marks in args:
        if marks >= 90:
            grades["A"] += 1
        elif marks >= 80:
            grades["B"] += 1
        elif marks >= 70:
            grades["C"] += 1
        elif marks >= 60:
            grades["D"] += 1
        else:
            grades["F"] += 1

    return minimum, maximum, average, grades


# Main program
n = int(input("Enter number of assessments: "))

marks_list = []

for i in range(n):
    marks = float(input(f"Enter marks for assessment {i + 1}: "))
    marks_list.append(marks)

# Take optional keyword information
student = input("Enter student name: ")
subject = input("Enter subject name: ")

# Pass variable-length arguments
minimum, maximum, average, distribution = calculate_statistics(
    *marks_list,
    student=student,
    subject=subject
)

# Display results
print("\n----- Student Grade Statistics -----")
print("Student Name:", student)
print("Subject:", subject)
print("Marks:", marks_list)
print("Minimum Marks:", minimum)
print("Maximum Marks:", maximum)
print("Average Marks:", round(average, 2))

print("\nGrade Distribution:")
for grade, count in distribution.items():
    print(f"{grade}: {count}")