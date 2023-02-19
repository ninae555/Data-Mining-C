
# =================================================================
# %%
#%%
# print("Hello world!")

#%%
# Question 1: From last homework, we have a list of classes. At the end of your studies here, you now have all the grades.
courses = [ { "CourseNumber" : "DATS 6101", 
            "CourseTitle" : "Introduction to Data Science", 
            "Year" : 2021,
            "Semester" : "Spring", 
            "Grade" : 85.5,
            "Lettergrade" : "",
            "Instructor" : "Divya Pandove"
            } , 
            { "CourseNumber" : "DATS 6102", 
            "CourseTitle" : "Data Warehousing", 
            "Year" : 2021,
            "Semester" : "Spring", 
            "Grade" : 95.5,
            "Lettergrade" : "",
            "Instructor" : "Abdi Awl"
            } ,
            { "CourseNumber" : "DATS 6103", 
            "CourseTitle" : "Introduction to Data Mining", 
            "Year" : 2021,
            "Semester" : "Spring", 
            "Grade" : 77.5,
            "Lettergrade" : "",
            "Instructor" : "Ning Rui"
            } , 
            { "CourseNumber" : "DATS 6202", 
            "CourseTitle" : "Machine Learning I", 
            "Year" : 2022,
            "Semester" : "Fall", 
            "Grade" : 91,
            "Lettergrade" : "",
            "Instructor" : "Yuxiao Huang"                              
            } , 
            { "CourseNumber" : "DATS 6001", 
            "CourseTitle" : "Algorithm Design", 
            "Year" : 2022,
            "Semester" : "Fall", 
            "Grade" : 93,
            "Lettergrade" : "",
            "Instructor" : "Yuxiao Huang"                              
            } , 
            { "CourseNumber" : "DATS 6401", 
            "CourseTitle" : "Visualization of Complex Data", 
            "Year" : 2022,
            "Semester" : "Fall", 
            "Grade" : 67.1,
            "Lettergrade" : "",
            "Instructor" : "Anya Mendenhall"                              
            } , 
            { "CourseNumber" : "DATS 6203", 
            "CourseTitle" : "Machine Learning II", 
            "Year" : 2022,
            "Semester" : "Spring", 
            "Grade" : 84.5,
            "Lettergrade" : "",
            "Instructor" : "Amir Jafari"
            } , 
            { "CourseNumber" : "DATS 6203", 
            "CourseTitle" : "Cloud Computing", 
            "Year" : 2022,
            "Semester" : "Spring", 
            "Grade" : 92.5,
            "Lettergrade" : "",
            "Instructor" : "Walcelio Melo"
            } , 
            { "CourseNumber" : "DATS 6450", 
            "CourseTitle" : "Ethics for Data Science",  
            "Year" : 2022,
            "Semester" : "Spring", 
            "Grade" : 94,
            "Lettergrade" : "",
            "Instructor" : "Simson Garfinkel"
            } , 
            { "CourseNumber" : "DATS 6501", 
            "CourseTitle" : "Data Science Capstone",  
            "Year" : 2023,
            "Semester" : "Fall", 
            "Grade" : 92,
            "Lettergrade" : "",
            "Instructor" : "Edwin Lo"
            }
          ] 


#%%
# Use this very standard and common syntax, write a for-loop to list out the grades for each course.
# Notice the use of plural and singular forms of words to make is highly readable.
# The start of the for-loop is given here. Do not change the syntax and the notation



for course in courses :
  # print something 
  print(f"{course['CourseNumber']} {course['CourseTitle']} ({course['Year']} {course['Semester']})- Grade: {course['Grade']}")
        

# Make your printout exactly like this (without the comment sign)
# 
# DATS 6101 Introduction to Data Science (2021 Spring) - Grade: 85.5
# DATS 6102 Data Warehousing (2021 Spring) - Grade: 95.5
# DATS 6103 Introduction to Data Mining (2021 Spring) - Grade: 77.5
# DATS 6202 Machine Learning I (2022 Fall) - Grade: 91
# DATS 6001 Algorithm Design (2022 Fall) - Grade: 93
# DATS 6401 Visualization of Complex Data (2022 Fall) - Grade: 67.1
# DATS 6203 Machine Learning II (2022 Spring) - Grade: 84.5
# DATS 6203 Cloud Computing (2022 Spring) - Grade: 92.5
# DATS 6450 Ethics for Data Science (2022 Spring) - Grade: 94
# DATS 6501 Data Science Capstone (2023 Fall) - Grade: 92

#%%
# Question 2: Now combining with conditional statements inside the for-loop (Do not create a new function to do this yet), 
# create printout look this this:
# 
# DATS 6101 Introduction to Data Science (2021 Spring) - Letter Grade: B
# DATS 6102 Data Warehousing (2021 Spring) - Letter Grade: A
# DATS 6103 Introduction to Data Mining (2021 Spring) - Letter Grade: C+
# DATS 6202 Machine Learning I (2022 Fall) - Letter Grade: A-
# DATS 6001 Algorithm Design (2022 Fall) - Letter Grade: A
# DATS 6401 Visualization of Complex Data (2022 Fall) - Letter Grade: D+
# DATS 6203 Machine Learning II (2022 Spring) - Letter Grade: B
# DATS 6203 Cloud Computing (2022 Spring) - Letter Grade: A-
# DATS 6450 Ethics for Data Science (2022 Spring) - Letter Grade: A
# DATS 6501 Data Science Capstone (2023 Fall) - Letter Grade: A-
#
# Start off the for-loop the same as before.

for course in courses:
    grade = course['Grade']
    if grade >= 93: 
        grade_string = f"- Grade: A"
    elif grade >= 90:
        grade_string = f"- Grade: A-"
    elif grade >= 87:
        grade_string = f"- Grade: B+"
    elif grade >= 83:
        grade_string = f"- Grade: B"
    elif grade >= 80:
        grade_string = f"- Grade: B-"
    elif grade >= 77:
        grade_string = f"- Grade: C+"
    elif grade >= 73:
        grade_string = f"- Grade: C"
    elif grade >= 70:
        grade_string = f"- Grade: C-"
    elif grade >= 67:
        grade_string = f"- Grade: D+"
    elif grade >= 60:
        grade_string = f"- Grade: D"
    elif grade < 60: 
        grade_string = f"- Grade: F"
    
    
    print(f"{course['CourseNumber']} {course['CourseTitle']} ({course['Year']} {course['Semester']}) {grade_string}")


#%%
# Question 3: Let us make the list easier to read by adding item numbers like this.
# 1: DATS 6101 Introduction to Data Science (2021 Spring) - Letter Grade: B
# 2: DATS 6102 Data Warehousing (2021 Spring) - Letter Grade: A
# 3: DATS 6103 Introduction to Data Mining (2021 Spring) - Letter Grade: C+
# 4: DATS 6202 Machine Learning I (2022 Fall) - Letter Grade: A-
# 5: DATS 6001 Algorithm Design (2022 Fall) - Letter Grade: A
# 6: DATS 6401 Visualization of Complex Data (2022 Fall) - Letter Grade: D+
# 7: DATS 6203 Machine Learning II (2022 Spring) - Letter Grade: B
# 8: DATS 6203 Cloud Computing (2022 Spring) - Letter Grade: A-
# 9: DATS 6450 Ethics for Data Science (2022 Spring) - Letter Grade: A
# 10: DATS 6501 Data Science Capstone (2023 Fall) - Letter Grade: A-
# 
# 
# You can start the for-loop anyway you like here. 

count = 0
for course in courses:
    grade = course['Grade']
    if grade >= 93: 
        grade_string = f"- Grade: A"
    elif grade >= 90:
        grade_string = f"- Grade: A-"
    elif grade >= 87:
        grade_string = f"- Grade: B+"
    elif grade >= 83:
        grade_string = f"- Grade: B"
    elif grade >= 80:
        grade_string = f"- Grade: B-"
    elif grade >= 77:
        grade_string = f"- Grade: C+"
    elif grade >= 73:
        grade_string = f"- Grade: C"
    elif grade >= 70:
        grade_string = f"- Grade: C-"
    elif grade >= 67:
        grade_string = f"- Grade: D+"
    elif grade >= 60:
        grade_string = f"- Grade: D"
    elif grade < 60: 
        grade_string = f"- Grade: F"
    
    count += 1
    
    
    print(f"{count}: {course['CourseNumber']} {course['CourseTitle']} ({course['Year']} {course['Semester']}) {grade_string}")



#%%
# Question 4: using the given tuple,  
# print out the list of days (31) in Jan 2023 like this
# Wed - 2023/1/1
# Thu - 2023/1/2
# Fri - 2023/1/3
# Sat - 2023/1/4
# Sun - 2023/1/5
# Mon - 2023/1/6
# Tue - 2023/1/7
# Wed - 2023/1/8
# Thu - 2023/1/9
# Fri - 2023/1/10
# Sat - 2023/1/11
# Sun - 2023/1/12
# Mon - 2023/1/13
# ...
# You might find something like this useful, especially if you use the remainder property x%7
# dayofweektuple = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat') # day-of-week-tuple

date = 0
dayofweektuple = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat')
for day in range(3, 34):
    date += 1
    print(f"{dayofweektuple[day % len(dayofweektuple)]} - 2023/1/{date}")
    
    

    
    
    


#%%
# Question 5:
# =================================================================
# Write python codes that converts seconds, say 257364 seconds,  to 
# (x Hour, x min, x seconds)
# ----------------------------------------------------------------

x=257364

#an hour has 60 mins; a min has 60 seconds; in an hour there are 3.6k seconds 
#lets make it fill out a min by seconds; then an hour by mins 


sec = x % 60
min = x//60
min2 = min % 60
hour = min//60 

print(f"{hour} Hour, {min2} mins, {sec} seconds")




# =================================================================
