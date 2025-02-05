import sys
from LinearRegressionModel import LinearRegressionModel

if __name__ == "__main__":
    model = LinearRegressionModel()
    while True:
        response = input("Please enter the mileage of the car in KM: ")
        try:
            if not response.strip():
                raise ValueError
            mileage = int(response)
            if mileage < 0:
                raise ValueError
            if mileage > sys.float_info.max:
                raise ValueError
            model.predict(mileage)
            break
        except  ValueError:
            print("Please enter a correct number!")