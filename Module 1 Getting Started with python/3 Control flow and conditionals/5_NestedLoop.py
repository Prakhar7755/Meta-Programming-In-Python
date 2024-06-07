import time
start_time = time.time()

for i in range(10):

    for j in range(10):

        print(j+1, end="\t")

    print("")

print(round(time.time()-start_time, 100))
