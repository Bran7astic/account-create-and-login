import time
import colorama
from colorama import Fore
colorama.init(autoreset=True)

# Making an Account
print("===Create Account===")

def validate_input(field_name): # Used to check if each field has at least 4 characters
  while True:
    field_input = input(f"{field_name}: ") # ask for input using field name
    if len(field_input) >= 2: 
      return field_input #if length is at least 2, return input
    else: 
      print(f"{field_name} must have at least 2 characters. ")
      print() #otherwise, repeat loop until true
      
first_name = validate_input("First name") #first name
print()
last_name = validate_input("Last name")#last name
print()
input_username = validate_input("Username") #username
print()
input_password = validate_input("Password") #password
input_password_repeat= validate_input("Reenter Password") #reenter password
print()
while input_password != input_password_repeat: #if passwords don't match, prompt user to retype
  print("Passwords do not match. ")
  print()
  input_password = validate_input("Password") #password
  input_password_repeat= validate_input("Reenter Password")
else: 
  print(f"{Fore.GREEN}Welcome, {first_name.capitalize()}! Thank you for creating an account! ") # welcome message

#Login
print()
print("===Login===")
for number in range(1):
    for number in range(5): # user has 5 tries to enter the correct credentials before waiting
      print()  
      username = input("Username: ")
      password = input("Password: ")
      if password == input_password and username == input_username:
          print("Welcome! You are now logged in")
          break
      elif username != input_username:
        print("No username was found. ")
        print()
      elif password != input_password:
        print("Your password was inccorect. Try again. ")
      else:
        print()
        print("Your username or password was incorrect. Try again")
      if number == 3: 
        print()
        print(f"{Fore.RED}You have one attempt remaining. ") 
    else: 
        print()
        print(f'{Fore.YELLOW}You have attempted too many times. Please try again in...')
        for seconds in range (3, 0, -1):
            print(seconds)
            time.sleep(1)
        username_final = input("Username: ")
        password_final = input("Password: ")
        if password_final == input_password and username_final == input_username: 
            print("Welcome! You are now logged in")
        else: 
            print(f"{Fore.RED}Too many failed attempts. Your account has been temporarily locked. ")