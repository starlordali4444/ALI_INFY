import time
def tryit1():
    for i in range(1,1000000):
        x=time.strftime("%d/%m/%Y")
            
t = time.time()
tryit1()
print('duration:', time.time()-t)