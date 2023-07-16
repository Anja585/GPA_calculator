import os
import numpy as np
import pandas as pd
import tkinter.filedialog

# Maps letter grades to GPA scale.
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

# User interface for importing information to calculate GPA.
# Returns a dictionary object with student(s) name(s), modules and grades.
def create_student():
    names = []
    marks_module_names = []
    file = str(input('Would you like to import a file (Y/N): '))
    if file == 'Y':
        final_list = file_import()
        return final_list
    else:
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
            marks_module_names.append(dict(zip(module_names, marks)))
        final_list = dict(zip(names, marks_module_names))
    return final_list

# Dialog for importing a CSV file. 
# Returns a dictionary object with student(s) name(s), modules and grades.
def file_import():
    filename = tkinter.filedialog.askopenfile()
    df = pd.read_csv(filename, index_col=0)
    dict_file = df.to_dict('index')
    return dict_file
    
def map_percentage_points_to_grades(percentage_grade):
    grade_keys = list(grade.keys())
    if percentage_grade >= 90:
        gpa_scale_grade = grade["A+"]
        letter_grade = grade_keys[0]
    elif percentage_grade >= 80:
        gpa_scale_grade = grade["A"]
        letter_grade = grade_keys[1]
    elif percentage_grade >= 70:
        gpa_scale_grade = grade["A-"]
        letter_grade = grade_keys[2]
    elif percentage_grade >= 67:
        gpa_scale_grade = grade["B+"]
        letter_grade = grade_keys[3]
    elif percentage_grade >= 64:
        gpa_scale_grade = grade["B"]
        letter_grade = grade_keys[4]
    elif percentage_grade >= 60:
        gpa_scale_grade = grade["B-"]
        letter_grade = grade_keys[5]
    elif percentage_grade >= 57:
        gpa_scale_grade = grade["C+"]
        letter_grade = grade_keys[6]
    elif percentage_grade >= 54:
        gpa_scale_grade = grade["C"]
        letter_grade = grade_keys[7]
    elif percentage_grade >= 50:
        gpa_scale_grade = grade["C-"]
        letter_grade = grade_keys[8]
    elif percentage_grade == 49:
        gpa_scale_grade = grade["D+"]
        letter_grade = grade_keys[9]
    elif percentage_grade >= 47:
        gpa_scale_grade = grade["D"]
        letter_grade = grade_keys[10]
    elif percentage_grade >= 45:
        gpa_scale_grade = grade["D-"]
        letter_grade = grade_keys[11]
    elif percentage_grade == 44:
        gpa_scale_grade = grade["E+"]
        letter_grade = grade_keys[12]
    elif percentage_grade >= 42:
        gpa_scale_grade = grade["E"]
        letter_grade = grade_keys[13]
    elif percentage_grade >= 40:
        gpa_scale_grade = grade["E-"]
        letter_grade = grade_keys[14]
    elif percentage_grade == 39:
        gpa_scale_grade = grade["F+"]
        letter_grade = grade_keys[15]
    else: 
        gpa_scale_grade = grade["F"]
        letter_grade = "F" 
    return gpa_scale_grade, letter_grade    

# Returns a dictionary object with names and gpas.
def calculate_gpa(final_list):
    names = final_list.keys()
    final_gpa = []
    for i in final_list:
        pairs = final_list[i]
        gpa_scale_grades = []
        for p in pairs:
            percentage_grade = pairs[p]
            gpa_scale_grade, letter_grade = map_percentage_points_to_grades(percentage_grade)
            gpa_scale_grades.append(gpa_scale_grade)
        gpa = np.average(gpa_scale_grades)
        gpa_rounded = np.round(gpa, 2)
        final_gpa.append(gpa_rounded)        
    return dict(zip(names,final_gpa))

# Returns a dictionary object with names and highest scoring modules.
def highest_scoring_module(final_list):
    names = final_list.keys()
    highest_scoring_modules = []
    for i in final_list:
        pairs = final_list[i]
        sorted_pairs = dict(sorted(pairs.items(), key=lambda x: x[1]))
        highest_scoring_module = list(sorted_pairs.keys())[-1]
        highest_scoring_modules.append(highest_scoring_module)        
    return dict(zip(names,highest_scoring_modules)) 

# Returns a dictionary object with names and lowest scoring modules.
def lowest_scoring_module(final_list):
    names = final_list.keys()
    lowest_scoring_modules = []
    for i in final_list:
        pairs = final_list[i]
        sorted_pairs = dict(sorted(pairs.items(), key=lambda x: x[1]))
        lowest_scoring_module = list(sorted_pairs.keys())[0]
        lowest_scoring_modules.append(lowest_scoring_module)        
    return dict(zip(names,lowest_scoring_modules))

# Returns a dictionary object with names and standard deviation.
def standard_deviation(final_list):
    names = final_list.keys()
    standard_deviations = []
    for i in final_list:
        pairs = final_list[i]
        pair_values = list(pairs.values())    
        st_deviation = np.std(pair_values)
        st_deviation_rounded = round(st_deviation, 2) 
        standard_deviations.append(st_deviation_rounded)
    return dict(zip(names,standard_deviations))

# Returns a dictionary object with names and median values.
def median(final_list):
    names = final_list.keys()
    medians = []
    for i in final_list:
        pairs = final_list[i]
        pair_values = list(pairs.values())  
        median = np.median(pair_values)
        median_rounded = round(median, 2) 
        medians.append(median_rounded)
    return dict(zip(names,medians))

# Returns a dictionary object with names, modules and letter grades.
def letter_grades(final_list):
    names = final_list.keys()
    final_results = []
    for i in final_list:
        pairs = final_list[i]
        letter_grades = []
        module_names = list(pairs.keys())
        for p in pairs:
            percentage_grade = pairs[p]
            gpa_scale_grade, letter_grade = map_percentage_points_to_grades(percentage_grade)
            letter_grades.append(letter_grade)
        result = dict(zip(module_names, letter_grades))
        final_results.append(result)
    return dict(zip(names,final_results))

# 
def next_highest(final_list):
    gpa = calculate_gpa(final_list)
    sorted_gpa = dict(sorted(gpa.items(), key=lambda x: x[1]))
    gpa_sorted_values = list(sorted_gpa.values())
    names_sorted = list(sorted_gpa.keys())
    differences = []
    for i in range(len(gpa_sorted_values)):
        difference = np.round((gpa_sorted_values[i] - gpa_sorted_values[i-1]), 3) 
        differences.append(difference)
    last = np.round((4.2 - gpa_sorted_values[-1]), 3)
    differences.append(last)
    differences_final = differences[1:] 
    dict_sorted = dict(zip(names_sorted, differences_final))
    final = {k: dict_sorted.get(k, v) for k, v in gpa.items()}
    return final
    
# Main function. 
if __name__ == '__main__':
    os.system('cls')    
    final_list = create_student()
    if len(list(final_list.keys())) == 0:
        print('Not enough data')
        print('End')
    else: 
        print('\nGPA')
        print(f'{calculate_gpa(final_list)}\n')
        print('Highest scoring module')
        print(f'{highest_scoring_module(final_list)}\n')
        print('Lowest scoring module')
        print(f'{lowest_scoring_module(final_list)}\n')
        print('Standard deviation')
        print(f'{standard_deviation(final_list)}\n')
        print('Median')
        print(f'{median(final_list)}\n')
        print('Grade point gap to the next highest GPA')       
        print(f'{next_highest(final_list)}\n')
        print('Letter grades')
        print(f'{letter_grades(final_list)}\n')
        print('End')
        
        