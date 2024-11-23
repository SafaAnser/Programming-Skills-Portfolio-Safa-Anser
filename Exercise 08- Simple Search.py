#creating list of names
name=['jake','zac','Ian','ron','sam','dave']

#askin user for which name to search
user=(input('which name would you like to search for: '))

#if users input name is available in the list
if user in name:
    print('the name',user ,'is available' )

#if user input name is not available in the list
else:
    print('the name', user,'is not available')
                        