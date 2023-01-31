#%%
## Run Markdown Cells

print("Hello World!")
#%%

# question 1: create a markdown cell with the following:
# Two paragraphs about yourself. In one of the paragraphs, give a hyperlink of a website you want us to see. Can be something you like. 

# As the operations associate at US Pharmacopeia for its USAID project, I have had the opportunity to hone several skills that will allow me to both contribute to and learn from this role. Due to the urgent nature of the work, I have become adept at optimizing workflow and efficiency, requiring extensive communication and presentation. I work with cross functional teams as well as the field teams across 10 different countries. Additionally, I secured project funding by developing presentations on project finance using PowerPoint to communicate with other teams as well as USAID. Since I was new to the operations field, I sought out learning opportunities and solicited feedback on my performance. Gaining knowledge quickly allowed me to take on the role as a trainer for new hires as well as become the point person for operations-related questions. 
# 
# As I worked with the data analytics division more, I realized I am most interested in data science as a field. While working fulltime and attending GW’s master’s program for Data science, I utilized R and Python to preform statistical analysis including logistic regression and random forests. In these classes, I created machine learning projects which allowed me to put in practice my coding skills. [This is something I find interesting!](https://www.kaggle.com/code/nkitgupta/advance-data-preprocessing)

#%%
# Question 2
# a list of all the class titles that you are planning to take in the data science program. 
# Have at least 6 classes, even if you are not a DS major
# Then print out the last entry in your list.

classes = ['Intro to Data Science', 'Data Mining', 'Data Wharehousing', 'Algorithm Design', 'Cloud Computing', 'Machine Learning I']
print(classes[-1])


#%%
# Question 3: After you completed question 2, you feel Intro to data mining is too stupid, so you are going 
# to replace it with Intro to Coal mining. Do that in python here.

classes[1] = 'intro to coal Mining'

print(classes)

#%%
# Question 4: Before you go see your acadmic advisor, you are 
# asked to create a python dictionary of the classes you plan to take, 
# with the course number as key. Please do that. Don't forget that your advisor 
# probably doesn't like coal. And that coal mining class doesn't even have a 
# course number.

myCourseList = {
    "66199" : "Intro to Data Mining",
    "65295" : "Algorithm Design for Data Science",
    "62893" : "Data Wharehousing",
    "63513" : "Introduction to Data Science	",
    "63512" : "Machine Learning I: Algorithm Analysis",
    "64159" : "Cloud Computing	"
}
print(myCourseList)

x = myCourseList.get("66199")
print(x)


#%%
# Question 5: print out and show your advisor how many 
# classes (print out the number, not the list/dictionary) you plan 
# to take.


print(len(myCourseList))
    


#%%
# Question 6: Fast forward to the end of your degree here at GWU. YOu will no 
# longer take any more classes. Convert the list of Course Titles (list, not dicationary) 
# into a tuple, so no one will change it. 
# Print out the second half of the tuple. 

myTupleCourseTitles =   tuple(classes)
print(myTupleCourseTitles[3:])


# %%
# Question 7: Create an object (JSON) described below, which is just multiple layers of 
# python lists and dictionary: 
# A dictionary about youself, here at GW in data science, with the keys 
# "Firstname", "Lastname", "CompletedClasses", "InProgressClasses", "PlannedClasses", "ExpectedGraduationYear", 
# And for the record of each class, it should contains "CourseNumber", "CourseTitle", "Prerequsites".
# Note that each prerequsite class is a class itself, so it should have all these attributes as well. 
# For the InProgress and Completed classes, you should also include "Year", "Semester", "Instructor".
#
# ATTENTION: if you see a key/word in plural, that most likely means the value should be a list of similar 
# things. Otherwise, the value should be a single object.
#

myself = { "Firstname" : "Nina", 
          "Lastname" : "Ebensperger", 
          "CompletedClasses" : {
              "Intro to Data Science" : {
                  "CourseNumber" : 6101,
                  "CourseTitle" : "Intro to Data Science",
                  "Prerequsites" : "None",
                  "Year" : 2022,
                  "Semester" : "Fall",
                  "Instructor" : "Farhana Farque"
              },
              "Data Wharehousing" : {
                 "CourseNumber" : 6102,
                  "CourseTitle" : "Data Wharehousing",
                  "Prerequsites" : "None",
                  "Year" : 2022,
                  "Semester" : "Fall",
                  "Instructor" : "Abdi Awl"
              },
          },
          "InProgressClasses" : {
              "Intro to Data Mining" : {
                  "CourseNumber" : 6103,
                  "CourseTitle" : "Intro to Data Mining",
                  "Prerequsites" : "None",
                  "Year" : 2023,
                  "Semester" : "Spring",
                  "Instructor" : "Ning Rui"
              },
              "Algorithm Design" : {
                  "CourseNumber" : 6001,
                  "CourseTitle" : "Algorithm Design",
                  "Prerequsites" : "None",
                  "Year" : 2023,
                  "Semester" : "Spring",
                  "Instructor" : "Yuxiao Huang"
              },
              "Cloud Computing": {
                  "CourseNumber" : 6450,
                  "CourseTitle" : "Cloud Computing",
                  "Prerequsites" : "None",
                  "Year" : 2023,
                  "Semester" : "Spring",
                  "Instructor" : "Walcelio Melo"
              },
          },
          "PlannedClasses" : {
               "Summer" : "Machine Learning",
               "Fall" : "Data Visulaization"
              },
          "ExpectedGraduationYear" : 2024
}




# %%
# Question 8: Make a copy of your info for a friend. Make sure that when they change their info, 
# yours will not be affected.

copylist = myCourseList.copy()
print('copied list', copylist)





# %%
