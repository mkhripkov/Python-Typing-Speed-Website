from flask import Flask
app = Flask(__name__)

# Landing page
@app.route('/')
@app.route('/home')
def home():
    return "Hello World!"

# About Page
@app.route('/about')
def about():
    return "Hello About Page!"

if __name__ == '__main__': # Allows us to run the script directly with Python
    app.run(debug=True)