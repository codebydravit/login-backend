from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Hardcoded credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "password"

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return {"status": "success", "message": "Login successful"}
    else:
        return JSONResponse(status_code=401, content={"status": "error", "message": "Invalid credentials"})
