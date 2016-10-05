def scores_grades(x):
    ret = ''
    if (x<=100 and x>=90):
        ret = 'Score: {} Your grade is A'.format(x)
    elif (x<=89 and x>=80):
        ret = 'Score: {} Your grade is B'.format(x)
    elif (x<=79 and x>=70):
        ret = 'Score: {} Your grade is C'.format(x)
    elif (x<=69 and x>=60):
        ret = 'Score: {} Your grade is D'.format(x)
    else:
        ret = 'Score: {} Your grade is F'.format(x)
    return ret

for i in range(0,10):
    score = input("Enter your score: ")
    print scores_grades(score)
