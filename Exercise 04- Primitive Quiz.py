#creating dictionary and assigning countries : capitals
area={'italy':'rome','france':'paris','russia':'moscow','germany':'berlin','portugal':'lisbon','spain':'madrid','united kingdom':'london','belgium':'brussels',
           'czechia':'prague','poland':'warsaw'}

#giving variables to keys and values in the dictionary
for country,capitals in area.items():

    #askin capitals to user
    answer= input(f'what is the capital of {country} ')

    #to ignore capitalization
    if answer.lower()==capitals.lower():
      
      #to print if correct answer
      print('Yay! you got it right')

      #to print if wrong answer
    else:
       print('Oops, wrong answer') 