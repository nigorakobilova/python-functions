# Part I
'''array = [2, 5, 8, 3, 1]
def draw_stars(x):
    for count in range(0, len(array)):
        print '*'* x[count]

draw_stars(array)'''

# Part II
array = [5, 'Limo', 10, 'Maria', 'Wonderful', 3, 2]

def draw_stars(x):
    for count in range(0, len(array)):
        if isinstance(array[count], int):
            print '*'* x[count]
        else:
            print array[count][0].lower()*len(array[count])
draw_stars(array)
