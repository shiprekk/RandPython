#***************************************************
#Purpose: This program reads data from the console and uses that data to compute circle area, rectangle area, sphere volume, and cylindervolume. It then displays those results and the entered data: name, radius, cylinderlength,width, and height. 
#
#Input:   Name, radius, cylinderlength, width, and height. 
#
#Output:  Display results for the computation of circle and rectangle area and sphere and cylinder volume.
#
#Course:  CS 1010 B
#
#Author:  Rekalyn Ware
#
#Date:    8/25/20
#
#Program: MyCalculations2
#****************************************************

#shapesDimensions function 
def shapesDimensions():
    
    name = input('Enter name here: ')
    radius = float ( input ('Enter radius here: '))
    cylinderlength = int (input ('Enter cylinder length here: '))
    width = int ( input ('Enter rectangle width here: '))
    height = int ( input ('Enter rectangle height here: '))
    return name, radius, cylinderlength, width, height  
#End of shapeDimensions

#circleArea function
def circleArea(radius):
    
    c_area = radius * radius * 3.14159
    return c_area
#end circleArea function

#rectangleArea function
def rectangleArea(width, height):

    r_area = width * height
    return r_area
#end of rectangleArea function

#sphereVolume function
def sphereVolume(radius):

    s_volume = 3.14159 * radius ** 2 * cylinderlength
    return s_volume
#end sphereVolume function

#cylinderVolume function
def cylinderVolume(radius, cylinderlength):

    c_volume = 3.14159 * radius ** 2 * cylinderlength
    return c_volume
#end cylinderVolume function



#printAll function
def printAll (name, radius, cylinderlength, width, height, c_area, r_area, s_volume, c_volume, cr_total_area, cr_total_volume):
   # YOU need to implement printAll with print statements here
    print ('Name:              ',name)
    print ('  ')
    print ('Radius:            ',radius)
    print ('  ')
    print ('Cylinder length:   ',cylinderlength)
    print ('Rectangle Width:   ',width)
    print ('Rectangle Height:  ',height)
    print ('  ')
    print ('Circle Area:       ',c_area)
    print ('Rectangle Area:    ',r_area)
    print ('  ')
    print ('Sphere Volume:     ',s_volume)
    print ('Cylinder Volume:   ',c_volume)
    print ('  ')
    print ('Totals:')
    print ('Total Areas:       ',cr_total_area)
    print ('Total Volumes:     ',cr_total_volume)       
#End printAll function  
           

#Invoke functions
    
#shapesDImensions function    
name, radius, cylinderlength, width, height = shapesDimensions()

#circleArea function
c_area = circleArea(radius) 

#rectangleArea function
r_area = rectangleArea(width, height)

#sphereVolume function
s_volume = sphereVolume(radius)

#cylinderVolume function
c_volume = cylinderVolume(radius, cylinderlength)

#totalArea function
cr_total_area = c_area + r_area

#totalVolume function           
cr_total_volume = s_volume + c_volume


#printall function
printAll (name, radius, cylinderlength, width, height, c_area, r_area, s_volume, c_volume, cr_total_area, cr_total_volume)
           
 
