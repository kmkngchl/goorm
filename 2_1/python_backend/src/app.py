from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>서버가 작동 중입니다!</h1><p>성공이에요.</p>"

if __name__ == '__main__':
    app.run(port=5000)
