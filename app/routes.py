from app import app  # Make sure you're importing the app instance correctly

@app.route('/')
def home():
    return "Hello, World!"
