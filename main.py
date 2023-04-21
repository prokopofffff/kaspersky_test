from fastapi import FastAPI
import os
import time

app = FastAPI()

pid = -1

@app.get("/api/docs")
def getDocs():
    pass

@app.post("/api/start_printpi")
def start():
    if pid == -1:
        pid = os.fork()
        if pid:
            print('Child process id:', pid)
            pi = ""
            with open("pi.txt", "r") as file:
                pi = file.readline()
            for i in range(0, len(pi) - 6, 6):
                print(pi[i : i + 6], end = '')
                time.sleep(1)
            pid = -1
        else:
            print("Can't run a process")
    else:
        print("Can't run a process")


@app.post("/api/stop_printpi")
def stop():
    if pid != -1:
        os.kill(pid, 0)
    else:
        print("Process has already stopped")


@app.get("/api/status_printpi")
def status():
    if pid == -1:
        return "Not launched"
    else:
        return "Launched"

@app.get("/api/pn/result")
def result():
    if pid != -1:
        pass
    else:
        pass