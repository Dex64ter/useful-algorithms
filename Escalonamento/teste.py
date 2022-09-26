
import random

l = ["Ola", "eu", "sou", "seu", "amiguinho"]

ma = list(range(len(l)))

while ma:
    o = random.choice(ma)
    print(l[o])
    ma.remove(o)