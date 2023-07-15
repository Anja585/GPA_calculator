import os
import numpy as np
import pandas as pd
import tkinter.filedialog


class Grade:
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
    def __init__(self, percentage_grade):
        self.percentage_grade = percentage_grade

    def map_percentage_points_to_grades(self):
        grade_keys = list(self.grade.keys())
        if self.percentage_grade >= 90:
            gpa_scale_grade = self.grade["A+"]
            letter_grade = grade_keys[0]
        elif self.percentage_grade >= 80:
            gpa_scale_grade = self.grade["A"]
            letter_grade = grade_keys[1]
        elif self.percentage_grade >= 70:
            gpa_scale_grade = self.grade["A-"]
            letter_grade = grade_keys[2]
        elif self.percentage_grade >= 67:
            gpa_scale_grade = self.grade["B+"]
            letter_grade = grade_keys[3]
        elif self.percentage_grade >= 64:
            gpa_scale_grade = self.grade["B"]
            letter_grade = grade_keys[4]
        elif self.percentage_grade >= 60:
            gpa_scale_grade = self.grade["B-"]
            letter_grade = grade_keys[5]
        elif self.percentage_grade >= 57:
            gpa_scale_grade = self.grade["C+"]
            letter_grade = grade_keys[6]
        elif self.percentage_grade >= 54:
            gpa_scale_grade = self.grade["C"]
            letter_grade = grade_keys[7]
        elif self.percentage_grade >= 50:
            gpa_scale_grade = self.grade["C-"]
            letter_grade = grade_keys[8]
        elif self.percentage_grade == 49:
            gpa_scale_grade = self.grade["D+"]
            letter_grade = grade_keys[9]
        elif self.percentage_grade >= 47:
            gpa_scale_grade = self.grade["D"]
            letter_grade = grade_keys[10]
        elif self.percentage_grade >= 45:
            gpa_scale_grade = self.grade["D-"]
            letter_grade = grade_keys[11]
        elif self.percentage_grade == 44:
            gpa_scale_grade = self.grade["E+"]
            letter_grade = grade_keys[12]
        elif self.percentage_grade >= 42:
            gpa_scale_grade = self.grade["E"]
            letter_grade = grade_keys[13]
        elif self.percentage_grade >= 40:
            gpa_scale_grade = self.grade["E-"]
            letter_grade = grade_keys[14]
        elif self.percentage_grade == 39:
            gpa_scale_grade = self.grade["F+"]
            letter_grade = grade_keys[15]
        else: 
            gpa_scale_grade = self.grade["F"]
            letter_grade = "F" 
        return gpa_scale_grade, letter_grade
    

class GPA_calculator:
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
    
    def __init__(self, student_name, **modules):
        self.student_name = student_name
        self.modules = modules

    def calculate_gpa(self):
            gpa_scale_grades = []
            self.module_values = list(self.modules.values())
            for percentage_grade in self.module_values:
                if percentage_grade >= 90:
                    gpa_scale_grades.append(self.grade["A+"])
                elif percentage_grade >= 80:
                    gpa_scale_grades.append(self.grade["A"])
                elif percentage_grade >= 70:
                    gpa_scale_grades.append(self.grade["A-"])
                elif percentage_grade >= 67:
                    gpa_scale_grades.append(self.grade["B+"])
                elif percentage_grade >= 64:
                    gpa_scale_grades.append(self.grade["B"])
                elif percentage_grade >= 60:
                    gpa_scale_grades.append(self.grade["B-"])
                elif percentage_grade >= 57:
                    gpa_scale_grades.append(self.grade["C+"])
                elif percentage_grade >= 54:
                    gpa_scale_grades.append(self.grade["C"])
                elif percentage_grade >= 50:
                    gpa_scale_grades.append(self.grade["C-"])
                elif percentage_grade == 49:
                    gpa_scale_grades.append(self.grade["D+"])
                elif percentage_grade >= 47:
                    gpa_scale_grades.append(self.grade["D"])
                elif percentage_grade >= 45:
                    gpa_scale_grades.append(self.grade["D-"])
                elif percentage_grade == 44:
                    gpa_scale_grades.append(self.grade["E+"])
                elif percentage_grade >= 42:
                    gpa_scale_grades.append(self.grade["E"])
                elif percentage_grade >= 40:
                    gpa_scale_grades.append(self.grade["E-"])
                elif percentage_grade == 39:
                    gpa_scale_grades.append(self.grade["F+"])
                else: gpa_scale_grades.append(self.grade["F"])
            gpa = np.average(gpa_scale_grades)
            self.gpa_rounded = np.round(gpa, 2)
            return self.student_name, self.gpa_rounded
    
    def highest_scoring_module(self):
        self.sorted_modules = dict(sorted(self.modules.items(), key=lambda x: x[1]))
        highest_scoring_module = list(self.sorted_modules.keys())[-1]
        return self.student_name, highest_scoring_module

    def lowest_scoring_module(self):
        lowest_scoring_module = list(self.sorted_modules.keys())[0]
        return self.student_name, lowest_scoring_module
    
    def standard_deviation(self):
        st_deviation = np.std(self.module_values)
        st_deviation_rounded = round(st_deviation, 2) 
        return self.student_name, st_deviation_rounded
    
    def median(self):
        median = np.median(self.module_values)
        median_rounded = round(median, 2) 
        return self.student_name, median_rounded
    
    def letter_grades(self):
            letter_grades = []
            module_names = list(self.modules.keys())
            for percentage_grade in self.module_values:
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
            result = dict(zip(module_names, letter_grades))
            return self.student_name, result
    
    # double-check this function -and compare - still doesn't work
    # def next_highest(self, students):
    #     gpas = []
    #     gpa_sorted = sorted(gpas)
    #     for s in students:
    #         name, gpa = s.calculate_gpa()
    #         gpas.append(gpa)
    #     for i in gpa_sorted:
    #         if i > self.gpa_rounded:
    #             difference = np.round((i - self.gpa_rounded), 3)
    #     return self.student_name, difference
                        
def create_student():
    final_list = []
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
            marks_module_names = dict(zip(module_names, marks))
            s = GPA_calculator(name, **marks_module_names)
            final_list.append(s) 
    return final_list

def file_import():
    final_list = []
    filename = tkinter.filedialog.askopenfile()
    df = pd.read_csv(filename, index_col=0)
    dict_file = df.to_dict('index')
    for i in dict_file:
        s = GPA_calculator(i, **dict_file[i])
        final_list.append(s)
    return final_list


            
                
# main function
if __name__ == '__main__':
    os.system('cls')    
    student_objects = create_student() 
    gpas = []
    highest_scoring_modules = []
    lowest_scoring_modules = []
    st_deviations = []
    medians = []
    next_highest = []
    letter_grades = []
    for i in student_objects:
        gpa = i.calculate_gpa()
        gpas.append(gpa)
        highest_scoring_module = i.highest_scoring_module()
        highest_scoring_modules.append(highest_scoring_module)
        lowest_scoring_module = i.lowest_scoring_module()
        lowest_scoring_modules.append(lowest_scoring_module)
        standard_deviation = i.standard_deviation()
        st_deviations.append(standard_deviation)
        median = i.median()
        medians.append(median)
        # print(i.next_highest(student_objects))
        # next_highest.append(i)
        letter_grade = i.letter_grades()
        letter_grades.append(letter_grade)
    if len(student_objects) == 0:
        print('Not enough data')
        print('End')
    else: 
        print('\nGPA')
        print(f'{dict(gpas)}\n') 
        print('Highest scoring module')
        print(f'{dict(highest_scoring_modules)}\n') 
        print('Lowest scoring module')
        print(f'{dict(lowest_scoring_modules)}\n')
        print('Standard deviation')
        print(f'{dict(st_deviations)}\n')
        print('Median')
        print(f'{dict(medians)}\n')
        print('Grade point gap to the next highest GPA')       
        # print(f'{dict(next_highest)}\n')
        print('Letter grades')
        print(f'{dict(letter_grades)}\n')
        
        
    