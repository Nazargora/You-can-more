from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy credentials
USERNAME = "hack"
PASSWORD = "hack"

# Route for the login page
@app.route('/')
def login():
    return render_template('login.html')

# Route to handle login form submission
@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']

    if username == USERNAME and password == PASSWORD:
        return redirect(url_for('welcome'))
    else:
        return redirect(url_for('bad_credentials'))

# Route for the welcome page (successful login)
@app.route('/welcome')
def welcome():
    return "<h1>Welcome!</h1>"

# Route for the error page (bad credentials)
@app.route('/bad_credentials')
def bad_credentials():
    return "<h1>Error 505: Bad Credentials</h1>", 505

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


