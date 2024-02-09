def angryProfessor(k, a):
    n_student = [stu for stu in a if stu <= 0]
    if k<=len(n_student):
        return 'NO'
    else : return 'YES'