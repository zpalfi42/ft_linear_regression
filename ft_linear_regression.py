"""_summary_
"""

import sys
import os
from predict import predict
from train import train_model


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menu():
    clear_screen()
    print("Please choose an option:")
    print("1. Predict Car Price")
    print("2. Train Model")
    print("3. Exit")

def main():
    while True:
        menu()
        response = input("\nEnter your choice: ")

        if response == "1":
            clear_screen()
            print("You selected **Predict Car Price**")
            while True:
                response = input("\nPlease enter the mileage of the car in KM: ")
                try:
                    mileage = int(response)
                    predict(mileage)
                    input("\nPress Enter to continue...")
                    break
                except  ValueError:
                    print("Please enter a correct number!")
        elif response == "2":
            clear_screen()
            train_model()
            input("\nPress Enter to continue...")
            break
        elif response == "3":
            sys.exit()
        else:
            print("Incorrect choice!")

if __name__ == "__main__":
    main()