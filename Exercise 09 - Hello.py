#defining a function called hello
def hello():

    #asking it to print hello whenever the function is called
    print('hello')

#main function used to call hello function
def main():
    hello()

#making it print 'hello' only if the program is being run directly
if __name__=='__main__':
    main()