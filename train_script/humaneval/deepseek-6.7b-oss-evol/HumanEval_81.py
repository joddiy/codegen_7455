def numerical_letter_grade(grades):
    grade_table = {
        4.0: 'A+',
        3.7: 'A',
        3.3: 'A-',
        3.0: 'B+',
        2.7: 'B',
        2.3: 'B-',
        2.0: 'C+',
        1.7: 'C',
        1.3: 'C-',
        1.0: 'D+',
        0.7: 'D',
        0.0: 'D-',
    }

    def get_grade(gpa):
        for gpa_limit, grade in sorted(grade_table.items(), reverse=True):
            if gpa >= gpa_limit:
                return grade
        return 'E'

    return [get_grade(gpa) for gpa in grades]

print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]))  # ['A+', 'B', 'C-', 'C', 'A-']