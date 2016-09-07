#coding: utf-8
"""
remover.py

Removes all elements from a file which also belong to another file.
Useful to remove 2nd 1st years from the list of 1st years (les redoublants ne
seront pas dans des groupes de coachés).

/!\ minimum required version: python 3. Some parts (print(), open() etc) are
incompatible with python2.7.

"""


def openFile() :
    f = None
    while f == None :
        filename = input("File name: ")
        try:
            f = open(filename, 'r')
        except:
            print("Unable to open file. Please make sure the file exists and"
                    "try again, or press Ctrl-C to stop the program.")

    return f

if __name__ == '__main__':
    print("Enter new list filename")
    newlist = openFile()
    print("Enter old list filename")
    oldlist = openFile()

    students = []

    for line in newlist:
        students.append(line)

    for line in oldlist:
        if line in students:
            students.remove(line)

    sfile = open("studentlist.txt", 'w')
    for line in students:
        print(line, file=sfile, end='')

    print("{0} new students".format(len(students)))
    print("List of new students output to 'studentlist.txt'")

    sfile.close()
    newlist.close()
    oldlist.close()
