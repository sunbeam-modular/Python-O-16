import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def function1():
    # dataset
    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    temperatrues = [10, 23, 25, 24, 27, 28, 28, 29, 30, 31]

    # scatter plot
    # plt.scatter(days, temperatrues)

    # markers: o, <, >, ^, *, s
    plt.scatter(days, temperatrues, color="red", marker='s', label="temperature")

    # add the axes lables
    plt.xlabel("days")
    plt.ylabel("temperatures")
    plt.title("Temperature data")

    # show the legend
    plt.legend()

    # chart background customization
    plt.grid(True, alpha=0.4)
    plt.tight_layout()

    # save the chart to an image
    plt.savefig("scatter_plot.png")

    # display the chart
    plt.show()

# function1()

def function2():
    # read the data from a file
    df = pd.read_csv("Salary_Data.csv")

    # plot a line chart
    # linestyle: '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
    plt.plot(
        df['YearsExperience'], 
        df['Salary'], 
        color="green", 
        linewidth=2,
        linestyle="dotted",
        label="Salary"
    )

    # draw a scatter plot
    # plt.scatter(
    #     df['YearsExperience'], 
    #     df['Salary'], 
    #     color="green"
    # )

    # add the axes lables
    plt.xlabel("experience")
    plt.ylabel("salary")
    plt.title("Experience vs Salary")

    # show the legend
    plt.legend()

    # chart background customization
    plt.grid(True, alpha=0.4)
    plt.tight_layout()

    # display the chart
    plt.show()

# function2()

def function3():
    # dataset
    subjects = ['maths', 'english', 'science', 'social science', 'hindi']
    marks = [46, 20, 45, 30, 36]

    # create a bar chart
    plt.bar(
        subjects, 
        marks, 
        color="orange",
        label="marks",
        width=0.5,
        edgecolor="black",
        linewidth=2)

    # add the axes lables
    plt.xlabel("subjects")
    plt.ylabel("marks")
    plt.title("Student Sore Card")

    # show the legend
    plt.legend()

    # chart background customization
    plt.grid(True, alpha=0.4)
    plt.tight_layout()

    # display the chart
    plt.show()

# function3()

def function4():
    # dataset
    subjects = ['maths', 'english', 'science', 'social science', 'hindi']
    marks = [46, 20, 45, 30, 36]

    # create a horizontal bar chart
    plt.barh(
        subjects, 
        marks, 
        color="orange",
        label="marks",
        edgecolor="black",
        linewidth=2)

    # add the axes lables
    plt.xlabel("subjects")
    plt.ylabel("marks")
    plt.title("Student Sore Card")

    # show the legend
    plt.legend()

    # chart background customization
    plt.grid(True, alpha=0.4)
    plt.tight_layout()

    # display the chart
    plt.show()

# function4()

def function5():
    # dataset
    subjects = ['maths', 'english', 'science', 'social science', 'hindi']
    marks = [46, 50, 45, 30, 16]

    # initialize all the positions to 0
    explode = np.zeros(len(marks))

    # set the explode property of max value
    # explode[np.argmax(marks)] = 0.1
    explode[np.argmin(marks)] = 0.1

    # create a pie chart
    plt.pie(
        marks,
        autopct="%.2f%%",
        explode=explode,
        # shadow=True,
        labels=subjects)
    
    # add the lables
    plt.title("Student Sore Card")

    # chart background customization
    plt.tight_layout()

    # display the chart
    plt.show()

# function5()

def function6():
    # dataset
    subjects = ['maths', 'english', 'science', 'social science', 'hindi']
    marks = []

    try: 

        # get the marks from user
        for subject in subjects:
            subject_marks = int(input(f"marks for {subject} = "))
            marks.append(subject_marks)

        # initialize all the positions to 0
        explode = np.zeros(len(marks))

        # set the explode property of max value
        # explode[np.argmax(marks)] = 0.1
        explode[np.argmin(marks)] = 0.1

        # create a pie chart
        plt.pie(
            marks,
            autopct="%.2f%%",
            explode=explode,
            # shadow=True,
            labels=subjects)
        
        # add the lables
        plt.title("Student Sore Card")

        # chart background customization
        plt.tight_layout()

        # display the chart
        plt.show()
    except:
        print("wrong data type detected, please enter numeric marks")

function6()