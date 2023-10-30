import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
# Set the seed for reproducibility
np.random.seed(0)

# Parameters for the distribution
mean = 65
std_dev = 6

# Generate a sample of retirement ages
retirement_ages = np.random.normal(mean, std_dev, 10000)

# Since the distribution is left-skewed, we'll "clip" the ages at 40 and 50
retirement_ages = np.clip(retirement_ages, 40, None)

# Plot the histogram of retirement ages
plt.hist(retirement_ages, bins=30, edgecolor='black')
plt.title('Retirement Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
