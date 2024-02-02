from flask import Flask, render_template

app = Flask(__name__,template_folder='templates',static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("3000"), debug=False)
