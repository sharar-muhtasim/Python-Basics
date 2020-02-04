#Generates a random range and then generates random numbers based on the range
import random
z = random.randrange(5)
print('The range is ' + str(z))
for i in range(z):
    print(random.randint(1,10))
