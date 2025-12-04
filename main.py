from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Abanime Flask server is running!"

# Vercel ko sirf 'app' object chahiye, isliye yaha pe
# if __name__ == "__main__": wala part zaroori nahi hai.
