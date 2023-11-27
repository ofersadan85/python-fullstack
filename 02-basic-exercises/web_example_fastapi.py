# pip install fastapi uvicorn
import fastapi

app = fastapi.FastAPI()


@app.get("/")  # Main site page
async def main_page():
    return "Hello World"


# Run with: uvicorn <filename>:app
