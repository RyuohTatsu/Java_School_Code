# Python code
# This program will compute the weekly pay for a newspaper carrier.
# Developer: Brian Walters CMIS102/7384
# Date: March 22, 2023

print('Developer:\t Brian Walters')
print('Class:\t CMIS 102/7384\nDate:\t  3/23/2023')
print('Week 2 Assignment:\t Compute weekly pay for newspaper carrier.')


def main():
    
#Initialize variables (commRate = 0.05) , (npPrice=$4.25),  (daySal=$20)
    commRate = 0.05
    npPrice = 4.25
    daySal = 20
    
#Prompt the user for  (name)
    name =  (input('\nPlease enter your name: \t'))

#Display welcome message     
    print ('\nWelcome', name)
    
#Prompt the user for days worked
    dayWkd = int(input('\nNumber of days worked? \t'))
       
#Prompt the user for number newspapers delivered per day
    npDay = int (input('\nHow many newspapers delivered per day? \t'))
    
#Prompt the user for weekly tips
    totTip = int (input('\nWhat was your total tips for the week ' + str (name) + '? \t'))

#Calculate the weekly salary (days worked*daySal)
    wkSal = dayWkd * daySal
    
#Calculate the total newspapers sold (number of newspapers per day* daysWkd)
    totNp = npDay * dayWkd
    
#Calculate the total price of newspapers sold (total newspapers * npPrice)
    totErn = totNp * npPrice
    
#Calculate the commission (totErn of newspapers * commRate)
    totComm = totErn * commRate
    
#Calculate the total weekly pay (sum of weekly salary and commission)
    totPay = wkSal + totComm + totTip
    
#Display the results (totalDeliv and wkSal and totpay)
    print('Total newspapers Delivered:\t', totNp)
    print('Weekly salery earned:\t', wkSal)
    print('Total pay:\t', totPay)
    

# Execute -----------------------------
main()




