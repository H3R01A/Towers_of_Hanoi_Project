from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
#Exercise 2
stacks = []

#Exercise 3
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

#Exercise 4
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
#Exercise 5
num_disks = int(input("\nHow many disks do you want to play with?\n"))

#Exercise 7
while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))

#Exercise 9
for i in range(num_disks,0,-1):
  #Exercise 10
  left_stack.push(i)

#Exercise 11
num_optimal_moves = (2**num_disks) - 1
print("\nThe fastest you can solve this game is in {} moves".format(num_optimal_moves))

#Get User Input
#Exercise 13
def get_input():
  #Exercise 14
  # i.get_name() gets the name of the stack.
  # Then i.get_name()[0] provides the FIRST LETTER of the name. So "L" for Left
  choices = [ i.get_name()[0] for i in stacks]
  #Exercise 15
  while True:
    #Exercise 16
    for i in range(len(stacks)):
      #Exercise 17
      name = stacks[i].get_name()
      letter = choices[i]
      #Exercise 18
      print("Enter {0} for {1}".format(letter,name))
     #Exercise 19
    user_input = input(" ")
      #Exercise 21
    if user_input in choices:
      for i in range(len(stacks)):
        #Exercise 22
        if user_input == choices[i]:
          return stacks[i]
        
#Play the Game
#Exercise 24
num_user_moves = 0
#Exercise 25
while(right_stack.get_size() != num_disks):
  #Exercise 26
  print("\n\n\n...Current Stacks...")
 
  for i in range(len(stacks)):
    stacks[i].print_items()
		#Code below was used to check and make sure game was working....
    #print("current size of right_stack is "+str(right_stack.get_size()))
    #print("current number of disks is "+str(num_disks))
    #print("current number of player moves is "+str(num_user_moves))
		
		#THE problem was that the "second" while loop was WITHIN the "for"
		#Once you moved it out, game works just fine!

    #Exercise 27
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    #Exercise 29
    if from_stack.is_empty() == True:
      print("\n\nInvalid Move. Try Again")
    #Exercise 30
    elif (to_stack.is_empty() == True) or (from_stack.peek() < to_stack.peek()) == True:
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break

    #Exercise 31
    else:
      print("\n\nInvalid Move. Try Again")

print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves,num_optimal_moves))