###############  HW  Functions      HW  Functions         HW  Functions       ###############
#%%
# ######  QUESTION 1  for Loop with range function    ##########
# Write python codes to print out the four academic years for a typical undergrad will spend here at GW. 
# Starts with Sept 2021, ending with May 2025 (45 months in total), with printout like this:
# Sept 2021
# Oct 2021
# Nov 2021
# ...
# ...
# Apr 2025
# May 2025
# Hints:
# Review loop with range() function. Here is an example that orints out 12 months in year one row at a time:

# months = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec')
# years = (2021, 2022, 2023, 2024, 2025)
# for y in range(12):
    
#     print(months[y])

# Hint: If you consider the month and year as some function that involves the index of the tuple, think how you can print out Sept 2021.
# Then you can continue to loop the increment and get the desired year and month. (If the system messes up a month or two because of rounding, 
# that's okay.
    
    
months = ("Aug", "Sept", "Oct", "Nov", "Dec", "Jan", "Feb", "March", "April", "May")
year = 2021

for i in range(4):
    for m in range(10):
        if months[m] == "Jan":
            year += 1
        print(months[m], year)
 
       

###############  Now:     Functions          ###############
# We will now continue to complete the grade record that you worked on previously.

#%%
###################################### Question 2 ###############################
# let us write a function find_grade(total) that converts total (0-100) to the letter grade (see conversion table in syllabus)
# have a habbit of putting in the docstring. What should a docstring look like? See https://www.geeksforgeeks.org/python-docstrings/
total = 62.1

def find_grade(total):

    """This is a function to convert number grades to a letter grade

    Returns:
        Letter Grade
    """
    
    
    if total >= 93:
        letter_grade = 'A'
    elif total >= 90:
        letter_grade = 'A-'
    elif total >= 87:
        letter_grade = 'B+'
    elif total >= 83:
        letter_grade = 'B'
    elif total >= 80:
        letter_grade = 'B-'
    elif total >= 77:
        letter_grade = '+C+'
    elif total >= 73:
        letter_grade = 'C'
    elif total >= 70:
        letter_grade = 'C-'
    elif total >= 67:
        letter_grade = 'D+'
    elif total >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
        
    return letter_grade
# Check if the function works:
print(find_grade(total))


# What is the input (function argument) data type for total? 
print(type(total))

# What is the output (function return) data type for find_grade(total) ?
print(type(find_grade(total)))

#%%
###################################### Question 3 ###############################
# convert a letter grade to a grade point.
"""
A  = 4.00
A-  = 3.70
B+  = 3.30
B  = 3.00
B-  = 2.70
C+  = 2.30
C  = 2.00
C-  = 1.70
D+  = 1.30
D  = 1.00
D-  = 0.70
F  = 0.00
"""
grade = 'C-'

def to_gradepoint(grade):
  # write an appropriate and helpful docstring
  # ??????    fill in your codes here, be sure you have all A, A-, ... thru D, and F grades completed.
  # gradepoint = ???
    """ This function converts letter grades to grade point averges 

    Returns:
        gradepoint: GPA
    """
    if grade == "A":
        gradepoint = 4.00
    elif grade == "A-":
        gradepoint = 3.70
    elif grade == "B+":
        gradepoint = 3.30
    elif grade == "B":
        gradepoint = 3.00
    elif grade == "B-":
        gradepoint = 2.70
    elif grade == "C+":
        gradepoint = 2.30
    elif grade == "C":
        gradepoint = 1.70 
    elif grade == "C-":
        gradepoint = 1.70
    elif grade == "D+":
        gradepoint = 1.30
    elif grade == "D":
        gradepoint = 1.00
    elif grade == "D-":
        gradepoint = .70
    
    else:
        gradepoint = 0.00

    return gradepoint

# check your function:
print(to_gradepoint(grade))

#Please also answer these 2 questions:
# What is the input (function argument) data type for find_grade?
print(type(grade))


# # What is the output (function return) data type for find_grade(grade)?
print(type(to_gradepoint(grade)))

#%%
###################################### Question 4 ###############################
# next the function to_gradepoint_credit(course)
# which calculates the total weight grade points you earned in one course. Say A- with 3 credits, that's 11.1 total grade_point_credit
course = { "class":"IntroDS", "id":"DATS 6101", "semester":"spring", "year":2018, "grade":'B-', "credits":3 } 

def to_gradepoint_credit(course):
  # eventually, if you need to print out the value to 2 decimal, you can 
  # try something like this for floating point values %f
  # print(" %.2f " % grade_point_credit)
    """This function calculates the 


    Returns: " %.2f " % grade_point_credit
        
    """
    grade_point_credit = to_gradepoint(course['grade']) * course['credits']
    return grade_point_credit

# check to see if the function works:
print(" %.2f " % to_gradepoint_credit(course) )

# What is the input (function argument) data type for to_gradepoint_credit? 

print(type(to_gradepoint_credit(course)))

# What is the output (function return) data type for to_gradepoint_credit(course) ?

print(type(" %.2f " % to_gradepoint_credit(course) ))

#%%
###################################### Question 5 ###############################
# next the function gpa(courses) to calculate the GPA 
# It is acceptable syntax for list, dictionary, JSON and the likes to be spread over multiple lines.
courses = [ 
  { "class":"Intro to DS", "id":"DATS 6101", "semester":"spring", "year":2020, "grade":'B-', "credits":3 } , 
  { "class":"Data Warehousing", "id":"DATS 6102", "semester":"fall", "year":2020, "grade":'A-', "credits":4 } , 
  { "class":"Intro Data Mining", "id":"DATS 6103", "semester":"spring", "year":2020, "grade":'A', "credits":3 } ,
  { "class":"Machine Learning I", "id":"DATS 6202", "semester":"fall", "year":2020, "grade":'B+', "credits":4 } , 
  { "class":"Machine Learning II", "id":"DATS 6203", "semester":"spring", "year":2021, "grade":'A-', "credits":4 } , 
  { "class":"Visualization", "id":"DATS 6401", "semester":"spring", "year":2021, "grade":'C+', "credits":3 } , 
  { "class":"Capstone", "id":"DATS 6101", "semester":"fall", "year":2021, "grade":'A-', "credits":3 } 
  ]

def find_gpa(courses):
    """This function is to calculate the total gpa


    Returns:
        gpa
    """
    total_grade_point_credit = 0 # initialize 
    total_credits = 0
    
    
    for course in courses:
        gpc = course['credits'] * to_gradepoint(course['grade'])
        # print(f" gpc {gpc}")
        total_grade_point_credit += gpc
        # print(f"tgpc {total_grade_point_credit}")
        total_credits += course['credits']
        # print(total_credits)
    
    gpa = total_grade_point_credit / total_credits
   
    
    return gpa

# Try:
print(" %.2f " % find_gpa(courses) )

# What is the input (function argument) data type for find_gpa? 
# What is the output (function return) data type for find_gpa(courses) ?


#%%
###################################### Question 6 ###############################
# Write a function to print out a grade record for a single class. 
# The return statement for such functions should be None or just blank
# while during the function call, it will display the print.
course = { "class":"IntroDS", "id":"DATS 6101", "semester":"spring", "year":2018, "grade":'B-', "credits":3 } 

def printCourseRecord(course):
    """Function to print out a grade record for single class

    Returns:
        None or blank
    """

  # 2018 spring - DATS 6101 : Intro to DS (3 credits) B-  Grade point credits: 8.10 
    print(f"{course['year']} {course['semester']} - {course['id']} : {course['class']} ({course['credits']} credits) {course['grade']} Grade Point Credit: {' %.2f ' % to_gradepoint_credit(course)}")
  
    return None
  
# check if the function works:
printCourseRecord(course)

# What is the input (function argument) data type for printCourseRecord? 
print(type(course))
# What is the output (function return) data type for printCourseRecord(course) ?

print(type(printCourseRecord(course)))
#%%
###################################### Question 7 ###############################
#print out the complete transcript and the gpa at the end
# 2018 spring - DATS 6101 : Intro to DS (3 credits) B-  Grade point credits: 8.10 
# 2018 fall - DATS 6102 : Data Warehousing (4 credits) A-  Grade point credits: 14.80 
# 
# Cumulative GPA: 
 
def printTranscript(courses):
  # write an appropriate and helpful docstring
  for course in courses:
    # print out each record as before
  
  # after the completion of the loop, print out a new line with the gpa info
  
  return # or return None

# Try to run, see if it works as expected to produce the desired result
# courses is already definted in Q4
printTranscript(courses)
# The transcript should exactly look like this: 
# 2020 spring - DATS 6101 : Intro to DS (3 credits) B- Grade point credits: 8.10
# 2020 fall - DATS 6102 : Data Warehousing (4 credits) A- Grade point credits: 14.80
# 2020 spring - DATS 6103 : Intro Data Mining (3 credits) A Grade point credits: 12.00
# 2020 fall - DATS 6202 : Machine Learning I (4 credits) B+ Grade point credits: 13.20
# 2021 spring - DATS 6203 : Machine Learning II (4 credits) A- Grade point credits: 14.80
# 2021 spring - DATS 6401 : Visualization (3 credits) C+ Grade point credits: 6.90
# 2021 fall - DATS 6101 : Capstone (3 credits) A- Grade point credits: 11.10
# Cumulative GPA: 3.37

# What is the input (function argument) data type for printTranscript? 
# What is the output (function return) data type for printTranscript(courses) ?



#%% 
# ######  QUESTION 8   Recursive function   ##########
# What is recursive function? Review out class notes: https://docs.google.com/document/d/1PTEBHBASfeYMmuFIE04diRiDpWynvt2v-mizwDW2GW0/edit#
# Write a recursive function that calculates the Fibonacci sequence (https://www.mathsisfun.com/numbers/fibonacci-sequence.html)
# The recusive relation is fib(n) = fib(n-1) + fib(n-2), 
# and the typically choice of seed values are fib(0) = 0, fib(1) = 1. 
# From there, we can build fib(2) and onwards to be 
# fib(2)=1, fib(3)=2, fib(4)=3, fib(5)=5, fib(6)=8, fib(7)=13, ...
# Let's set it up from here:

def fib(n):
  """
  Finding the Fibonacci sequence with seeds of 0 and 1
  The sequence is 0,1,1,2,3,5,8,13,..., where 
  the recursive relation is fib(n) = fib(n-1) + fib(n-2)
  :param n: the index, starting from 0
  :return: the sequence
  """
  # assume n is positive integer
  # ??????    fill in your codes here

  return # return what ????


# Try:
for i in range(12):
  print(fib(i))  



#%% 
# ######  QUESTION 9   Recursive function   ##########
# Similar to the Fibonacci sequence, let us create a function that has a  
# modified recusive relation dm_fibonacci(n) = dm_fibonacci(n-1) + 2* dm_fibonacci(n-2) - dm_fibonacci(n-3). 
# Pay attention to the coefficients and their signs. 
# And let us choose the seed values to be dm_fibonacci(0) = 1, dm_fibonacci(1) = 1, dm_fibonacci(2) = 2. 
# From there, we can build dm_fibonacci(3) and onwards to be 1,1,2,3,6,10,...
# Let's set it up from here:

def dm_fibonacci(n):
  """
  Finding the dm_Fibonacci sequence with seeds of 1, 1, 2 for n = 0, 1, 2 respectively
  The sequence is 1,1,2,3,6,10,..., where 
  the recursive relation is dm_fibonancci(n) = dm_fibonancci(n-1) + 2* dm_fibonancci(n-2) - dm_fibonancci(n-3)
  :param n: the index, starting from 0
  :return: the sequence
  """
  # assume n is positive integer
  # ??????    fill in your codes here

  return # return what ????

for i in range(12):
  print(dm_fibonancci(i))  # should gives 1,1,2,3,6,10,...


#%%
