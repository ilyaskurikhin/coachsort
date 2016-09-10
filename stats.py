
# coding: utf-8

import student as s
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


# create a pretty color scheme
a = np.random.random(10)
cs = cm.Set1(np.arange(10)/10.)
fig_size = (6,6)

def plot_nationality(students,title):
    nationalities = []
    for student in students:
        nationalities.append(student.data['nationality'])

    counted = {}
    for i,nat in enumerate(nationalities):
        if nat in counted:
            counted[nat] += 1
        else:
            counted[nat] = 1
           
    values, names = [[],[]]
    counted['autre'] = 0
    for k in counted.keys():
        if counted[k] < 5 and k is not 'autre':
            counted['autre'] += counted[k]
            counted[k] = 0
        elif (k is not 'autre'):
            values.append(counted[k])
            names.append(k)

    values.append(counted['autre'])
    names.append("autre")
            
    plt.pie(values, 
            labels=names,
            autopct='%1.1f%%',
            colors=cs,
            startangle=90,
            pctdistance=0.8)
    plt.axis('square')
    plt.title(title, y=1.1)
    plt.show()


def plot_repeating(students,repeating,title):
    num_repeating = 0
    for student in students:
        for rep in repeating:
            if student.data['SCIPER'] == rep.data['SCIPER']:
                num_repeating += 1
                break

    plt.pie([num_repeating,len(students)],
            labels=["redoublant","non redoublant"], 
            autopct='%1.1f%%',
            colors=cs,
            startangle=90)
    plt.axis('square')
    plt.title(title, y=1.1)
    plt.show()

def plot_sex(students,title):

    num_m = len(s.get_students_by_keys(students,{'sex':"M"}))
    num_f = len(s.get_students_by_keys(students,{'sex':"F"}))

    plt.pie([num_m,num_f],
            labels=["homme","femme"],
            autopct='%1.1f%%',
            colors=cs,
            startangle=90)
    plt.axis('square')
    plt.title(title, y=1.1)
    plt.show()



def plot_nationalities_by_year(classes,title):
    # create array of available years so that they are in order
    years = []
    for year in classes.keys():
        years.append(year)
    years.sort()

    # get list of nationalities per year
    nationality_years = {}
    for year in years:
        nationality_years[year] = []
        for student in classes[year]:
            nationality_years[year].append(student.data['nationality'])


    # count nationailty per year
    count_per_year = {}
    for year in years:
        count_per_year[year] = {}
        for nat in nationality_years[year]:
            if nat in count_per_year[year].keys():
                count_per_year[year][nat] += 1
            else:
                count_per_year[year][nat] = 1


    # convert to country based so that we have one line per country
    graph_data = {}
    for year in years:
        for nat in count_per_year[year].keys():
            if nat in graph_data.keys():
                graph_data[nat][year] = count_per_year[year][nat]
            else:
                graph_data[nat] = {}
                graph_data[nat][year] = count_per_year[year][nat] 


    # initialize 'autre' category
    graph_data['autre'] = {}
    for year in years:
        graph_data['autre'][year] = 0


    # fill empty data with zeroes
    to_delete = []
    for nat in graph_data.keys():
        nat_sum = 0
        for year in years:
            if year not in graph_data[nat].keys():
                graph_data[nat][year] = 0
            else:
                nat_sum += graph_data[nat][year]

        # move nat with less than 2 average to 'autre' category
        if nat_sum < 2*len(years):
            for year in years:
                graph_data['autre'][year] += graph_data[nat][year]
                graph_data[nat][year] = 0
                to_delete.append(nat)

    # remove excess graphs accounted for by 'autre'
    for nat in to_delete:
        if nat in graph_data.keys():
            del graph_data[nat]


    fig, ax = plt.subplots()

    for nat in graph_data.keys():
        values = []
        for year in years:
            values.append(graph_data[nat][year])
        ax.plot(values,label=str(nat))

    legend = ax.legend(bbox_to_anchor=(1.4,1.0))
    
    plt.xticks(range(len(years)),years)
    plt.title(title)
    plt.show()


def plot_nat_percentage_by_year(classes,title):
    
    # create array of available years so that they are in order
    years = []
    for year in classes.keys():
        years.append(year)
    years.sort()

    # get list of nationalities per year
    nationality_years = {}
    for year in years:
        nationality_years[year] = []
        for student in classes[year]:
            nationality_years[year].append(student.data['nationality'])


    # count nationailty per year
    count_per_year = {}
    for year in years:
        count_per_year[year] = {}
        for nat in nationality_years[year]:
            if nat in count_per_year[year].keys():
                count_per_year[year][nat] += 1
            else:
                count_per_year[year][nat] = 1


    # convert to country based so that we have one line per country
    graph_data = {}
    for year in years:
        for nat in count_per_year[year].keys():
            if nat in graph_data.keys():
                graph_data[nat][year] = count_per_year[year][nat] / len(classes[year]) 
            else:
                graph_data[nat] = {}
                graph_data[nat][year] = count_per_year[year][nat] / len(classes[year])


    # initialize 'autre' category
    graph_data['autre'] = {}
    for year in years:
        graph_data['autre'][year] = 0


    # fill empty data with zeroes
    to_delete = []
    for nat in graph_data.keys():
        nat_sum = 0
        for year in years:
            if year not in graph_data[nat].keys():
                graph_data[nat][year] = 0
            else:
                nat_sum += graph_data[nat][year]

        # move nat with less than 2 average to 'autre' category
        if nat_sum < 0.01*len(years):
            for year in years:
                graph_data['autre'][year] += graph_data[nat][year]
                graph_data[nat][year] = 0
                to_delete.append(nat)

    # remove excess graphs accounted for by 'autre'
    for nat in to_delete:
        if nat in graph_data.keys():
            del graph_data[nat]


    fig, ax = plt.subplots()

    for nat in graph_data.keys():
        values = []
        for year in years:
            values.append(graph_data[nat][year])
        ax.plot(values,label=str(nat))

    legend = ax.legend(bbox_to_anchor=(1.4,1.0))
    
    plt.xticks(range(len(years)),years)
    plt.title(title)
    plt.show()
