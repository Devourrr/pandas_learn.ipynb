data = [1,2,3]
newdata = []

for x in data:
    newdata.append(x*10)

print(newdata)

import numpy as np

data = [1,2,3,4,5]
arr = np.array(data)
print(arr)

high = [97200,92400,92100,94300,92300]
low = [90000,91100,91700,92100,90900]

arr_high = np.array(high)
arr_low = np.array(low)

arr_dif = arr_high - arr_low

print(arr_dif)


for i in range(10):
    print(i, end='')

import matplotlib.pyplot as plt
import numpy as np
import time

start = time.time()

dice = np.random.choice(6,1000000)

end = time.time()
print(end - start)

plt.hist(dice, bins=6)
plt.show()


print(np.arage(10))