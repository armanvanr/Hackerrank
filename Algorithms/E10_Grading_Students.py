def gradingStudents(grades):
    # final_grades = []
    # for grade in grades:
    #     next_multi5 = int(grade / 5 + 1) * 5
    #     if grade >= 38 and next_multi5 - grade < 3:
    #         grade = next_multi5
    #     final_grades.append(grade)
    # return final_grades

    for i in range(len(grades)):
        next_multi5 = (grades[i] // 5 + 1) * 5
        if grades[i] >= 38 and next_multi5 - grades[i] < 3:
            grades[i] = next_multi5
    return grades
print(gradingStudents([73, 67, 38, 33]))