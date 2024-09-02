# print("caio"[0])

# print(len("caio"[1]))

# print(123 + 123)
# # print("452456" + "45432")
# print(int("111") + int("456"))


# print(len("444454"))

# number1 = 1
# print(type("564654"))
# print(type(654654))
# print(type(1231321.132))
# print(type(bool(number1)))
# print(bool(number1))
# print(type(True))


# name_of_the_user = input("how many letters have your name? \n")
# length_of_name = len(name_of_the_user)
# print(type("The number of letters in your name is: "))
# print(type(length_of_name))
# print("The number of letters in your name is: " + str(length_of_name))

# print(7 - 3)
# print(5 * 2)
# print(8 / 2)
# print(8 // 2)
# print(8 ** 3)
# print(3 * 3 + 3 / 3 - 3) 
# print((3 * 3) + (3 / 3) - (3 + 3))
# print((3-3) * 3)
# print((3*3) - 3 / (3 + 3))


# height = 1.84
# weight = 90
# imc = weight / (height **2)
# print(imc)
# print(int(imc))
# print(round(imc))
# print(round(imc, 2))
# print(float(imc))

# score = 0
# score = 1
# print("Your score is: " + str(score))

# score = 8
# height = 1.84
# is_winning = True
# print(f"Your score is: {score}")
# print(f"Your score is: {score}, your height is {height}")
# print(f"Your score is: {score}, your height is {height}. You are winning is {is_winning}")

base_value = 100
print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill?\n"))
print(f"The value total is ${bill}")
tip = int(input("How much tip would you like to give? 10, 12 or 15 ?\n"))
print(f"The tip is {tip}%")
people = int(input("How many people to split the bill?\n"))
print(f"It's just {people} people to share")
# bill_with_tip = (round(bill * (1 + tip / 100)))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"The total with tip is {final_amount}, but when you split it with {people} each person must pay ${bill_per_person}")