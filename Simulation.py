# Develop a python program to model the populations of rabbits and foxes in an Inhabitat. Use the following information.
# 1. Foxes eat rabbits.
# 2. Foxes die of starvation if they don't eat enough rabbits.
# 3. Rabbits and foxes both reproduce, but rabbit reproduces faster.
# 4. Rabbits and foxes both die of other causes.

import matplotlib.pyplot as plt

# Initial population of rabbits and foxes
rabbits = 100
foxes = 20

# Time steps for the simulation
time_steps = 50

# Lists to store the populations at each time step
rabbit_population = []
fox_population = []

for i in range(time_steps):
    rabbit_population.append(rabbits)
    fox_population.append(foxes)

    # Foxes eat rabbits
    if rabbits > foxes:
        rabbits -= foxes
    else:
        rabbits = 0
        foxes = 0

    # Foxes die of starvation if they don't eat enough rabbits
    if foxes > 0 and rabbits == 0:
        foxes -= 1

    # Rabbits reproduce
    rabbits += rabbits // 10
    # Foxes reproduce
    foxes += foxes // 20

    # Rabbits and foxes die of other causes
    rabbits -= rabbits // 100
    foxes -= foxes // 100

# Plot the populations over time
plt.plot(rabbit_population, label='Rabbits')
plt.plot(fox_population, label='Foxes')
plt.xlabel('Time Steps')
plt.ylabel('Population')
plt.legend()
plt.show()
