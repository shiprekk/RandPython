#******************************************************************
#Purpose:   Reading students records from a text file
#           Computing grades, Test average, Test Median, Text smallest, Test Largest
#           Number of scores above the average
#           Display students with highest score, student with the lowest score
#
#Input:     Reading names and scores from a text file. One name and a score per line
#
#Output:    Display output as shown on handout
#
#Course:    CS 1010
#
#Author:    Rekalyn Ware
#
#Date:      11/3/20
#
#******************************************************************
#   module8:    functions needed and invoked by the driver myGrades8
#
#   1.  Function receives name of a student records file.
#       It opens the input textfile and populates the names and scores
#       lists (arrays). At the end, function returns both lists to driver
#
def readRecords(filename):
    #Open the input text file
    infile = open (filename,'r')
    #Declare names and scores lists
    names = []
    for i in range
    
    scores = []
    for i in range
    

    #Reading student records
    for line in infile:
        #Scan line and split name and score
        tokens = line.split()  #tokens is a temporary list
        names.append(tokens[0])
        scores.append(int(tokens[1]))
    #End of for loop

    #Return names and scores
    return names, scores
#End of readRecords
#******************************************************************
#   
#   2.  computeGrades
#       Function receives scores, computes grades and saves them into grades list
#       at the end, it returns the grades list
def computeGrades(scores):
    print ("\n\tcomputeGrades to be implemented")
    grades = [scores]
    for i in range(
    return grades    #Update this statement
#End of computeGrades

#******************************************************************
#
#   3.  displayNamesScoresGrades
#       Function receives lists: names, scores, grades, and course name
#       It prints course information, table labels, and students records
#******************************************************************
def displayNamesScoresGrades(names, scores, grades, course):
    print ("\n\tdisplayNamesScoresGrades to be implemented")
    
#End displayNamesScoresGrades
    
#******************************************************************
#
#   4.  highestStudent
#       Function receives lists: names, scores, and grades.
#       it uses the scores list to find the location of students with the highest score
#       it uses that location to display name, score, and grade
#******************************************************************
def highestStudent(names, scores, grades):
    print ("\n\thighestStudent to be implemented")
    max(grades)
#End of highestStudent
        
#******************************************************************
#
#   5.  lowestStudent
#       Function receives lists: names, scores, and grades.
#       it uses the scores list to find the location of students with the lowest score
#       it uses that location to display name, score, and grade
#******************************************************************
def lowestStudent(names, scores, grades):
    print ("\n\tlowestStudent to be implemented")
    min(grades)
#End of lowestStudent
    
#******************************************************************
#
#   6.  courseStats
#       Function receives scores to compute:
#       average score, highestScore, lowestScore, number of students
#       in course, and number of students with scores above the test average score
#
#******************************************************************
def courseStats(scores):
    print ("\n\tcourseStats to be implemented")
    
#End of courseStats  
    
    
    
