import time

with open('../kaspersky_test/ap/pi.txt', 'r') as file:
    pi = file.readline()
    for i in range(0, len(pi) - 6, 6):
        print(pi[i : i + 6], end = '')
        time.sleep(1)