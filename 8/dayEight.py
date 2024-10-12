# def greet(massage1, message2, message3):
#   print(massage1)
#   print(message2)
#   print(message3)

# greet("welcome", "good night", "congratulations")


# def greet():
#   print("welcome")
#   print("good night")
#   print("congratulations")

# greet()
# greet()

# def greet_with_name(name):
#   print(f"welcome {name}")
#   print(f"good night, how is it going {name}?")
#   print(f"congratulations {name}")

# greet_with_name("Caio")



# def life_in_weeks():
#     max_age = 90

#     age = int(input("How are your age ? \n"))
#     remain_life = (max_age - age) * 52
#     print(f"You only have {remain_life} weeks to try to be happy!")
    

# life_in_weeks()




# def greet_with_name_and_location(name, location):
#   print(f"Welcome {name}")
#   print(f"I search about your {location} and then it looks wonderful")

# greet_with_name_and_location("caio", "sao paulo")   




# def greet_with_name_and_location(*args):
#     name, location = args
#     print(f"Welcome {name}")
#     print(f"I search about your {location} and then it looks wonderful")

# greet_with_name_and_location("Caio", "São Paulo")



# def greet_with_name_and_location(**kwargs):
#     name = kwargs.get('name')
#     location = kwargs.get('location')
#     print(f"Welcome {name}")
#     print(f"I search about your {location} and then it looks wonderful")

# greet_with_name_and_location(name="Caio", location="São Paulo")




# def greet_with_number(a, b ,c):
#   print(f"hello {a}")
#   print(f"hello {b}")
#   print(f"hello {c}")

# a = "Caio"
# b = "Aline"
# c = "Ravi"  

# greet_with_number(a = b, b = c, c = a)




# def greet_with_number(a = 1, b = 2, c = 3):
#   print(f"I have {a}")
#   print(f"However I lost {b}")
#   print(f"So I have -1 but I won {c} and then I have 1")

# greet_with_number()




# def greet_with_number(passion, dreams):
#   print(f"I love {passion}")
#   print(f"So one day, {dreams}")

# greet_with_number(passion = "Ocean", dreams = "I'm going to live in front of the beach.")
# greet_with_number(dreams = "I'm going to live in front of the beach.", passion = "Ocean")




# def calculate_love_score(name1, name2):
#     combined_name = name1.lower() + name2.lower()

#     true_count = combined_name.count('t') + combined_name.count('r') + combined_name.count('u') + combined_name.count('e')
#     love_count = combined_name.count('l') + combined_name.count('o') + combined_name.count('v') + combined_name.count('e')

#     love_score = int(f"{true_count}{love_count}")

#     print(f"Your love score is: {love_score}")

# calculate_love_score("Caio Bakerolov", "Aline Bakerolov") 




# def calculate_love_score(name1, name2):
#   combined_name = name1.lower() + name2.lower()

#   true_count = combined_name.count('t') + combined_name.count('r') + combined_name.count('u') + combined_name.count('e')
#   love_count = combined_name.count('l') + combined_name.count('o') + combined_name.count('v') + combined_name.count('e')

#   love_score = int(f"{true_count}{love_count}")
  

#   print(f"Your love score is: {love_score}")

# calculate_love_score("Caio Bakerolov", "Aline Bakerolov")  




# def calculate_love_score(name1, name2):
#     combined_names = name1.lower() + name2.lower()

#     t = combined_names.count("t")
#     r = combined_names.count("r")
#     u = combined_names.count("u")
#     e_true = combined_names.count("e")
#     first_word = t + r + u + e_true

#     l = combined_names.count("l")
#     o = combined_names.count("o")
#     v = combined_names.count("v")
#     e_love = combined_names.count("e")
#     second_word = l + o + v + e_love

#     score = int(str(first_word) + str(second_word))
#     print(score)

# calculate_love_score("Caio Bakerolov", "Aline Bakerolov")





# def calculate_love_score(name1, name2):
#     combined_names = name1.lower() + name2.lower()

#     t = combined_names.count("t")
#     r = combined_names.count("r")
#     u = combined_names.count("u")
#     e_true = combined_names.count("e")
#     first_word = t + r + u + e_true

#     l = combined_names.count("l")
#     o = combined_names.count("o")
#     v = combined_names.count("v")
#     e_love = combined_names.count("e")
#     second_word = l + o + v + e_love

#     score = first_word + second_word
#     print(score)

# calculate_love_score("Caio Bakerolov", "Aline Bakerolov")



# # Parte 1: Criação do alfabeto
# # Cria uma lista com todas as letras do alfabeto em ordem
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# # Parte 2: Função de Criptografia
# # Função que criptografa a mensagem deslocando as letras
# def encrypt(text, shift):
#     encrypted_text = ""  # Inicializa uma string vazia para armazenar o texto criptografado
#     for letter in text:  # Percorre cada letra da mensagem fornecida
#         if letter in alphabet:  # Verifica se a letra está no alfabeto (ignora espaços e pontuação)
#             index = alphabet.index(letter)  # Encontra o índice da letra no alfabeto
#             new_index = (index + shift) % 26  # Calcula o novo índice com o deslocamento, usando % 26 para circular no alfabeto
#             encrypted_text += alphabet[new_index]  # Adiciona a letra criptografada à string de saída
#         else:
#             encrypted_text += letter  # Se não for uma letra (por exemplo, um espaço), mantém o caractere original
#     return encrypted_text  # Retorna o texto criptografado

# # Parte 3: Função de Descriptografia
# # Função que descriptografa a mensagem revertendo o deslocamento
# def decrypt(text, shift):
#     decrypted_text = ""  # Inicializa uma string vazia para armazenar o texto descriptografado
#     for letter in text:  # Percorre cada letra da mensagem fornecida
#         if letter in alphabet:  # Verifica se a letra está no alfabeto (ignora espaços e pontuação)
#             index = alphabet.index(letter)  # Encontra o índice da letra no alfabeto
#             new_index = (index - shift) % 26  # Calcula o novo índice subtraindo o deslocamento, usando % 26 para circular no alfabeto
#             decrypted_text += alphabet[new_index]  # Adiciona a letra descriptografada à string de saída
#         else:
#             decrypted_text += letter  # Se não for uma letra (por exemplo, um espaço), mantém o caractere original
#     return decrypted_text  # Retorna o texto descriptografado

# # Parte 4: Entrada do Usuário
# # Pede ao usuário para escolher entre criptografar (encode) ou descriptografar (decode)
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
# # Pede ao usuário para inserir a mensagem
# text = input("Type your message: \n").lower()
# # Pede ao usuário para inserir o número de deslocamento
# shift = int(input("Type the shift number: \n"))

# # Parte 5: Decisão e execução da criptografia/descriptografia
# # Verifica se o usuário escolheu "encode" para criptografar
# if direction == "encode":
#     result = encrypt(text, shift)  # Chama a função de criptografia
#     print(f"Encrypted message: {result}")  # Imprime a mensagem criptografada
# # Verifica se o usuário escolheu "decode" para descriptografar
# elif direction == "decode":
#     result = decrypt(text, shift)  # Chama a função de descriptografia
#     print(f"Decrypted message: {result}")  # Imprime a mensagem descriptografada
# # Se o usuário não escolher nem "encode" nem "decode", exibe um aviso de erro
# else:
#     print("Invalid input! Please type 'encode' or 'decode'.")




# # Criação da lista com as letras do alfabeto
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# # Cria uma chave secreta (número fixo) que você guarda em segurança e não revela ao público
# secret_key = 751  # A chave secreta adiciona um fator extra de segurança ao deslocamento (shift)

# # Função de criptografia usando a chave secreta
# def encrypt(text, shift):
#     encrypted_text = ""  # Inicializa uma string vazia para armazenar o texto criptografado
#     for letter in text:  # Para cada letra na mensagem fornecida
#         if letter in alphabet:  # Verifica se a letra está no alfabeto (para ignorar espaços e pontuação)
#             index = alphabet.index(letter)  # Encontra o índice da letra no alfabeto (posição da letra)
#             # Aplica o deslocamento com a soma do shift dado pelo usuário e a chave secreta
#             new_index = (index + shift + secret_key) % len(alphabet)  # % 26 garante que o índice fique no intervalo de 0 a 25
#             encrypted_text += alphabet[new_index]  # Adiciona a nova letra criptografada ao texto
#         else:
#             encrypted_text += letter  # Mantém a letra original se for um espaço ou caractere especial
#     return encrypted_text  # Retorna o texto criptografado

# # Função de descriptografia usando a chave secreta
# def decrypt(text, shift):
#     decrypted_text = ""  # Inicializa uma string vazia para armazenar o texto descriptografado
#     for letter in text:  # Para cada letra na mensagem fornecida
#         if letter in alphabet:  # Verifica se a letra está no alfabeto (para ignorar espaços e pontuação)
#             index = alphabet.index(letter)  # Encontra o índice da letra no alfabeto
#             # Subtrai o shift e a chave secreta para reverter o deslocamento aplicado
#             new_index = (index - shift - secret_key) % len(alphabet)  # % 26 mantém o índice dentro do intervalo 0-25
#             decrypted_text += alphabet[new_index]  # Adiciona a letra descriptografada ao texto
#         else:
#             decrypted_text += letter  # Mantém a letra original se for um espaço ou caractere especial
#     return decrypted_text  # Retorna o texto descriptografado

# # Inputs do usuário
# # O usuário escolhe se quer criptografar ou descriptografar a mensagem
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()

# # O usuário insere a mensagem que deseja criptografar ou descriptografar
# text = input("Type your message: \n").lower()

# # O usuário insere o número de deslocamento (shift) para alterar as letras
# shift = int(input("Type the shift number: \n"))

# # Verifica se o usuário escolheu criptografar ou descriptografar
# if direction == "encode":
#     result = encrypt(text, shift)  # Chama a função de criptografia com a mensagem e o shift fornecidos
#     print(f"Encrypted message: {result}")  # Exibe a mensagem criptografada
# elif direction == "decode":
#     result = decrypt(text, shift)  # Chama a função de descriptografia com a mensagem e o shift fornecidos
#     print(f"Decrypted message: {result}")  # Exibe a mensagem descriptografada
# else:
#     print("Invalid input! Please type 'encode' or 'decode'.")  # Caso a entrada do usuário seja inválida



# Criação da lista com as letras do alfabeto
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Cria uma chave secreta (número fixo) que você guarda em segurança e não revela ao público
secret_key = 751  # A chave secreta adiciona um fator extra de segurança ao deslocamento (shift)

# Função de criptografia usando a chave secreta
def caesar_cipher(text, shift, encode_or_decode):
    if encode_or_decode == "decode":
        shift = -shift  # Inverte o valor do shift para descriptografar
        secret_key_shift = -secret_key  # Inverte também a chave secreta para descriptografar
    else:
        secret_key_shift = secret_key  # Usa a chave secreta original para criptografar

    result_text = ""  # Inicializa uma string vazia para armazenar o resultado (criptografado/descriptografado)
    for letter in text:
        if letter in alphabet:  # Verifica se a letra está no alfabeto
            index = alphabet.index(letter)  # Encontra o índice da letra no alfabeto
            # Aplica o deslocamento (shift) junto com a chave secreta (criptografia ou descriptografia)
            new_index = (index + shift + secret_key_shift) % len(alphabet)
            result_text += alphabet[new_index]  # Adiciona a nova letra ao texto
        else:
            result_text += letter  # Mantém a letra original se for um espaço ou caractere especial
    return result_text  # Retorna o texto criptografado ou descriptografado

should_continue = True

while should_continue: 

    # Inputs do usuário
    # O usuário escolhe se quer criptografar ou descriptografar a mensagem
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()

    # O usuário insere a mensagem que deseja criptografar ou descriptografar
    text = input("Type your message: \n").lower()

    # O usuário insere o número de deslocamento (shift) para alterar as letras
    shift = int(input("Type the shift number: \n"))

    # Verifica se o usuário escolheu criptografar ou descriptografar
    if direction in ["encode", "decode"]:
        result = caesar_cipher(text, shift, direction)  # Chama a função unificada com a direção (encode ou decode)
        if direction == "encode":
            print(f"Encrypted message: {result}")  # Exibe a mensagem criptografada
        else:
            print(f"Decrypted message: {result}")  # Exibe a mensagem descriptografada
    else:
        print("Invalid input! Please type 'encode' or 'decode'.")  # Caso a entrada do usuário seja inválida

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")
    if restart == "no":
        should_continue = False
        print("GoodBye")    