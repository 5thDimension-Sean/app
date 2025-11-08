from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 4000))  # Render provides the PORT in env
    app.run(host="127.0.0.1", port=port, debug=True)