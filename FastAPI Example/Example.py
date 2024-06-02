from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


# Simple Endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Simple GET Endpoint
@app.get("/items")
def read_item(item1, item2, item3):
    return {"item1": item1,
            "item2": item2,
            "item3": item3}

# Simple Endpoint with HTML Response
@app.get("/html")
def read_html():
    html = """<html><body>Welcome</body></html>"""
    return HTMLResponse(content=html, status_code=200)
