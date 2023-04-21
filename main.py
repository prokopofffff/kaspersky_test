from fastapi import FastAPI

app = FastAPI()

@app.get("/api/docs")
def getDocs():
    pass

@app.post("/api/start_pn")
async def start():
    pass

@app.post("/api/stop_pn")
async def stop():
    pass

@app.get("/api/pn")
def status():
    pass

@app.get("/api/pn/result")
def result():
    pass