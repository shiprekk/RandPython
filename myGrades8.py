#****************************************************
#Purpose:   A driver that invokes functions in module8
#           to read, compute grades, and prints students records
#
#
#****************************************************
import module8
def main(textFile):
    #Process first course that is stored in data8a.txt
    #   1.  invoke readRecords to process textfile data8a.txt
    names, scores = module8.readRecords(textFile)
    print(names)
    print(scores)
    
    #   2.  compute grades
    grades = module8.computeGrades(scores)
    #module8.displayGrades(grades)
    print(grades)
    #   3.  display students names, scores, and grades
    module8.displayNamesScoresGrades(names,scores,grades, 'CS 1010')
    print(names)
    print(scores)
    print(grades)
    print(course)

    #   4.  Display student name, score, and grade with highest score
    module8.highestStudent(names,scores,grades)
    print(names)
    print(scores)
    print(grades)
    #   5.  Display student name, score, and grade with lowest score
    module8.lowestStudent(names,scores,grades)
    print(names)
    print(scores)
    print(grades)
    #   6.  Display course stats: text average, highest score, lowest score,
    #       number of students in class, and the number of scores
    #       above the test average
    module8.courseStats(scores)
    print(scores)
#End of main
main("data8a.txt")  #Process first data file
main("data8b.txt")  #Process second data file
    

    
