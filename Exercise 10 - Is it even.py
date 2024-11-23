#defining a function 
def even_or_odd(number):

    #if the remainder of that number divided by 2 is 0 then it is even
    if number % 2 ==0:
        return(f'the number {number} is even')
    
    #if number is odd because the remainder wont be 0
    else:
        return(f'the number {number} is odd')

#defining a function
def main():

    #asking user input 
    number=int(input('enter the number: '))

    #new variable assigned to the function
    output=even_or_odd(number)

    #printing the variable 
    print(output)

#making it run only if it is directly scripted and not imported 
if __name__=='__main__':
    main()