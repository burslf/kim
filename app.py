
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()
  
@app.post('/generate_messages')
async def run_app(request: Request):
    return {"messages": "hello my man !"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6262)
