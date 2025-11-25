# Initialize an empty list to store student records
students = []

# Start an infinite loop for the menu system
while True:
    print("\n--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Generate a full report")
    print("4. Find the top student")
    print("5. Exit program")

    # Prompt user for menu choice and handle invalid input
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Error: incorrect choice")
        continue  # Skip to next loop iteration

    # Option 1: Add a new student by name
    if choice == 1:
        name = input("Enter student name: ")
        # Check if student already exists
        exists = any(student["name"] == name for student in students)
        if exists:
            print(f"Student '{name}' already exists.")
        else:
            # Create a new student dictionary with empty grades
            new_dict = {"name": name, "grades": []}
            students.append(new_dict)
            print(f"Student '{name}' added.")

    # Option 2: Add grades for an existing student
    elif choice == 2:
        name = input("Enter student name: ")
        found = False
        for student in students:
            if student["name"] == name:
                found = True
                # Loop to enter multiple grades until 'done' is typed
                while True:
                    grade = input("Enter a grade (or 'done' to finish): ")
                    if grade.lower() == "done":
                        break
                    try:
                        int_grade = int(grade)
                        # Validate grade range
                        if 0 <= int_grade <= 100:
                            student["grades"].append(int_grade)
                        else:
                            print("Grade must be between 0 and 100.")
                    except ValueError:
                        print("Invalid input. Please enter a number or 'done'.")
                break
        if not found:
            print("Student not found.")

    # Option 3: Generate a full report with averages and summary
    elif choice == 3:
        if not students:
            print("No students in the system.")
        else:
            max_avg = None  # Track highest average
            min_avg = None  # Track lowest average
            total_sum = 0   # Sum of all grades
            total_count = 0  # Total number of grades

            for student in students:
                grades = student["grades"]
                name = student["name"]

                try:
                    # Calculate average grade for current student
                    avg = sum(grades) / len(grades)
                    print(f"{name}'s average grade is {avg:.2f}")

                    # Update max and min averages
                    if max_avg is None or avg > max_avg:
                        max_avg = avg
                    if min_avg is None or avg < min_avg:
                        min_avg = avg

                    # Add to overall totals
                    total_sum += sum(grades)
                    total_count += len(grades)

                except ZeroDivisionError:
                    # Handle case where student has no grades
                    print(f"{name} has no grades. Average grade is N/A.")

            # Print overall summary if grades exist
            if total_count == 0:
                print("No grades available for any student.")
            else:
                overall_avg = total_sum / total_count
                print("\nSummary:")
                print(f"Max average: {max_avg:.2f}")
                print(f"Min average: {min_avg:.2f}")
                print(f"Overall average: {overall_avg:.2f}")

    # Option 4: Find the top student using max() and lambda
    elif choice == 4:
        def find_top_student(students):
            if not students:
                print("No students in the system.")
                return

            # Filter out students who have no grades
            valid_students = [s for s in students if s.get("grades")]

            if not valid_students:
                print("No grades available for any student.")
                return

            # Use max() with a lambda function to find the highest average
            # Lambda returns average grade for each student
            top_student = max(valid_students, key=lambda s: sum(
                s["grades"]) / len(s["grades"]))
            avg = sum(top_student["grades"]) / len(top_student["grades"])

            # Print result with formatted average
            print(
                f"The student with the highest average is {top_student['name']} with a grade of {avg:.2f}.")

        # Call the function to execute Option 4
        find_top_student(students)

    # Option 5: Exit the program
    elif choice == 5:
        print("Exiting program. Goodbye!")
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice. Please select a number between 1 and 5.")
