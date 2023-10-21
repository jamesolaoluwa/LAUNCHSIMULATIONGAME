import random
import time

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
    with open("success.txt","a") as file:
        file.write(f"{planet} \n")
        print("Success recorded.....")
        time.sleep(1)
        main()

def success():
    with open("success.txt","r") as sc:
        for line in sc: 
            print(line)
    time.sleep(1)
    main()
    

login()
    
            
        

     
        
        
        

        

        

        
        

        
        
        