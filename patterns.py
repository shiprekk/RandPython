#**********************************************************
#Purpose:   This program uses nested loop functions to create six different patterns displaying numbers one through six. The code information is then imported to Mypatterns6 so that the program can be ran and the patterns display when a number is entered.
#
#Input:     none
#
#Output:    The output includes the various number patterns resulting from the nested loops.
#
#Course:    CS 1010 B
#
#Author:    Rekalyn Ware
#
#Date:      9/29/20
#
#*********************************************************

#patternI displays the following pattern

##   1 
##   1 2 
##   1 2 3 
##   1 2 3 4 
##   1 2 3 4 5 
##   1 2 3 4 5 6
##
##
def pattern1(n):
    print("\n\tPattern I")
    for i in range (1,n+1, 1):
        print()
        for j in range (1, i+1, 1):
            print (j, end = ' ')
        #End of inner loop
    #End of outer loop
    print()
    
#End of patternI
#patternI displays the following pattern
    
#patternII
    
##   1 2 3 4 5 6 
##   1 2 3 4 5 
##   1 2 3 4 
##   1 2 3 
##   1 2 
##   1 
##
def pattern2(n):
    print("\n\tPattern II")
    for i in range (n,0,-1):
        print()
        for j in range (1, i+1, 1): 
            print (j, end = ' ')
        #End of inner loop
    #End of outer loop
    print()

#End of PatternII
    

##                            }

##   
##             6 
##           5 6 
##         4 5 6 
##       3 4 5 6 
##     2 3 4 5 6 
##   1 2 3 4 5 6 
##

def pattern3 (n):
    print ("\n\tPattern III")
    for i in range (n, 0, -1):
        print()
        for j in range (1,i):
            print(' ', end = ' ')
        for k in range (i,n+1):
            print (k, end = ' ')
        #End of inner loop
    #End of outer loop
    print()

#End of patternIII

#patternIV displays the following pattern
##   
##   1 2 3 4 5 6 
##     2 3 4 5 6 
##       3 4 5 6 
##         4 5 6 
##           5 6 
##             6 
##   
def pattern4(n):
    print ("\n\n\tPattern IV")
    for i in range (1,n+1):
        print()
        #first inner loop
        for j in range (1,i):
            print(' ', end = ' ')
        #end of first inner loop
        #second inner loop
        for k in range (i,n+1):
            print (k, end = ' ')
        #End of second inner loop
    #End of outer loop
    print()

#End of patternIV

#patternIV displays the following pattern
##   
##   1 2 3 4 5 6 5 4 3 2 1     
##     2 3 4 5 6 5 4 3 2              
##       3 4 5 6 5 4 3
##         4 5 6 5 4
##           5 6 5 
##             6
           
def pattern5(n):
    print ("\n\n\tPattern V")
    for i in range ():
        print()
        for j in range ():
            print()
        for k in range ():
            print ()
        #End of inner loop
    #End of outer loop
    print()
#End of patternV
            
#patternVI displays your own pattern
##   
##      
##             
##           
##         
##      
##     
##   
##   
##
            
def pattern6(n):
    print("\n\n\tMy Own Pattern")
    for i in range (n, 0, -1):
        print()
        for j in range (n, i-1,-1):
            print('  ', end = '  ')
        for k in range (n-1,0,-1):
            print (j, end = '  ')
        #End of inner loop
    #End of outer loop
    print()
#End of patternVI

