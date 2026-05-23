import string 
import random 
password_lenght = 0
user_input_funktons= []

while password_lenght == 0:
 password_lenght = int (input("how long you want the password to be: "))
    
ask_uppercase = input ("Do you want Uppercase? (y/n): ")
if ask_uppercase == 'y': 
 user_input_funktons.append(string.ascii_uppercase )
      
ask_lowercase = input ("Do you want Lowercase? (y/n): ")
if ask_lowercase == 'y': 
        user_input_funktons.append(string.ascii_lowercase )

ask_Nummbers = input ("Do you want numbers? (y/n): ")
if ask_Nummbers == 'y': 
    user_input_funktons.append(string.digits)
     
ask_symbols = input ("Do you want symbols? (y/n): ")
if ask_symbols == 'y': 
    user_input_funktons.append (string.punctuation)

comnbine_pool = ''.join(user_input_funktons)
pick_random = (random.choices(comnbine_pool,k=password_lenght))
password = ''.join(pick_random)
print (password)
