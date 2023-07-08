import os
import numpy as np

# maps letter grade to GPA scale
grade = { 
        "A+": 4.2,
        "A": 4,
        "A-": 3.8,
        "B+": 3.6, 
        "B": 3.4, 
        "B-": 3.2, 
        "C+": 3, 
        "C": 2.8,
        "C-": 2.6, 
        "D+": 2.4, 
        "D": 2.2, 
        "D-": 2, 
        "E+": 1.8, 
        "E": 1.6, 
        "E-": 1.4, 
        "F+": 1.2, 
        "F": 1   
        }

# returns gpa from a user input
def calculate_gpa(percentage_grades):
    gpa_scale_grades = []
    for percentage_grade in percentage_grades:
        if percentage_grade >= 90:
            gpa_scale_grades.append(grade["A+"])
        elif percentage_grade >= 80:
            gpa_scale_grades.append(grade["A"])
        elif percentage_grade >= 70:
            gpa_scale_grades.append(grade["A-"])
        elif percentage_grade >= 67:
            gpa_scale_grades.append(grade["B+"])
        elif percentage_grade >= 64:
            gpa_scale_grades.append(grade["B"])
        elif percentage_grade >= 60:
            gpa_scale_grades.append(grade["B-"])
        elif percentage_grade >= 57:
            gpa_scale_grades.append(grade["C+"])
        elif percentage_grade >= 54:
            gpa_scale_grades.append(grade["C"])
        elif percentage_grade >= 50:
            gpa_scale_grades.append(grade["C-"])
        elif percentage_grade == 49:
            gpa_scale_grades.append(grade["D+"])
        elif percentage_grade >= 47:
            gpa_scale_grades.append(grade["D"])
        elif percentage_grade >= 45:
            gpa_scale_grades.append(grade["D-"])
        elif percentage_grade == 44:
            gpa_scale_grades.append(grade["E+"])
        elif percentage_grade >= 42:
            gpa_scale_grades.append(grade["E"])
        elif percentage_grade >= 40:
            gpa_scale_grades.append(grade["E-"])
        elif percentage_grade == 39:
            gpa_scale_grades.append(grade["F+"])
        else: gpa_scale_grades.append(grade["F"]) 
    gpa = np.average(gpa_scale_grades)
    gpa_rounded = np.round(gpa, 2)
    return gpa_rounded
        
# returns the name of the highest scoring module
def highest_scoring_module(marks, module_names):
    pairs = dict(zip(marks, module_names))
    pair_keys = list(pairs.keys())
    pair_keys.sort()
    sorted_pairs = {i: pairs[i] for i in pair_keys}
    highest_scoring_module = list(sorted_pairs.values())[-1]
    return highest_scoring_module

# returns the name of the lowest scoring module
def lowest_scoring_module(marks, module_names):
    pairs = dict(zip(marks, module_names))
    pair_keys = list(pairs.keys())
    pair_keys.sort()
    sorted_pairs = {i: pairs[i] for i in pair_keys}
    lowest_scoring_module = list(sorted_pairs.values())[0]
    return lowest_scoring_module

# returns standard deviation
def standard_deviation(marks):
    st_deviation = np.std(marks)
    st_deviation_rounded = round(st_deviation, 2) 
    return st_deviation_rounded

# returns median
def median(marks):
    median = np.std(marks)
    median_rounded = round(median, 2) 
    return median_rounded
   
# return module names and letter grades
def letter_grades(percentage_grades, module_names):
    letter_grades = []
    for percentage_grade in percentage_grades:
        if percentage_grade >= 90:
            letter_grades.append("A+")
        elif percentage_grade >= 80:
            letter_grades.append("A")
        elif percentage_grade >= 70:
            letter_grades.append("A-")
        elif percentage_grade >= 67:
            letter_grades.append("B+")
        elif percentage_grade >= 64:
            letter_grades.append("B")
        elif percentage_grade >= 60:
            letter_grades.append("B-")
        elif percentage_grade >= 57:
            letter_grades.append("C+")
        elif percentage_grade >= 54:
            letter_grades.append("C")
        elif percentage_grade >= 50:
            letter_grades.append("C-")
        elif percentage_grade == 49:
            letter_grades.append("D+")
        elif percentage_grade >= 47:
            letter_grades.append("D")
        elif percentage_grade >= 45:
            letter_grades.append("D-")
        elif percentage_grade == 44:
            letter_grades.append("E+")
        elif percentage_grade >= 42:
            letter_grades.append("E")
        elif percentage_grade >= 40:
            letter_grades.append("E-")
        elif percentage_grade == 39:
            letter_grades.append("F+")
        else: letter_grades.append("F")
    return dict(zip(letter_grades, module_names))





# main function
if __name__ == '__main__':
    os.system('cls')
    marks = []
    module_names = []
    while True:
        module = str(input('Enter module name: '))
        if module  == 'Y':
            break
        grade_in_percentage = int(input('Enter grade (%): '))
        module_names.append(module)
        marks.append(grade_in_percentage)
    # calculate_gpa(marks)
    # highest_scoring_module(marks, module_names)
    # lowest_scoring_module(marks, module_names)
    # standard_deviation(marks):
    # median(marks)
    # for i in letter_grades(marks, module_names):
    #     module = str(letter_grades(marks, module_names)[i])
    #     print(f'{module}: {i}') 
    


