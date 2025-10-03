import random

def play():
    print("\n \n \n*****Welcome to number guessing game*****")
    print("please choose the deficulty level")
    print("1. easy (1-100) 10 attempts")
    print("2. mediam(1-100) 7 attempts")
    print("3. hard (1-199) 7 attempts")

    try:
        num= int(input("Enter the deficulty level: "))

        if num == 1:
            num = random.randint(1,100)
            attempt = 10
        elif num == 2:
            num = random.randint(1,100)
            attempt = 7
        elif num == 3:
            num = random.randint(1,199)
            attempt = 7
        
    except ValueError:
        print("invalid value set deficulty to mediam")
        num = random.randint(1,100)
        attempt = 7
    count = 0

    while count < attempt:
        try:
            guess = int(input("Enter your guess: "))

            count += 1

            if guess > num:
                print("little bit lower")
            elif guess < num:
                print("little bit greater")
            else:
                print(f"conreats  you guessed the correct number {num} in {count+1} attempts")
                break
            

        except ValueError:
            print("please enter a valid number.")
            continue
        
    else:
        print(f"you have used all your {attempt} attempts.")

while True:
    play()
    again = input("do you want to play again (yes/no)").lower()
    if again != "yes":
        print("thank you for playing")
        break