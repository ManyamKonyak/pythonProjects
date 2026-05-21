import random
import string


letters_1 = list(string.ascii_lowercase)
letter_2 = list(string.ascii_uppercase)
digits = list(string.digits)
symbols = list(string.punctuation)

while True:
    try:
        user_input = int(input("How long do you want your password to be?:"))
    
        if(user_input < 8):
            print("Password length is lesser than 8. Try again!")
        else:
            break
    except ValueError:
        print("Please enter numbers only")
        
random.shuffle(letters_1)
random.shuffle(letter_2)
random.shuffle(digits)
random.shuffle(symbols)

letters_count = round(user_input * 0.3)
digits_and_symbols_count = round(user_input * 0.2)

password = []

for i in range(letters_count):
    password.append(letters_1[i])
    password.append(letter_2[i])
    
for i in range(digits_and_symbols_count):
    password.append(digits[i])
    password.append(symbols[i])
    
random.shuffle(password)

print("Password:" + "".join(password))
    
            
    


         
        
        

        