
# coding: utf-8


import xlrd
import xlwt

import random

from math import floor



class Student():
    
    def __init__(self, sciper=12345, sex="M", name="John Smith"):
        self.data = {    
            'SCIPER' : int(sciper),
            'sex' : sex,
            'name' : name,
            'group' : 0,
            'nationality' : "none",
            'phone' : "none",
            'email' : "gaspar@epfl.ch",
            'facebook_invited' : False,
            'facebook_member' : False
        }
    
    def show(self):
        print(str(self.data['SCIPER'])+"; "+self.data['sex']+"; "+self.data['name'])



def open_workbook():
    
    filename_valid = False
    while not filename_valid:
        filename = input("Enter filename : ")
        filename_valid = True
        try:
            workbook = xlrd.open_workbook(filename)
        except:
            filename_valid = False
            print("Unable to open file...")
    
    print("\n Opened " + str(filename))
    
    # check the import parameters
    
    print("\nThis workbook contains the following sheets:")
    print(workbook.sheet_names())
    sheet_index = int(input("Which sheet contains the data? : "))
    
    sheet = workbook.sheet_by_index(sheet_index)
    
    print("\nThese are the first 5 rows beginnings of the sheet : \n")
    for i in range(0,5):
        line = "Line " + str(i) + " : "
        for j in range(0,3):
            line += str(sheet.cell(i,j).value) + "; "
        print(line)
    row = int(input("Which row contains the column headers? : "))
    
    print("\nThese are the headers:")
    for i in range(0,sheet.ncols):
        print(str(i) + " : " + str(sheet.cell(row,i).value))
    
    return sheet, row



def import_column(students,sheet=None,header_row=None,sciper=None):
    
    if sheet == None:
        sheet, header_row = open_workbook()
    
    sample = Student(12324,"M","John Smith")
    
    print("\nYou can add one of the following keys:")
    for k in sample.data.keys():
        print(k)
    
    
    valid_key = False
    while not valid_key:
        key = input("Which key do you want to add to ? : ")
        if key in sample.data.keys():
            valid_key = True
        else:
            print("Key invalid")
    
    print("\nWhich column contains :")
    if (sciper == None):
        sciper = int(input("SCIPER : "))
    column = int(input("your data : "))
    
    for i in range(header_row+1,sheet.nrows):
        row = sheet.row(i)
        for student in students:
            if student.data['SCIPER'] == row[sciper].value:
                student.data[key] = row[column].value
    
    return students
    


def import_check_headers():

    sheet, header_row = open_workbook()
    
    print("\nWhich column contains the :")
    name = int(input("Name : "))
    sciper = int(input("SCIPER : "))
    sex = int(input("Sex : "))
    
    # start importing
    
    students = []
    for i in range(header_row+1,sheet.nrows):
        row = sheet.row(i)
        
        # change empty SCIPER fields to 0
        if (row[sciper].value == 'No Sciper'):
            row[sciper].value = 0
        
        # infer sex from saluation
        if (row[sex].value == "Madame"):
            row[sex].value = "F"
        elif (row[sex].value == "Monsieur"):
            row[sex].value = "M"
        
        students.append(Student(row[sciper].value,row[sex].value,row[name].value))

    while True:
        answer = input("Input more keys from this file (y/n) ? : ")
        if answer == "n":
            break
        elif answer == "y":
            import_column(students,sheet,header_row,sciper)

    return students



def import_safe_file(filename):

    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_index(0)

    # get the column headers to use as keys
    keys = []
    for i in range(0,sheet.ncols):
        keys.append(sheet.cell(0,i))
    
    # get the student data
    students = []
    for i in range(1,sheet.nrows):
        student = Student()
        for j in range(0,sheet.ncols):
            key = sheet.cell(0,j).value
            student.data[key] = sheet.cell(i,j).value
        students.append(student)

    return students



def write_to_file(student_list,filename):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Sheet1")
    
    # write the column headers
    j = int(0)
    for k in student_list[0].data.keys():
        sheet.write(0,j,k)
        j += 1

    # write the data per student
    i = int(1)
    for student in student_list:
        j = int(0)
        for k in student.data.keys(): 
            sheet.write(i,j,student.data[k])
            j += 1
        i += 1
    
    workbook.save(filename)



def merge_students(old_list,new_list):
    """
    This function will merge an old and new list of students, while
    keeping info from the old data.
    The merge is based in SCIPER numbering
    """
    merged_list = []
    for new_student in new_list:
        existed = False
        for old_student in old_list:

            # check student id by SCIPER
            if new_student.data['SCIPER'] == old_student.data['SCIPER']:
                existed = True

                # check if email has been updated, use new email
                email = new_student.data['email']
                if not (email == "none" or email == "mailto:" or email == ""):
                    old_student.data['email'] = new_student.data['email']
                
                # check if nationality has been updates, use new data
                nat = new_student.data['nationality']
                if not (nat == "none" or nat == ""):
                    old_student.data['nationality'] = new_student.data['nationality']

                merged_list.append(old_student)
                break

        # if this is a new student, add to students  
        if existed == False:
            merged_list.append(new_student)
    return merged_list

def find_updated_students(old_list,new_list):
    updated_students = []

    for new_student in new_list:
        for old_student in old_list:

            # check student id by SCIPER
            if new_student.data['SCIPER'] == old_student.data['SCIPER']:
                updated = False

                email = new_student.data['email']
                if not (email == "none" or email == "mailto:" or email == ""):
                    if not (email == old_student.data['email']):
                        updated = True

                nat = new_student.data['nationality']
                if not (nat == "none" or nat == ""):
                    if not (nat == old_student.data['nationality']):
                        updated = True

                if updated:
                    updated_students.append(new_student)
                break

    return updated_students



def find_new_students(old_list,new_list):
    new_students = []
    for new_student in new_list:
        existed = False
        for old_student in old_list:
            if new_student.data['SCIPER'] == old_student.data['SCIPER']:
                existed = True
                break
        if existed == False:
            new_students.append(new_student)
    
    return new_students



def assign_students(students,num_groups):
    
    # find required group size
    unassigned = get_students_by_group(students,0)
    group_size = floor(len(unassigned) / (num_groups - 1))
    
    print("Distributing " + str(len(unassigned))+" into "+str(num_groups))
    print("Using a group size of " + str(group_size))
    
    # assign students to each group
    for i in range(1,num_groups):
        placed = 0
        while (placed < group_size):
            j = random.randrange(0,len(unassigned))
            if students[j].data['group'] == 0:
                students[j].data['group'] = i
                placed += 1
    
    # assign the students that have been left out
    placed_positions = []
    for student in students:
        if student.data['group'] == 0:
            placed = False
            while not placed:
                i = random.randrange(1,num_groups)
                
                # make sure not to assign two overflow students
                # to the same group, since they can all fit once
                
                if i not in placed_positions:
                    placed_positions.append(i)
                    student.data['group'] = i
                    placed = True
                
        
    return students

def get_students_by_group(students,group):
    current = []
    for student in students:
        if student.data['group'] == group:
            current.append(student)
    return current



def show_group_stats(students,group_num):
    group = get_students_by_group(students,group_num)
    
    print("\nStats for group " + str(group_num))
    print("Number of students: " + str(len(group)))
    m = float(0)
    for student in group:
        if student.data['sex'] == "M":
            m = m+1
    part_male = m / float(len(group))
    print("Percentage male: " + str(part_male))
