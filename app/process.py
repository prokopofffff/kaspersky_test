import time

start = time.time()
with open('app/pi.txt', 'r') as file:
    pi = file.readline()
    for i in range(0, len(pi) - 6, 6):
        print(pi[i : i + 6], end = '')
        time.sleep(1)
end = time.time()
print()
print(str(end - start) + " секунд")