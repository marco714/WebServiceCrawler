from app import app
import uvicorn

if __name__ == "__main__":

    uvicorn.run("debug_server:app", host='127.0.0.1', port=5000, reload=True)