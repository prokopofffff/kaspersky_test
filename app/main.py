from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import os
import subprocess

app = FastAPI()

cmd = "systemctl start Bluetooth.service"
pid = -1
process = ""
flag = False

@app.get("/api/docs")
def getDocs():
    return RedirectResponse("/docs")

'''
@app.post("/api/start")
def start():
    try:
        process = subprocess.Popen(cmd.split(), stdout = subprocess.PIPE)
        pid = process.pid
        print('Child process id:', pid)
        flag = True
    except Exception as ex:
        return "Can't run a process"
'''

@app.post("/api/start")
def start():
    try:
        process = subprocess.Popen(cmd.split(), stdout = subprocess.PIPE)
        pid = process.pid
        print('Child process id:', pid)
        flag = True
    except Exception as ex:
        return "Can't run a process"


@app.post("/api/stop")
def stop():
    try:
        os.getpgid(pid)
        os.kill(pid, 0)
    except Exception as ex:
        return "Process has already stopped"


@app.get("/api/status")
def status():
    try:
        os.getpgid(pid)
        return "Not launched"
    except Exception as ex:
        return "Launched"

@app.get("/api/pn/result")
def result():
    if flag:
        return process.stdout
    else:
        return "404 Not Found"