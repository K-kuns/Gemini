import numpy as np
import matplotlib.pyplot as plt

# Create a NumPy array
data = np.array([10, 20, 30, 40, 50])

# Print the array
print("Array:", data)

# Calculate and print the mean
mean_value = np.mean(data)
print("Mean value:", mean_value)

# Multiply every element by 2
doubled = data * 2
print("Doubled array:", doubled)

# Create an array of x values from 0 to 2π
x = np.linspace(0, 2 * np.pi, 100)

# Calculate the sine of each x value
y = np.sin(x)

# Plot the sine wave
plt.plot(x, y, label='sin(x)', color='blue')

# Add labels and title
plt.title('Sine Wave Example')
plt.xlabel('x values')
plt.ylabel('sin(x)')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
