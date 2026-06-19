def user_input():
    grades = []

    while True:
        entry = input("Input grades (or 'done' to stop): ")
        if entry == "done":
            break
        try:
            grades.append(int(entry))
        except ValueError:
            print("Invalid input, try again.")
    return grades

def generate_fdt(grades):        

    frequency = {}

    total_students = 0
    total_grades = 0

    for grade in grades:
        if grade not in frequency:
            frequency[grade] = 1
        else:
            frequency[grade] = frequency[grade] + 1
        total_students = total_students + 1
        total_grades = total_grades + grade

    print("Grade | Frequency | Relative Frequency")

    for grade, count in sorted(frequency.items()):
        relative_frequency = (count/total_students) * 100
        print(f"{grade} | {count} | {relative_frequency}%")

    avg_grades = total_grades/total_students

    most_frequent = max(frequency, key=frequency.get)
    least_frequent = min(frequency, key=frequency.get)

    print(f"Total Students: {total_students}")
    print(f"Average Grades: {avg_grades}")
    print(f"Most frequent grade: {most_frequent}")
    print(f"Least frequent grade: {least_frequent}")

grades = user_input()
generate_fdt(grades)
