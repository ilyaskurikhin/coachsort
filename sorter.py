"""
 ~~~~  CoachAssigner3000 ~~~~~~



"""

import random

def sortStudents(listfile) :
    """ Open text file containing list of students, and sort them into two
    lists, guys and girls.         

    Note: the file must be in the format <gender>\t<name> 
        
    """
    guys = []
    girls = []

    for line in listfile:
        currentLine = line.strip('\n')
        currentLine = currentLine.split('\t')
        if currentLine[0] == "Monsieur":
            guys.append(currentLine[1])
        elif currentLine[0] == "Madame":
            girls.append(currentLine[1])

    return guys, girls


def addCoaches(coachfile=None) :
    """ Get coach names from the user or file. 
    Add each group of coaches to a list, and return the list
    of these lists.
    """
    coaches = [] 

    # Get em from the supplied file
    for line in coachfile:
        line = line.strip()
        c = line.split(',')
        for i in c :
            i = i.strip()
        coaches.append(c)

    return coaches

def distribute(array, dest_size) :
    """ Take a list, and return a new list of lists of size dest_size. This
    is sort of like dealing a deck of cards to n players.
    """
    newlist = [[] for _ in range(dest_size)]

    i = random.randrange(0, dest_size)
    for item in array:
        newlist[i].append(item)
        if i < dest_size - 1 :
            i += 1
        else :
            i = 0

    return newlist


def assignStudentsToCoaches(coaches, guys, girls) :
    """ Assign students to each pair of coaches, return a dictionary with
    (coach n-tuple) -> (assigned students list)
    """
    
    # First, remove coaches from students list
    for c in coaches:
        if c in guys:
            guys.remove(c)
        if c in girls:
            girls.remove(c)

    guys_d = distribute(guys, len(coaches))
    girls_d = distribute(girls, len(coaches))
   
    groups = {}
    for c in coaches:
        groups[tuple(c)] = guys_d[coaches.index(c)]
        groups[tuple(c)].extend(girls_d[coaches.index(c)])

    return groups

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
    # TODO: supply file name as argv

    print("Enter the name of the file containing the list of students")
    sfile = openFile()
    guys, girls = sortStudents(sfile)
    sfile.close()

    random.shuffle(guys)
    random.shuffle(girls)
   
    n_girls = len(girls)
    n_guys = len(guys)
    total = n_girls + n_guys
   
    print("Total number of students: ", total)
    print("Girls : {0} ({1:.2%})".format(n_girls, n_girls/total))
    print("Guys : {0} ({1:.2%})".format(n_guys, n_guys/total))

    print("------------------------")
    print("Enter the name of the file containing the list of coaches")
    cfile = openFile()
    coaches = addCoaches(cfile)
    cfile.close()
    print("Added {0} coaches".format(len(coaches)))

    groups = assignStudentsToCoaches(coaches, guys, girls)
   
    # print the groups to a file
    gfile = open("groups.txt", 'w')
    for c, s in groups.items() :
        line = ""
        for i in c:
            line = line + i + ", "
        line = line.rstrip(', ')
        line += "\t" 
        print(line, end='', file=gfile)
        
        line = ""
        for i in s:
            line = line + i + "\n\t"
        line = line.rstrip()
        print(line, file=gfile)
    
    gfile.close()
    gfile = open("groups.txt", 'r')
    print("Groups created and written to file \"groups.txt\"")

    for line in gfile:
        print(line)

    gfile.close()
