#Golf Handicap Index
# Note- Only Works for 18 hole entries

import math
import statistics
import pickle
   
#function to calculate differential    
def differential(score,course_rating,slope_rating):
    diff = (score - course_rating) * 113 / slope_rating
    return math.floor(diff*100)/100

#function to collect user input and return the differential
def data_gather():
    score = int(input("Enter your score: "))
    course = float(input("Enter the course rating: "))
    slope = int(input("Enter the slope rating: "))
    return differential(score,course,slope)

#Append the differential to the current list
mylist = []
with open('handicap.pkl', 'rb+') as hc:
    mylist = pickle.load(hc)
    mylist.append(data_gather())
    hc.seek(0)
    pickle.dump(mylist, hc, pickle.HIGHEST_PROTOCOL)

#Open the file to view the list
with open('handicap.pkl', 'rb') as hc:
    scores = pickle.load(hc)

#Sort the scores so lowest can be found and print the list
score_sort = sorted(scores)
print(score_sort)

#Print the handicap index based on amount of rounds played
if len(score_sort) < 10:
    index = score_sort[0] * .96
    print(math.floor(index*100)/100)
else:
    if len(score_sort) < 19:
        x = score_sort[:5] 
        index = statistics.mean(x) * .96
        print(index)
    else:
        x = score_sort[:10]
        index = statistics.mean(x) * .96
        print(index)
