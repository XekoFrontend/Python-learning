student_scores = {
    "Harry": 81,
    "Ron":  78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 64
}

final_grades = {}


def student_grades():
    for name in student_scores:
        score = student_scores[name]
        if score > 90:
            final_grades[name] = "Outstanding"
        elif score > 80:
            final_grades[name] = "Exceeds Expectations"
        elif score > 70:
            final_grades[name] = "Acceptable"
        else:
            final_grades[name] = "Fail"

    return final_grades


print(student_grades())
