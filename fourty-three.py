from flask import Flask
import os

app = Flask(__name__)

@app.route('/home')
def ex43_home(): return "Index Page"

@app.route('/user/<username>')
def ex44_user(username): return f"User Page for {username}"

# ... 底下依此類推放 ex45~ex48 ...

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
