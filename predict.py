def predict(mileage: int, theta0: int = 0, theta1: int = 0):
    estimatedPrice = theta0 + theta1*mileage
    print(f"\nThe predicted price for a car with {mileage}km of mileage is {estimatedPrice}")
    return estimatedPrice

if __name__ == "__main__":
    try:
        open("theta.val")
    except  FileNotFoundError:
        print("There is no theta file! Default values of theta would be assigned...")
    while True:
        response = input("Please enter the mileage of the car in KM: ")
        try:
            mileage = int(response)
            predict(mileage)
            break
        except  ValueError:
            print("Please enter a correct number!")