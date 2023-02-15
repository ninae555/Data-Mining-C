#%%
# Question 1
# Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

import numpy as np

x = np.arange(2, 11).reshape((3, 3))
print(x)

#%%
import q1data as q1
# After the import, you will have a dictionary called 
q1.courselist
print(f"Length: {len(q1.courselist)}")
# For convenience, let us give it a local name
courses = q1.courselist 
print(courses[0])

#%%[markdown]
# Do not import any other libraries to perform this task.
# 
# I have an agressive plan to take all the python courses on a website, within the month of March. 
# To make a plan, I need to loop through all the courses, starting March 1 (2022) which is a 
# Tuesday, and assuming I will spend 8 hours a day, 7 days a week, to finish them all in March.
# The schedule is printed out like this:
# 
# Mar 1 (Tue): Supervised Learning with scikit-learn : 4.0 hour
# Mar 1 (Tue): Python Data Science Toolbox (Part 1) : 3.0 hour
# Mar 1 (Tue): Introduction to Python : 4.0 hour
# Mar 2 (Wed): Intermediate Python : 4.0 hour
# Mar 2 (Wed): Introduction to Data Science in Python : 4.0 hour
# Mar 3 (Thu): Data Manipulation with pandas : 4.0 hour
# Mar 3 (Thu): Python Data Science Toolbox (Part 2) : 4.0 hour
# Mar 4 (Fri): Joining Data with pandas : 4.0 hour
# Mar 4 (Fri): Introduction to Data Visualization with Matplotlib : 4.0 hour
# Mar 5 (Sat): Introduction to Importing Data in Python : 3.0 hour
# Mar 5 (Sat): Cleaning Data in Python : 4.0 hour
# Mar 6 (Sun): Introduction to Data Visualization with Seaborn : 4.0 hour
# Mar 6 (Sun): Statistical Thinking in Python (Part 1) : 3.0 hour
# Mar 7 (Mon): Writing Efficient Python Code : 4.0 hour
# Mar 7 (Mon): Exploratory Data Analysis in Python : 4.0 hour
# ..........
# 
# As you can see, in the first day, I can complete a little more than 2 courses, 
# then start the third course "Introduction to Python". I will resume this third 
# course on day 2 with 3 hours of learning left (without printing out 
# that line again for March 2, but keep track of how many hours left for the 
# day to learn). So continue with the next courses, and stop after 1 hour 
# of "Introduction to Data Science in Python" on March 2, etc.
# 
# Print out the entire schedule for all the courses. It is an 
# agressive 30-day plan.
# 
# # course list with (course name, duration in hours) tuple
course_list = [("Supervised Learning with scikit-learn", 4.0),
               ("Python Data Science Toolbox (Part 1)", 3.0),
               ("Introduction to Python", 4.0),
               ("Intermediate Python", 4.0),
               ("Introduction to Data Science in Python", 4.0),
               ("Data Manipulation with pandas", 4.0),
               ("Python Data Science Toolbox (Part 2)", 4.0),
               ("Joining Data with pandas", 4.0),
               ("Introduction to Data Visualization with Matplotlib", 4.0),
               ("Introduction to Importing Data in Python", 3.0),
               ("Cleaning Data in Python", 4.0),
               ("Introduction to Data Visualization with Seaborn", 4.0),
               ("Statistical Thinking in Python (Part 1)", 3.0),
               ("Writing Efficient Python Code", 4.0),
               ("Exploratory Data Analysis in Python", 4.0),
               ("Statistical Thinking in Python (Part 2)", 3.0),
               ("Python Data Science Toolbox (Part 3)", 3.0),
               ("Analyzing Police Activity with pandas", 4.0),
               ("Interactive Data Visualization with Bokeh", 3.0),
               ("Manipulating Time Series Data in Python", 4.0),
               ("Cluster Analysis in Python", 4.0),
               ("Applied Social Network Analysis in Python", 4.0)]

# start date and time
start_date = "2022-03-01"
start_day = 1

# initialize hours left in the day
hours_left = 8.0

# loop through the course list
for i, course in enumerate(course_list):
    # calculate the end date and time for the current course
    days, hours = divmod(course[1], hours_left)
    end_date = (start_day + days) % 7 + 1
    end_time = (hours_left + hours) % 8

    # print the course schedule
    print(f"Mar {int(end_date)} ({'Mon' if end_date == 1 else 'Tue' if end_date == 2 else 'Wed' if end_date == 3 else 'Thu' if end_date == 4 else 'Fri' if end_date == 5 else 'Sat' if end_date == 6 else 'Sun'}): {course[0]} : {min(course[1], hours_left):.1f} hour")
    # update the start date and time for the next course
    start_day = end_date
    hours_left = 8.0 if end_time == 0 else 8.0 - end_time


# %%
#%%
# Question 2
# loop through the list of courses and their hours, and print (like below).
# 
# Supervised Learning with scikit-learn : 4.0 hour
# Python Data Science Toolbox (Part 1) : 3.0 hour
# Introduction to Python : 4.0 hour
# ...
#
# for course in courses:
for course in course_list:
    print(f"{course[0]} : {course[1]:.1f} hour")


#%%
# Question 3
# Try to put in the date in March (variable marchdate) on the printout as well.
# If the date value is not what is expected, try using the debugger to inspect the different values at different steps.
# You will need to keep a running total of how many hours left for each day before increment of the marchdate value. 
# The running total is being tracked using hourofdayleft variable. 
# Try to produce printout like this:
#
# Mar 1 : Supervised Learning with scikit-learn : 4.0 hour
# Mar 1 : Python Data Science Toolbox (Part 1) : 3.0 hour
# Mar 1 : Introduction to Python : 4.0 hour
# Mar 2 : Intermediate Python : 4.0 hour
# Mar 2 : Introduction to Data Science in Python : 4.0 hour
# Mar 3 : Data Manipulation with pandas : 4.0 hour
# Mar 3 : Python Data Science Toolbox (Part 2) : 4.0 hour
# ...


course_list = [    ['Supervised Learning with scikit-learn', 4.0],
    ['Python Data Science Toolbox (Part 1)', 3.0],
    ['Introduction to Python', 4.0],
    ['Intermediate Python', 4.0],
    ['Introduction to Data Science in Python', 4.0],
    ['Data Manipulation with pandas', 4.0],
    ['Python Data Science Toolbox (Part 2)', 4.0]
]

import numpy as np
marchdate = 1     # March dates from 1, 2, ... , 31, increment by 1 after each filled day
hourofdayleft = 8   # Keep a running total of hours left after taken a course. Starting with 8 hours on the first day


for course in course_list:
    while course[1] > 0:
        if hourofdayleft == 0:
            marchdate += 1
            hourofdayleft = 8
        print(f"Mar {marchdate} : {course[0]} : {min(course[1], hourofdayleft):.1f} hour")
        hourofdayleft -= min(course[1], hourofdayleft)
        course[1] -= min(course[1], hourofdayleft)

print(f"Total days needed: {marchdate - 1}")




#%%
# Question 4
# Try to put in the final piece of info to the print line. 
#

dayofweektuple = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat')
marchdate = 1     # March dates from 1, 2, ... , 31, increment by 1 after each filled day
hourofdayleft = 8   # Keep a running total of hours left after taken a course. Starting with 8 hours on the first day

for course in course_list:
    while course[1] > 0:
        if hourofdayleft == 0:
            marchdate += 1
            hourofdayleft = 8
        dayofweek = dayofweektuple[marchdate % 7]
        print(f"Mar {marchdate} ({dayofweek}): {course[0]} : {min(course[1], hourofdayleft):.1f} hour")
        hourofdayleft -= min(course[1], hourofdayleft)
        course[1] -= min(course[1], hourofdayleft)
        if hourofdayleft == 0:
            hourofdayleft = 8

print(f"Total days needed: {marchdate - 1}")
#%%





# %%
