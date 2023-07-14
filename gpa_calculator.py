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
def calculate_gpa(final_list):
    final_gpa = []
    for i in final_list:
        pairs = final_list[i]
        gpa_scale_grades = []
        for percentage_grade in pairs:
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
        final_gpa.append(gpa_rounded)
    return final_gpa

# returns the name of the highest scoring module
def highest_scoring_module(final_list):
    highest_scoring_modules = []
    for i in final_list:
        pairs = final_list[i]
        pair_keys = list(pairs.keys())
        pair_keys.sort()
        sorted_pairs = {i: pairs[i] for i in pair_keys}
        highest_scoring_module = list(sorted_pairs.values())[-1]
        highest_scoring_modules.append(highest_scoring_module)        
    return highest_scoring_modules

# returns the name of the lowest scoring module
def lowest_scoring_module(final_list):
    lowest_scoring_modules = []
    for i in final_list:
        pairs = final_list[i]
        pair_keys = list(pairs.keys())
        pair_keys.sort()
        sorted_pairs = {i: pairs[i] for i in pair_keys}
        lowest_scoring_module = list(sorted_pairs.values())[0]
        lowest_scoring_modules.append(lowest_scoring_module)        
    return lowest_scoring_modules

# returns standard deviation
def standard_deviation(final_list):
    standard_deviations = []
    for i in final_list:
        pairs = final_list[i]
        pair_keys = list(pairs.keys())    
        st_deviation = np.std(pair_keys)
        st_deviation_rounded = round(st_deviation, 2) 
        standard_deviations.append(st_deviation_rounded)
    return standard_deviations

# returns median
def median(final_list):
    medians = []
    for i in final_list:
        pairs = final_list[i]
        pair_keys = list(pairs.keys())  
        median = np.median(pair_keys)
        median_rounded = round(median, 2) 
        medians.append(median_rounded)
    return medians

# return module names and letter grades
def letter_grades(final_list):
    final_results = []
    for i in final_list:
        pairs = final_list[i]
        letter_grades = []
        module_names = list(pairs.values())
        for percentage_grade in pairs:
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
        result = dict(zip(letter_grades, module_names))
        final_results.append(result)
    return final_results

def next_highest(final_list):
    gpa = calculate_gpa(final_list)
    gpa_sorted = sorted(gpa)
    names = list(final_list.keys())
    differences = []
    for i in range(len(gpa_sorted)):
        difference = np.round((gpa_sorted[i] - gpa_sorted[i-1]), 3) 
        differences.append(difference)
    last = np.round((4.2 - gpa_sorted[-1]), 3)
    differences.append(last)
    differences_final = differences[1:] 
    return dict(zip(names, differences_final))
    
def user_interface():
    names = []
    marks_module_names = []
    while True:
        marks = []
        module_names = []
        print('To quit or insert data for another student press 0')
        name = str(input('Enter student name: '))
        if name  == '0':
            break
        names.append(name)
        while True:           
            module = str(input('Enter module name: '))
            if module  == '0':
                break
            try:
                grade_in_percentage = int(input('Enter grade (%): '))
                if grade_in_percentage  == 0:
                    break
                marks.append(grade_in_percentage)    
            except:
                ValueError
                print('Use number characters only!')
            module_names.append(module)            
        marks_module_names.append(dict(zip(marks, module_names)))
    final_list = dict(zip(names, marks_module_names))
    return final_list


# main function
if __name__ == '__main__':
    os.system('cls')    
    final_list = user_interface()
    names = list(final_list.keys())
    if len(list(final_list.keys())) == 0:
        print('Not enough data')
        print('End')
    else: 
        print('\nGPA')
        print(f'{dict(zip(names, calculate_gpa(final_list)))}\n') 
        print('Highest scoring module')
        print(f'{dict(zip(names, highest_scoring_module(final_list)))}\n') 
        print('Lowest scoring module')
        print(f'{dict(zip(names, lowest_scoring_module(final_list)))}\n')
        print('Standard deviation')
        print(f'{dict(zip(names, standard_deviation(final_list)))}\n')
        print('Median')
        print(f'{dict(zip(names, median(final_list)))}\n')
        print('Gap from the next highest GPA')       
        print(f'{next_highest(final_list)}\n')
        print('Letter grades')
        print(f'{dict(zip(names, letter_grades(final_list)))}\n')
        
        