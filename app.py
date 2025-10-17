from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from src.chatbot import Chatbot

# Initialize FastAPI app
app = FastAPI()

# Link templates and static folders
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize your chatbot
bot = Chatbot()

# Home route - loads the chat webpage
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

# Chat route - handles user messages
@app.post("/get")
async def get_bot_response(user_message: str = Form(...)):
    """
    This route is called when the user sends a message from the webpage.
    FastAPI receives it, passes it to the chatbot, and returns the reply.
    """
    try:
        bot_reply = bot.get_response(user_message)
        return JSONResponse(content={"response": bot_reply})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
