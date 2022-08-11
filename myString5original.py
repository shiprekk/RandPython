#***************************************************************
#Purpose:   This program converts and tests stings based on the function implemented by scaniing the strings defined and applying them to the written functions and displaying their results.
#
#Input:     Rekalyn Ware
#
#Output:    Display orginal string and length, string first characher, last character, middle character, string in swappedcase, lowercase, uppercase, string as title, string last word, first word, is string last word alphabet, s replaced with #?, location of right most s, and unicode value of first character. 
#
#Course:    CS 1010 B
#
#Author:    Rekalyn Ware
#
#Date:      9/23/20
#***************************************************************
def printHeader (name, course, date):
    
    print ('***********************************************','\nName: ', name)
    print ('Course: ', course)
    print ('Date: ', date,'\n\n***********************************************')
    
#End of function
    

def scan(s):
    print ('1. ',format ('Original String:','45s'),format(s,'>25s'))
    print ('2. ',format ('Original String Length:','45s'),format(len(s),'25d'))
    print ('3. ',format ('First Character: ','45s'),format(s[0],'>25s'))
    print ('4. ',format ('Last Character: ','45s'),format(s[-1],'>25s'))
    print ('5. ',format ('Middle Charachter: ','45s'),format(s[len(s)//2],'>25s'))
    print ('6. ',format ('Original string in swappedcase: ','45s'),format(s.swapcase(),'>25s'))
    print ('7. ',format ('Original string in lowercase: ','45s'),format(s.lower(),'>25s'))
    print ('8. ',format ('Original string in upppercase: ','45s'),format(s.upper(),'>25s'))
    print ('9. ',format ('Original string in title: ','45s'),format(s.title(),'>25s'))
    print ('10. ',format ('First word: ','45s'),s.startswith('Valdosta'))
    print ('11. ',format ('Last word: ','45s'),format(s.endswith('University'),'24d'))
    print ('12. ',format ('Is Last word alphabet? ','45s'),format(s.isalpha(),'24d'))
    print ('13. ',format ('''All 's' are replaced with '#?' ''','45s'),format(s.replace('s','#?'),'>25s'))
    print ('14. ',format ('Locate right most s in string ','45s'),format(s.rfind('s'),'24d'))
    print ('15. ',format ('Unicode value for 1st character ','45s'),format(ord(s[0]),'24d'))
#End of main
           
printHeader ('Rekalyn Ware', 'CS 1010', '9/21/2020')
scan ('Valdosta State University')
scan ('CS 1010 - Fall Semester, 20')
scan ('Math 1111A Spring Semester')
