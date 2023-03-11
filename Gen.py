import random
import string
import pyfiglet 
import time
from discord import SyncWebhook, File
import os

webhook = SyncWebhook.from_url("Webhook_url_here")


randomLetters = string.ascii_letters + string.digits + string.punctuation



def generate():
    # do work
    return generate_answer()


def generate_answer():
    while True:
        result = pyfiglet.figlet_format("SL33PY", font = "banner3-D" )
        print(result)
        print('*********************************Coded by SL33PY*********************************************')
        print('*                   Type "mail" to Generate emails                                          *')
        print('*                   Type "passwords" to Generate Passwords                                  *')
        print('*                   Type "pin" to generate a 6 digit pin                                    * ')
        print('*                   Type "Phook" to send the password.txt to your webhook                   *')
        print('*                   Type "Ehook" to send the email.txt to your webhook                      *')
        print('*                   Type "n" to exit the program                                            *')
        print('*********************************Coded by SL33PY*********************************************')
        answer = input("What woukd you like to use?: ")
        if answer not in {"y","n","pin","passwords","mail","Ehook","Phook"}:
            print("please enter valid input")
        elif answer == "passwords":
            while True:
                number = int(
                    input("Enter the amount of password you want to generate: "))
                length = int(input("Enter the length of the password: "))
                break
            for c in range(number):
                password = " "
                for x in range(length):
                    password += random.choice(randomLetters)
                print(password, file=open("password.txt", "a"))
                print("Generating....")
                time.sleep(1)
                print("Saved in passwords.txt")               
        elif answer == 'mail':
            def email_gen():
                chars_after_at = int(input("How many character mail do you want before @gmail.com between 4 and 100: "))
                emails = int(input('How many Emails shall i create?: \n'))
                add = input("Enter the domain name: for example @gmail.com \n")
                if(chars_after_at <4 or chars_after_at >100):
                    print("Please use characters between 4 and 100 ")
                else:
                    for i in range(emails):
            
                        letters_list =[string.digits,string.ascii_lowercase , string.ascii_uppercase]

                        letters_list_to_str = "".join(letters_list)


                        email_generated = "".join(random.choices(letters_list_to_str ,k=chars_after_at)) + add
                
                        print(email_generated, file=open("email.txt", "a"))
                        print('Generating.......')
                        time.sleep(2)
                        print('Email Stored in email.txt :)')
#call the email generator function
            email_gen()                   
        elif answer == 'Phook':
            print("Add your webhook url and make sure the password.txt file is in the same directory")
            webhook.send("The Passwords You Generated",file=File('password.txt'))
        elif answer == 'Ehook':
            print("Add your webhook url and make sure the email.txt file is in the same directory")
            webhook.send("The Emails You Generated",file=File('email.txt'))
        elif answer == "pin":
            random_id = ' '.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
            print(random_id)
            return generate()                      
        elif answer == "n":
            return "Thank you, bye!"
        elif answer == "y":
            # call function to start the calc answer
            return generate()
generate()