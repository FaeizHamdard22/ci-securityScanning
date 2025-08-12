from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hi , I am Faeiz Hamdard a student in herat uni...."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
