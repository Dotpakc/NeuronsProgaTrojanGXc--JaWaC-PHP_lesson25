# iven a dictionary of student grades,
# write a function that calculates the average grade 
# for each student and returns a dictionary that maps
# student names to their average grades.
grades = {
    'Alice': [100, 90, 80],
    'Bob': [60, 70, 80],
    'Charlie': [80, 80, 80],
    'Dave': [70, 70, 70],
    'Eve': [60, 60, 60],
    'Frank': [50, 50, 50],
    'Gina': [40, 40, 40],
    'Hannah': [30, 30, 30],
    'Igor': [20, 20, 20],
    'Jenny': [10, 10, 10]
}

def average_grades(grades):
    return {name: sum(scores) / len(scores) for name, scores in grades.items()}

average_grades3 = average_grades(grades)
print(average_grades3)  # {'Alice': 90.0, 'Bob': 70.0, 'Charlie': 80.0}


def sdafsdf(grades):
    for name, scores in grades.items():
        yield sum(scores) / len(scores)