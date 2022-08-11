#*******************************************
#Purpose: This program reads data from the console and uses it to compute the prices and costs of shares purchase and sales. It then displays the data entered and the computation results.
#
#Input:   Stock name, shares, commission rate, purchase date, purchase share price.
#
#Output:  Display results of the computation of share purchase price, share purchase cost, purchase commission, total purchase cost, share sale price, share sale cost, share sale commission, total sale cost, and gain and loss amount.
#
#Course:  CS 1010 B
#
#Author:  Rekalyn Ware
#
#Date:    9/2/20
#
#Program: MyInvestment3
#*******************************************

# getStockInformation
def getStockInformation ():
    
    stockName = input ('Enter stock name: ')
    shares = int (input ('Enter number of shares: ')) 
    commissionRate = float (input ('Enter commision rate: '))
    return stockName, shares, commissionRate

#End of getStockInformation

#transaction function
def transaction():
   
    transactionDate = input ('Enter transaction date: ')
    purchaseSharePrice = float (input ('Enter share price: '))
    return transactionDate, purchaseSharePrice 
#End of transaction function

# computeTransactionCommissionAndCost function.
def computeTransactionCommissionAndCost (shares, price, comm):

    purchaseSharesCost = shares * purchaseSharePrice
    
    purchaseCommission = commissionRate * purchaseSharesCost
    
    purchaseTotalCost = purchaseSharesCost + purchaseCommission

    
    return purchaseSharesCost, purchaseCommission, purchaseTotalCost
#End of computeTransactionCommissionAndCost

# printAll function.  
def printAll (shareName, shares, commissionRate, transactionDate, purchaseSharePrice,
          saleDate,saleSharePrice, purchaseSharesCost, purchaseCommission, purchaseTotalCost,
          saleSharesCost, saleCommission, saleTotalCost, totalCommission, netAmount):
    
    print ('Share Name:           ', stockName)
    print ('Number of Shares:     ', shares)
    print ('Commisson Rate:       ',commissionRate)
    print ('  ')
    print ('Purchase Date:        ', transactionDate)
    print ('Share Purchase Price: ', purchaseSharePrice)
    print ('Share Purchase Cost:  ', purchaseSharesCost)
    print ('Purchase Commission:  ', purchaseCommission)
    print ('Total Purchase Cost:  ', purchaseTotalCost)
    print ('   ')
    print ('Sale Date:            ', saleDate)
    print ('Share Sale Price:     ', saleSharePrice)
    print ('Shares Sale Cost:     ', saleSharesCost)
    print ('Sale Commission:      ', saleCommission)
    print ('Total Sale Cost:      ', saleTotalCost)
    print ('  ')
    print ('Gain/Loss Amount:     ', netAmount)
       
#End of printAll function

    
#5. Invoke getStckInformation function 
stockName, shares, commissionRate = getStockInformation ()

#6. Invoke transaction function to prompt user to enter
#   purchase information
print ("\n\nEnter Stock Purchase Date and Purchase Share Price\n")
transactionDate, purchaseSharePrice = transaction()

#7. Invoke transaction function to prompt user to enter
#   sale information
print ("\n\nEnter Stock Sale Date and Sale Share Price\n")
saleDate, saleSharePrice = transaction ()

#8. Invoke computeTransactionCommissionAndCost function to compute
#   purchase cost and details
purchaseSharesCost, purchaseCommission, purchaseTotalCost = computeTransactionCommissionAndCost (shares, purchaseSharePrice, commissionRate)

#9. Invoke computeTransactionCommissionAndCost function to compute
#   sale cost and details
saleSharesCost, saleCommission, saleTotalCost = computeTransactionCommissionAndCost (shares, saleSharePrice, commissionRate)

#10.    Compute total commission
totalCommission = purchaseCommission + saleCommission

#11.    Compute gain/loss amount
netAmount = saleTotalCost - purchaseTotalCost

#12.    Invoke printAll
printAll (stockName, shares, commissionRate, transactionDate, purchaseSharePrice,
          saleDate,saleSharePrice, purchaseSharesCost, purchaseCommission, purchaseTotalCost,
          saleSharesCost, saleCommission, saleTotalCost, totalCommission, netAmount)
