#ef print_keyword_args(**kwargs):

#  print('\n')

 # for key, value in kwargs.items():
  #  print(f'{key} = {value}')

  #third = kwargs.get('third', None)
 # if third != None:
 #@   print('third arg =', third)


#print_keyword_args(first='a')
#print_keyword_args(first='b', second='c')
choice1 = input('select rock, paper or scissor:')
choice2 = input('select rock, paper or scissor:')
if choice1 == "rock" and choice2 == "scissor":
  print('win player 1')
elif choice1 == "scissor" and choice2 == "paper":
  print('win player 1')
elif choice1 == "paper" and choice2 == "rock":
  print('win player 1')
elif choice2 == "scissor" and choice1 == "paper":
  print('win player 1')
elif choice2 == "paper" and choice1 == "rock":
  print('win player 2')
elif choice2 == "rock" and choice1 == "scissor":
  print('win player 2')
  

