import pygame
import random
import time

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("NASA Control Desk")
font = pygame.font.Font(None, 36)

# Global variables
user_choice = ""
username = ""
user_password = ""
planet = ""
outcome = ["yes", "no"]

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game loop flag
running = True

def display_text(text, x, y):
    text = font.render(text, True, WHITE)
    screen.blit(text, (x, y))

def main():
     print("""
Hello Welcome to the NASA control desk
WHAT WOULD YOU LIKE TO DO?
1. Launch.
2. View Successes.
3. Quit.
              """)
     user_choice = input("Enter Choice: ")
     if user_choice == "1":
         launch()
     elif user_choice == "2":
         success()
     elif user_choice == "3":
         print("Quitting.......")
         time.sleep(1)
         quit()
     else:
         print("Invalid input")
         main()
         
def login():
   
   global username, user_password
   username=  input("Enter your username: ")
   user_password = input("Enter your password: ")
   users = []
   passwords = []
   
   with open('userdata.txt','r') as f:
       for line in f:
            fields = line.split(',')
            users.append(fields[0])
            passwords.append(fields[1])
            letIn = False
            
       for user in users:
            if username == users and user_password == passwords:
                letIn = True
                main()
                break
                
            if not letIn:
                print("Incorrect username or password")
                login()
                

def launch():
    
    global planet
    planet = input("What planet would you like to go to:  ")
    print(f"Launch into {planet} has started........")
    time.sleep(1)
    print("Preparing for liftoff.....")
    time.sleep(1)
    print("T-minus 3....")
    time.sleep(1)
    print("T-minus 2......")
    time.sleep(1)
    print("T-minus 1.....")
    time.sleep(2)
    print("Liftoff.......")
    time.sleep(3)
    
    outcome = ["yes","no"]
    dice_toss = random.choice(outcome)
    if dice_toss == "yes":
        print(f"Launch Mission to {planet} was successful!!")
        writesuccess(planet)
    else: 
        print("Launch Mission Unsuccessful.....")
        main()
        
def writesuccess(planet):
    with open("success.txt", "a") as file:
        file.write(f"{planet} \n")
    print("Success recorded.....")

def success():
    with open("success.txt", "r") as sc:
        successes = sc.readlines()
    return successes
    

login()

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if user_choice == "":
        display_text("1. Launch", 100, 50)
        display_text("2. View Successes", 100, 100)
        display_text("3. Quit", 100, 150)
       

    elif user_choice == "1":
        launch()
        

    elif user_choice == "2":
        successes = success()
        y = 50
        for line in successes:
            display_text(line, 100, y)
            y += 50

    elif user_choice == "3":
        running = False

    # Update the display
    pygame.display.flip()

pygame.quit()