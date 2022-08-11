#****************************************
# Purpose:  Practice with functions and
#           Reading from console

# Input:    Reading data from console (keyboard)
# Output:   Display read values and computed results
#
# Course:   CS 1010
#
# Author:   Fares
#
# Date:     8/24/2020
#
# Program:  ReadingDataFromConsole
#*****************************************
# 1.    Define computeArea function that receices
#       radius, computes and returns circle area
#       Use area = radius * radius * 3.14159

def computeArea(radius):

    #1.1    write the equation to compute the area of the  circle
    area = radius * radius * 3.14159
    #1.2    Return the computed area
    
    return area
#End of computeArea

# 2.    Define displayValues function that receices
#       name, age, radius, and area.
#       The function prints the received values with label as shown:
#
#       Name:       <Your name>
#       Age:        <Your age>
#       Radius:     1.0
#       Area:       3.14159
#

#displayValues function
def displayValues(name, age, radius, area):
  
    #2.1    Write several print statements to display received values
    print ("\n\n")
    print ("Name:    ", name)
    print ("Age:     ", age)
    print ("Radius:  ", radius)
    print ("Area:    ", area)
    print ("\n\n")
#End of displayValues function
    
#3. Invoke functions
##3.1   Reading Input from the Console
##  a.  Use the input function 
##          variable = input("Enter a string: ")
##

##  b.  Use the float and int function to convert a string to a float or int.
##
##          var = float(stringVariable)
##
##          var = int(stringVariable)
#3.2 Prompt user to enter name
name = input ("Enter your name: ")

#3.3 Prompt user to enter age
myAge = int (input ("Enter your age: "))
#3.4 Prompt user to enter radius
r = float (input ("Enter Radius: "))
#3.5    invoke computeArea function by passing the radius.
#       the function should return a value to be assigned to  area
area = computeArea(r)
#3.6    Invoke displayValues function to display values. Pass name,
#       age, radius, and area
displayValues(name, myAge, r, area)


