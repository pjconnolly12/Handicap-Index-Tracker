#Golf Handicap Index
# Note- Only Works for 18 hole entries

import math
import statistics
    
def differential(score,course_rating,slope_rating):
    diff = (score - course_rating) * 113 / slope_rating
    return math.floor(diff*100)/100

def data_gather():
    score = int(input("Enter your score: "))
    course = float(input("Enter the course rating: "))
    slope = int(input("Enter the slope rating: "))
    return differential(score,course,slope)

with open("handicap.txt", "a+") as hc:
    hc.write("[],"
             .format(data_gather()))

scores = []

with open("handicap.txt", "r") as hc:
    scores.append(hc.read())

sorted(scores)
print(scores)
"""
if len(scores) < 10:
    index = scores[0] * .96
    print(index)
else:
    if len(scores) < 19:
        x = scores[:5] 
        index = statistics.mean(x) * .96
        print(index)
    else:
        x = scores[:10]
        index = statistics.mean(x) * .96
        print(index)
"""
