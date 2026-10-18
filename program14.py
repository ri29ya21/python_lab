#Program 14: Object Persistence Engine via Serialization

import pickle
import shelve
import os


class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)


def save_with_pickle(student):
    with open("student.dat", "wb") as file:
        pickle.dump(student, file)

    print("Object saved using pickle.")


def load_with_pickle():
    if not os.path.exists("student.dat"):
        print("No saved student found.")
        return

    with open("student.dat", "rb") as file:
        student = pickle.load(file)

    print("\nRestored using pickle:")
    student.display()


def save_with_shelve(student):
    with shelve.open("student_db") as database:
        database["student"] = student

    print("Object saved using shelve.")


def load_with_shelve():
    with shelve.open("student_db") as database:
        if "student" not in database:
            print("No saved student found.")
            return

        student = database["student"]

    print("\nRestored using shelve:")
    student.display()


def main():
    student = Student("Aman", 101, 92.5)

    while True:
        print("\nObject Persistence Menu")
        print("1. Save using pickle")
        print("2. Load using pickle")
        print("3. Save using shelve")
        print("4. Load using shelve")
        print("5. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                save_with_pickle(student)

            elif choice == "2":
                load_with_pickle()

            elif choice == "3":
                save_with_shelve(student)

            elif choice == "4":
                load_with_shelve()

            elif choice == "5":
                print("Program terminated.")
                break

            else:
                print("Invalid choice.")

        except (OSError, EOFError, pickle.PickleError) as error:
            print("File operation error:", error)


if __name__ == "__main__":
    main()