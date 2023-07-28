from flask import Flask, render_template
app = Flask(__name__)

# Landing page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html', title='About')

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

if __name__ == '__main__': # Allows us to run the script directly with Python
    app.run(debug=True)