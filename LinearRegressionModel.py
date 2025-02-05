import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class   LinearRegressionModel:
    def __init__(self):
        try:
            self.load_model("model.val")
        except FileNotFoundError:
            print("There is no theta file! Default values of theta would be assigned...")
            self.theta0 = 0.0
            self.theta1 = 0.0
            self.mean_km = 0
            self.std_km = 1
            self.mean_price = 0
            self.std_price = 1      

    def load_data(self, file: str):
        try:
            data = pd.read_csv(file)
            if len(data) < 2:
                print("The data file does not contain enough data! Please provide a correct data file...")
                return None, None
            data['km'] = [float(i) for i in data['km']]
            data['price'] = [float(i) for i in data['price']]
            if np.any(data['km'] < 0) or np.any(data['price'] < 0):
                print("The data file contains negative values! Please provide a correct data file...")
                return None, None
            km = data['km'].values
            prices = data['price'].values
            return km, prices
        except FileNotFoundError:
            print("There is no data file! Please provide a data file...")
            return None, None
        except:
            print("The data file is not in the correct format! Please provide a correct data file...")
            return None, None
    
    def load_model(self, file: str):
        if os.path.exists(file):
            with open(file, 'r') as f:
                self.theta0 = float(f.readline().strip())
                self.theta1 = float(f.readline().strip())
                self.mean_km = float(f.readline().strip())
                self.std_km = float(f.readline().strip())
                self.mean_price = float(f.readline().strip())
                self.std_price = float(f.readline().strip())
        else:
            self.theta0 = 0.0
            self.theta1 = 0.0
            self.mean_km = 0
            self.std_km = 1
            self.mean_price = 0
            self.std_price = 1
    
    def predict(self, mileage: int):
        normalized_mileage = (mileage - self.mean_km) / self.std_km
        normalized_price = self.theta0 + self.theta1 * normalized_mileage
        estimated_price = normalized_price * self.std_price + self.mean_price
        print(f"\nThe predicted price for a car with {mileage}km of mileage is {estimated_price}")
        return estimated_price
    
    def save_model(self, file: str):
        with open(file, 'w') as f:
            f.write(f"{self.theta0}\n{self.theta1}\n{self.mean_km}\n{self.std_km}\n{self.mean_price}\n{self.std_price}\n")

    def normalize(self, values):
        mean = np.mean(values)
        std = np.std(values)
        return (values - mean) / std, mean, std
    
    def train(self, lr: float, n_iter: int):
        km, prices = self.load_data("data.csv")
        if km is None or prices is None:
            return

        km, self.mean_km, self.std_km = self.normalize(km)
        prices, self.mean_price, self.std_price = self.normalize(prices)
        m = len(km)

        for _ in range(n_iter):
            temp_theta0 = lr * (1/m) * np.sum(self.theta0 + self.theta1*km - prices)
            temp_theta1 = lr * (1/m) * np.sum((self.theta0 + self.theta1*km - prices) * km)
            self.theta0 -= temp_theta0
            self.theta1 -= temp_theta1

        self.save_model("model.val")

    def plot(self):
        km, prices = self.load_data("data.csv")
        if km is None or prices is None:
            return
        
        plt.scatter(km, prices, color='blue', label='Data points')
        km_normalized = (km - self.mean_km) / self.std_km
        prices_normalized = self.theta0 + self.theta1 * km_normalized
        prices_predicted = prices_normalized * self.std_price + self.mean_price
        plt.plot(km, prices_predicted, color='red', label='Regression line')
        plt.xlabel('Mileage (km)')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

    def clear_model(self):
        model_file = "model.val"
        if os.path.exists(model_file):
            os.remove(model_file)
            self.load_model("mode.val")