# import random

# random_integer = random.randint(1, 10)
# print(random_integer)


# random_number_0_to_1 = random.random() * 20
# print(random_number_0_to_1)


# random_float = random.uniform(1, 10)
# print(random_float)


# random_heads_or_tails = random.randint(0,1)
# if random_heads_or_tails == 0:
#     print("Heads")
# else: 
#     print("Tails")    

# states_of_australia = ["queensland", "sydney", "melbourne", "perth", "camberra"]
# states_of_australia[1] = "Cairns"
# states_of_australia.append("tasmania")

# print(states_of_australia)



# friends_random = ["jose", "carlos", "maria","arnaldo", "francisco", "cristiano"]
# print(random.choice(friends_random))


# random_index = random.randint(0, 4)
# print(friends_random[random_index])

# print(len(friends_random))
# num_of_friends = len(friends_random)
# print(friends_random[num_of_friends - 2])



# friends = ["jose", "carlos", "maria","arnaldo", "francisco", "cristiano"]
# fruits = ["banana", "apple", "kiwi", "pineapple", "orange", "strawberries"]
# vegetables = ["Spinach", "kale", "tomatoes", "celery", "potatoes"]

# mix = [fruits, vegetables]
# print(mix)


# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# print(fruits)


# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1])


# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# print(fruits[0])


import random

rock = '''


    ./   ._. \)
    |    / (_\_\)
    |_ '  (___)
    |     (__)
    |`----(_)


'''

paper = '''

        ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'       

'''

scissors = '''

 .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/

'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose ? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer chose: ")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number. You Lose!")
elif user_choice == 0 and computer_choice == 2:
  print("You wins!")
elif computer_choice == 0 and user_choice == 12:
  print("You lose!")
elif computer_choice > user_choice:
  print("You lose!")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("You tied!")  
