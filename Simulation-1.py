# Develop a program to model the populations of rabbits and foxes in inhabitat. Use the following information to help you.
# Foxes eat rabbits.
# Foxes die of starvation if they don't eat enough rabbits.
# Rabbits and foxes both reproduce, but rabbit reproduces faster.
# Rabbits and foxes both die of other causes.


# This program simulates the populations of rabbits and foxes in an inhabitat over a period
# of 10 years. Each year, it calculates the number of rabbits that are eaten by the foxes
# (based on the starvation threshold of 10 rabbits per fox per year), the number of foxes
# that die of starvation, the number of rabbits and foxes that die of other causes, and the
# number of new rabbits and foxes born. It then prints the population numbers for each year.
# Note that this is a simplified model and there could be other factors that could affect the
# population of rabbits and foxes in reality.

import random

# Initial populations
rabbit_population = 100
fox_population = 50

# Reproduction rates (per year)
rabbit_reproduction_rate = 0.1
fox_reproduction_rate = 0.05

# Mortality rates (per year)
rabbit_mortality_rate = 0.05
fox_mortality_rate = 0.1

# Starvation threshold (number of rabbits needed per fox per year)
starvation_threshold = 10

# Number of years to simulate
years = 10

for year in range(1, years + 1):
    # Calculate number of rabbits eaten by foxes
    rabbits_eaten = min(rabbit_population, fox_population * starvation_threshold)
    rabbit_population -= rabbits_eaten
    fox_population -= rabbits_eaten / starvation_threshold

    # Calculate number of foxes dying of starvation
    fox_starvation_deaths = max(0, fox_population - (rabbit_population / starvation_threshold))
    fox_population -= fox_starvation_deaths

    # Calculate number of rabbits and foxes dying of other causes
    rabbit_deaths = rabbit_population * rabbit_mortality_rate
    rabbit_population -= rabbit_deaths
    fox_deaths = fox_population * fox_mortality_rate
    fox_population -= fox_deaths

    # Calculate number of new rabbits and foxes born
    new_rabbits = rabbit_population * rabbit_reproduction_rate
    rabbit_population += new_rabbits
    new_foxes = fox_population * fox_reproduction_rate
    fox_population += new_foxes

    # Print population numbers for current year
    print(f"Year {year}: Rabbits: {rabbit_population}, Foxes: {fox_population}")
