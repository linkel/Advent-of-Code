import collections
import matplotlib.pyplot as plt
from blist import blist

with open('input.txt', 'r') as f:
    data = f.read()

res = [i for i in data.splitlines()]

print(res)

# do I want five variables all storing the pot and the LLPRR configuration?
# or can I do this with a stack?
