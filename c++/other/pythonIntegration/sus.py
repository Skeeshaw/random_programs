import random

mapsize = 20

for i in range(5):
    random.seed(i)
    print(i, [random.randint(1,3)
              for i in range(mapsize)])