from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Python ini berjalan di Render, ditulis oleh H Gunarto!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

# print("Hello from Render!")
