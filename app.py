import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello welcome to kirabo's API!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 8080))
  app.run(debug=True,host='0.0.0.0',port=port)
