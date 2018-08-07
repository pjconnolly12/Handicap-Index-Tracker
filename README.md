# Handicap-Index-Tracker
Creating a program where I can enter my golf score as well as some course data required to calculate a golf handicap. It will keep track of all prior scores to update my handicap index accordingly.

I know there are plenty of these out there but I am a beginner programmer and wanted a interesting project to work on. I will be uploading the new file as I continue to code it more. 

After Day 1 I am stuck with being able to append each new differential(score) as a separate item in the existing list. Instead they all get appended into the same string. I will continue working on a fix to get this up and running. 

*UPDATE* I was able to fix my solution from day 1 by using the pickle module. The program now works at a basic level and does the following:

Asks for user input for score from an 18 hole round
Asks for the course rating
Asks for the slope rating
Uses this info to calculate the differential, which is used for golf handicap indexing
Appends differential to existing list of differentials
Prints the list of all differentials
Prints your handicap index based on the amount of rounds played

Next steps are to make it so that once 20 rounds are reached it removes the first item in the list before printing the list or the handicap, as only the latest 20 rounds should be used in tracking. 
