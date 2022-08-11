#****************************************
#Purpose:   This program uses boolean expressions to make tax calculations. Once the employee and company name is entered, this program displays the tax calculations based on whether the number of hours worked are below or above 40. Then it either calculates regular or overtime pay and the rest of the computations based on the pay.  
#           
#
#
#Input:     Employee name and company name
#
#Output:    Display the results of the calculated regular and overtime pay and the state and federal tax rate, FICA rate, state and federal tax, FICA tax, total deduction, and net pay associated with them. 
#               
#Course:    CS 1010 B
#
#Author:    Rekalyn Ware
#
#Date:      9/14/20
#
#****************************************

#define computePay
def computePay (hours, hourlyRate):
    
    if (hours <= 40):
         regularPay = hours * hourlyRate
         overtimePay = 0
       
    else:
         regularPay = 40 * hourlyRate
         overtimePay = (hours - 40) * hourlyRate * 1.5

    grossPay = regularPay + overtimePay
    
    return regularPay, overtimePay, grossPay 
#End of computePay

# Define computeTaxes.

def computeTaxes (grossPay, stateRate, federalRate, FICA_rate):
    
    stateTax = grossPay * stateRate
    
    federalTax = grossPay * federalRate
    
    FICA_tax = grossPay * FICA_rate
    
    totalDeduction = stateTax + federalTax + FICA_tax
    
    netPay = grossPay - totalDeduction
   
    return stateTax, federalTax, FICA_tax, totalDeduction, netPay
#End of computeTaxes


# Define printAll

def printAll (name, company, hours, hourlyRate,stateRate, \
              federalRate, FICA_rate, stateTax, federalTax,\
              FICA_tax, regularPay,overtimePay, grossPay,\
              totalDeduction, netPay):
    
    print ('Employee Name: ', name)
    print ('Company Name: ', company)
    print ('\n')
    print (format('Hours Worked: ','25s'),format(hours,'10d'))
    print (format('Hourly Rate: ','25s'),format(hourlyRate,'13.2f'))
    print ('\n')
    print (format('State Tax Rate: ','25s'), format(stateRate,'14.2%'))
    print (format('Federal Tax Rate: ','25s'), format(federalRate,'14.2%'))
    print (format('FICA Rate: ', '25s'), format(FICA_rate,'14.2%'))
    print ('\n')
    print (format('Regular Pay: ','25s'),format(regularPay,'13.2f'))
    print (format('Overtime Pay: ','25s'),format(overtimePay,'13.2f'))
    print (format('Gross Pay: ','25s'),format(grossPay,'13.2f'))
    print ('\n')
    print (format('State Tax: ','25s'),format(stateTax,'13.2f'))
    print (format('Federal Tax: ','25s'),format(federalTax,'13.2f'))
    print (format('FICA Tax: ','25s'),format(FICA_tax,'13.2f'))
    print ('\n')
    print (format('Total Deduction: ','25s'),format(totalDeduction,'13.2f'))
    print ('\n')
    print (format('Net Pay: ','25s'),format(netPay,'13.2f'))
    print ('\n')
    
    
#End of printAll

#10.    Declare and initialize variables
name = "Rekalyn Ware"
company = "RW Inc."
hours = 40
hourlyRate = 10.0
stateRate = 0.06
federalRate = 0.15
FICA_rate = 0.085

#11.    Invoke computePay function
regularPay, overtimePay, grossPay = computePay (hours,hourlyRate)

#12.    Invoke computeTaxes function
stateTax, federalTax, FICA_tax, totalDeduction, netPay = \
    computeTaxes (grossPay, stateRate, federalRate, FICA_rate)

#13.    Invoke printAll function
printAll (name, company, hours, hourlyRate,stateRate, \
              federalRate, FICA_rate, stateTax, federalTax,\
              FICA_tax, regularPay,overtimePay, grossPay,\
              totalDeduction, netPay)

#14.    Assign another set of hours and hourly rate
hours = 50
hourlyRate = 20.0

#15.    Invoke computePay function
regularPay, overtimePay, grossPay = computePay (hours,hourlyRate)

#16.    Invoke computeTaxes function
stateTax, federalTax, FICA_tax, totalDeduction, netPay = \
    computeTaxes (grossPay, stateRate, federalRate, FICA_rate)

#17.    Invoke printAll function
printAll (name, company, hours, hourlyRate,stateRate, \
              federalRate, FICA_rate, stateTax, federalTax,\
              FICA_tax, regularPay,overtimePay, grossPay,\
              totalDeduction, netPay)


