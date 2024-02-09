def gradingStudents(grades):
    return [g+(g > 37)*(g % 5 > 2)*(5 - (g % 5)) for g in grades]