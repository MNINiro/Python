def health(age,apple_ate,smoked):
       condition=(100-age)+(apple_ate * 3.5)-(smoked * 2)
       print(condition)
       

my_data=[47,20,0]

health(my_data[0], my_data[1],my_data[2])

# unpacking

health(*my_data)
