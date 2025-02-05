from LinearRegressionModel import LinearRegressionModel

if __name__ == "__main__":
    model = LinearRegressionModel()
    model.train(lr=0.01, n_iter=10000)