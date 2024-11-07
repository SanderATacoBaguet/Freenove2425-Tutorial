import time

print("Raspberry pi pico initialization completed !")

while True:
    print("Running time : ", time.time()%60,"s")
    time.sleep(1)