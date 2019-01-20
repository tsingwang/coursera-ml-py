import matplotlib.pyplot as plt
import pandas as pd


def plot_data(x, y):
    # ===================== Your Code Here =====================
    # Instructions : Plot the training data into a figure using the matplotlib.pyplot
    #                using the "plt.scatter" function. Set the axis labels using
    #                "plt.xlabel" and "plt.ylabel". Assume the population and revenue data
    #                have been passed in as the x and y.

    # Hint : You can use the 'marker' parameter in the "plt.scatter" function to change the marker type (e.g. "x", "o").
    #        Furthermore, you can change the color of markers with 'c' parameter.


    # ===========================================================

    plt.scatter(x, y, marker='x', color='r', label='Training Data')
    plt.xlabel('Population of City in 10,000s')
    plt.ylabel('Profit in $10,000s')
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv('ex1data1.txt', names=['population', 'profit'])
    plot_data(df.population, df.profit)
