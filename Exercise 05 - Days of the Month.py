#creating dictionary of month number:month days
months={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

#askin user the month number
user=int(input('enter the month number: '))

if user>=1 and user<=12:

    #at the case if month=2
    if user==2:

        #asking user if its leap year or not
        leap_year=(input('is it a leap year?(yes/no): ').strip().lower())

        #printing the output accordingly

        if leap_year=='no':
           print('the month had 28 days') 
        elif leap_year=='yes':
           print('the month has 29 days')
    
    #if month not 2
    else:
          print('the months has', months[user], 'days')

#if month number given is other than 1-12
else:
      print('invalid month number') 