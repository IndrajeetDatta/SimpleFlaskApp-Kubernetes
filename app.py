from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    image_path = request.args.get('image_path')
    return render_template('index.html', image_path=image_path)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
