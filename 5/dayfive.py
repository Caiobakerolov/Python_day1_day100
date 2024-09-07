# fruits = ["apple", "Peach", "Pear"]

# for fruit in fruits:
#     # print(fruit)
#     print(fruit + " pie")






# students_scores = [105, 150, 178, 123, 199, 162, 135, 141, 180, 110, 157, 175, 190, 145, 183, 129, 195, 168, 132, 140
# ]
# total_exam_score = sum(students_scores)
# print(total_exam_score )


# sum = 0
# for score in students_scores:
#     sum +=score
#     print(sum)

# max_score = 0
# for score in students_scores:
#     if score > max_score:
#         max_score = score
# print(max_score)



# average_score = sum(students_scores) / len(students_scores)
# print(average_score)




# total = 0
# for number in range(1, 101):
#     total += number
# print(total)


# for number in range(1, 16):    
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("fizz")
#     elif number % 5 == 0:
#         print ("buzz")
#     else:
#         print(number)   




# import random
# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.', '/', '?', '|', '\\', '"', "'"]
# letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# print("Welcome to the PyPassword Generator!!!")
# mean_numbers = int(input("How many numbers would you like ? \n"))
# mean_symbols = int(input("How many symbols would you like ? \n"))
# mean_letters = int(input("How many letters would you like ? \n"))

# easyPassword = ""

# for character_letters in range(0, mean_letters):
#     easyPassword += random.choice(letters)

# for character_symbols in range(0, mean_symbols):
#     easyPassword += random.choice(symbols)

# for character_numbers in range(0, mean_numbers):
#     easyPassword += random.choice(numbers)

# print(easyPassword)





import random
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.', '/', '?', '|', '\\', '"', "'"]
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print("Welcome to the PyPassword Generator!!!")
mean_numbers = int(input("How many numbers would you like ? \n"))
mean_symbols = int(input("How many symbols would you like ? \n"))
mean_letters = int(input("How many letters would you like ? \n"))

max_length = 16
total_characters = mean_numbers + mean_symbols + mean_letters

if total_characters > max_length:
    print(f"Error: The total number of characters exceeds the limit. {max_length}.")
else:
    password_list = []

    for character_letters in range(0, mean_letters):
        password_list.append(random.choice(letters))

    for character_symbols in range(0, mean_symbols):
        password_list.append(random.choice(symbols))

    for character_numbers in range(0, mean_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    password = "".join(password_list)
    print(f"Your password is: {password}")
   