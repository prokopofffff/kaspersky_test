from fastapi import FastAPI
import os
import time

app = FastAPI()

@app.get("/api/docs")
def getDocs():
    pass

@app.post("/api/start_pn")
def start():
    pid = os.fork()
    if pid:
        print('Child process id:', pid)
        pi = ""
        with open("pi.txt", "r") as file:
            pi = file.readline()
        for i in range(0, len(pi) - 6, 6):
            print(pi[i : i + 6], end = '')
            time.sleep(1)
    else:
        print('Can\'t run a process')


@app.post("/api/stop_pn")
def stop():
    pass

@app.get("/api/pn")
def status():
    pass

@app.get("/api/pn/result")
def result():
    pass