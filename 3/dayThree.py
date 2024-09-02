# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? \n"))
# bill = 0

# if height >= 120:
#     print("You can ride on the rollercoaster.")
#     age = int(input("How old are you ? \n"))
#     if age <= 12:
#         bill = 5
#         print("Please pay $5.")
#     elif age <= 18:
#         bill = 7
#         print("please pay $7.")
#     elif age >= 45:
#         bill = 0     
#         print("You don't need to pay, thank so much!")   
#     else:
#         bill = 12
#         print("please pay $12.")
    
#     wants_photo = input("Do you want to have a photo taken? Type y for Yes and n for No. \n")
#     if wants_photo == "y":
#         bill += 3
    
#     print(f"Your final bill is {bill}")

# else:
#     print("Sorry you have to grow taller before you can ride")  



# weight = 85
# height = 1.85
 
# bmi = weight / (height ** 2)
 
# if bmi >= 25:
#     print("overweight")
# elif bmi >= 18.5:
#     print("normal weight")
# else:
#     print("underweight")  




# weight = 84
# height = 1.80
# bmi = weight / (height ** 2)
# print(bmi)

# if bmi <= 18.5:
#     print("underweight")
# elif 18.5 < bmi <= 24.9:
#     print("normal weight")
# elif 25 <= bmi <= 29.9:
#     print("overweight")
# elif bmi >= 30:
#     print("obesity")
# else:
#     print("consult a specialist")



# print("Welcome to Python Pizza Deliveries!")

# size = input("What size pizza do you want? S, M or L: \n").strip().upper()
# size_price = 0

# if size == "S":
#   size_price += 15
#   pepperoni_price = 2
# elif size == "M":
#   size_price += 20
#   pepperoni_price = 3
# elif size == "L":
#   size_price += 25
#   pepperoni_price = 3
# else:
#     print("Invalid size choice.")
#     exit()

# pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n").strip().upper()
# if pepperoni == "Y":
#     size_price += pepperoni_price

# extra_cheese = input("Do you want extra cheese? Y or N: \n").strip().upper()
# if extra_cheese == "Y":
#    size_price += 1

# print(f"Your final bill is {size_price}")       



# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: \n").strip().upper()
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: \n").strip().upper()
# extra_cheese = input("Do you want extra cheese? Y or N: \n").strip().upper()
# size_price = 0

# if size == "S":
#   size_price += 15
# elif size == "M":
#   size_price += 20
# elif size == "L":
#   size_price += 25
# else:
#     print("Invalid size choice.")
#     exit()

# if pepperoni == "Y":
#     if size == "S":
#        size_price += 2
#     else:
#        size_price += 3   

# if extra_cheese == "Y":
#    size_price += 1

# print(f"Your final bill is: ${size_price}.")  



print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You're at a crossroad, where do you want to go? Type 'left' or 'right'. \n").upper().lower()
if choice1 == "left":
    print("You've come to a lake, there is an island in thew middle of the lake. Keep going you is winning!")
else:
    print("Game Over, you made the wrong choice!!!")
    exit()
    
choice2 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").upper().lower()
if choice2 == "wait":
    print("you arrive at the island unharmed. There is house with 3 doors. One red, one blue and one yellow.")
else:
    print("Game over, the shark ate you! HAHAHAHA ") 
    exit()   

choice3 = input("Which door do you choose ? 'red', 'blue' or 'yellow'? \n").upper().lower()
if choice3 == "red":
    print(''' 
          
          You Found the treasure. You win!!!
          


*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
          

          
          Thank so Much my Pirate!!!

''')
elif choice3 == "blue":
    print("You came close but not this time, See you later!!!")
    exit() 
else:
    print("You enter a room of beasts. Game Over.")
    exit()    
