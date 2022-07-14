from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"Data": "value"}

if __name__ == "__main__":
    # Use this for debugging purposes only

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
