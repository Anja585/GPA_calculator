import os
import numpy as np

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
    def __init__(self, student_name, pairs):
        self.student_name = student_name
        self.pairs = pairs

    def __repr__(self):
        return f'({self.student_name}, {self.pairs})'
    
    def calculate_gpa(self):
            gpa_scale_grades = []
            for percentage_grade in self.pairs:
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
            gpa_rounded = np.round(gpa, 2)
            return gpa_rounded

    def highest_scoring_module(self):
        pair_keys = list(self.pairs.keys())
        pair_keys.sort()
        sorted_pairs = {i: self.pairs[i] for i in pair_keys}
        highest_scoring_module = list(sorted_pairs.values())[-1]
        return highest_scoring_module    
    
    def lowest_scoring_module(self):
        pair_keys = list(self.pairs.keys())
        pair_keys.sort()
        sorted_pairs = {i: self.pairs[i] for i in pair_keys}
        lowest_scoring_module = list(sorted_pairs.values())[0]
        return lowest_scoring_module
    
    def standard_deviation(self):
        pair_keys = list(self.pairs.keys())    
        st_deviation = np.std(pair_keys)
        st_deviation_rounded = round(st_deviation, 2) 
        return st_deviation_rounded
    
    def median(self):
        pair_keys = list(self.pairs.keys())  
        median = np.median(pair_keys)
        median_rounded = round(median, 2) 
        return median_rounded
    
    def letter_grades(self):
            letter_grades = []
            module_names = list(self.pairs.values())
            for percentage_grade in self.pairs:
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
            return result

            

# a = GPA_calculator('Anja', {90:'data', 80:"machine"})   
# print(a.highest_scoring_module())


# main function
if __name__ == '__main__':
    os.system('cls')    
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
    
    
    # final_list = dict(zip(names, marks_module_names))
    # if len(list(final_list.keys())) == 0:
    #     print('Not enough data')
    #     print('End')
    