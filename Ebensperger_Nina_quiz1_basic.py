#%%
import q1data as q1
courses  = q1.courselist
# 
# From above, you now have a list object named "courses " 



#%%
# Q1 (2 points). How many items are there in courses? (Write python codes to find the answer.)

print(len(courses))


#%%
# Q2 (3 points). Print out the first and the 50-th class in the list.
#from operator import itemgetter 
#print(*itemgetter(0, 49)(courses))

[courses[x] for x in [0,50]]


#%%
# Q3 (3 points). Write a line of python code to obtain the estimated time (in hours) required to complete the 82-th course.
# 

print(courses[82]['time'])


#%%
# I created a copy of the list 
mylist = courses.copy()
# Q4 (2 points). Is this a true copy of courses? Write some python codes to substantiate your answer.

#The copy() method returns a shallow copy of the list.



mylist.append(['new sublist'])
print(mylist)
print(courses)

#This shows that we only created a shallow copy of the original list, mylist still contains references to the original child objects stored in courses.

courses[1][0] = 'X'

#when you modify one of the child objects in courses, this modification will be reflected in mylist as well

#%%