"""_summary_
"""

import sys
import os
from LinearRegressionModel import LinearRegressionModel


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
    print("3. Plot Data")
    print("4. Exit")

def main():
    model = LinearRegressionModel()
    model.clear_model()
    try:
        while True:
            menu()
            response = input("\nEnter your choice: ")

            if response == "1":
                clear_screen()
                print("You selected **Predict Car Price**")
                while True:
                    response = input("\nPlease enter the mileage of the car in KM: ")
                    try:
                        if not response.strip():
                            raise ValueError
                        mileage = int(response)
                        if mileage < 0:
                            raise ValueError
                        if mileage > sys.float_info.max:
                            raise ValueError
                        model.predict(mileage)
                        input("\nPress Enter to continue...")
                        break
                    except  ValueError:
                        print("Please enter a correct number!")
            elif response == "2":
                clear_screen()
                model.train(lr=0.01, n_iter=10000)
                input("\nPress Enter to continue...")
            elif response == "3":
                model.plot()
            elif response == "4":
                sys.exit()
            else:
                print("Incorrect choice!")
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()