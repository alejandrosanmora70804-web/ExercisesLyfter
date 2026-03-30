import csv


def export_to_csv(data_students):
    if not data_students:
        print("There are no registered students to export.")
        return
    
    with open("data_students.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Section", "Spanish", "English", "Social", "Sciences", "Average"])

        for student in data_students:
            average = (student.spanish_note + student.english_note + student.social_note + student.sciences_note) / 4
            writer.writerow([
                student.name,
                student.section,
                student.spanish_note,
                student.english_note,
                student.social_note,
                student.sciences_note,
                f"{average}"
            ])

    print(f"Data exported successfully to 'data_students.csv'.")


def import_from_csv(data_students):
    file_name = input("Enter the filename to import: ").strip()
    if not file_name:
        print("No filename entered.")
        return
    file_name += ".csv"

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            imported = 0
            skipped = 0
            for row in reader:
                name = row["Name"]
                section = row["Section"]
                already_exists = any(
                    student.name.lower() == name.lower() and
                    student.section.upper() == section.upper()
                    for student in data_students
                )
                if already_exists:
                    skipped += 1
                    continue

                from actions import Student
                student = Student(
                    name=name,
                    section=section,
                    spanish_note=float(row["Spanish"]),
                    english_note=float(row["English"]),
                    social_note=float(row["Social"]),
                    sciences_note=float(row["Sciences"])
                )
                data_students.append(student)
                imported += 1

        print(f"Import complete: {imported} students added, {skipped} skipped (already existed).")

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as error:
        print(f"An unexpected error ocurred while importing: {error}.")