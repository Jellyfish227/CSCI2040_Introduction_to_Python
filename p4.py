import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['axes.titlepad'] = 20

# Sales data
sales = {'Apple': 35, 'Banana': 42, 'Orange': 28, 'Grape': 17, 'Strawberry': 32}

# Define custom colors for each fruit
colors = ['lightgreen', 'yellow', 'orange', 'mediumpurple', 'pink']  # Colors matching the fruits

if __name__ == '__main__':
    # Create figure with specific size
    plt.figure(figsize=(10, 8))
    
    # Create pie chart with custom colors
    plt.pie(sales.values(),  # values
           labels=sales.keys(),  # labels
           autopct='%1.1f%%',  # show percentages
           colors=colors)      # custom colors
    
    # Add title with padding
    plt.title("Daily Sales Record", pad=20)
    
    # Save and show the plot
    plt.savefig('pie.png')
    plt.show()
    plt.close()