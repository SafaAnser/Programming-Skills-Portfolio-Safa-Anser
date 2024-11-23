#creating variable password
password=12345

#number of maximum attempts
max_attempts=5

#creating variable for attempts
attempts=0

#using while loop 
while attempts<max_attempts:
    #asking user for password
    user=int(input('what is the password'.strip()))

    #if password is correct 
    if user==password:
        print('Your access is granted')

        #break point
        break

    #if password is wrong
    else:
        print('wrong password, try again')

        #adding up the attempts done
        attempts+=1

        #creating variable to show remaining attempts
        remaining_attempts= max_attempts - attempts
        print('your remaining attempts are',remaining_attempts)

#if the user has reached the attempts
if attempts==max_attempts:
    print('THE NUMBER OF ATTEMPTS HAS REACHED, THE AUTHORITIES HAVE BEEN ALERTED!!')