# Generate random numbers with fixed seed
import numpy as np
np.random.seed(42)
random_numbers = np.random.normal(1 , 0.25 , 100)
import matplotlib.pyplot as plt

if __name__ == '__main__':
    plt.figure(figsize=(10, 6))

    plt.hist(random_numbers, bins=30, density=True)
    plt.title('Histogram of Random Numbers')
    plt.xlabel('Random Numbers')
    plt.ylabel('Probability Density')


    # Save the figure
    plt.savefig('histogram.png')
    # Show the plot
    plt.show()
    plt.close()
