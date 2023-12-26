from fastapi import FastAPI
import aichat 

app = FastAPI()

@app.post("/chat")
async def read_root(message: str, user: str, channel: str):
    return aichat.chatmessage(message, user, channel)

@app.get("/test")
async def read_root():
    return "endpoint ok"

if __name__ == "__main__":
   app.run(host="0.0.0.0",port = 8080)
