from flask import Flask, render_template, request, redirect, url_for, session
from decimal import Decimal, InvalidOperation
import sqlite3

# Create a Flask instance
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management


# Connect to SQLite3 database (or create it if it doesn't exist)
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (username TEXT PRIMARY KEY, password TEXT, age INTEGER)''')
    conn.commit()
    conn.close()


# Home page route
@app.route('/')
def home():
    return render_template('home.html')


# Register page route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        age = request.form['age'].strip()
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password, age) VALUES (?, ?, ?)", (username, password, age))
        conn.commit()
        conn.close()
        return redirect(url_for('login'))
    return render_template('register.html')


# Login page route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            session['username'] = user[0]
            session['age'] = user[2]
            return redirect(url_for('welcome'))
        else:
            return 'Invalid credentials'
    return render_template('login.html')


# Welcome page route
@app.route('/welcome')
def welcome():
    if 'username' in session:
        username = session['username']
        age = session['age']
        return render_template('welcome.html', username=username, age=age)
    else:
        return redirect(url_for('login'))

    # Calculator page route


# Calculator page route

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    error = None  # Initialize an error variable to handle errors gracefully

    if request.method == 'POST':
        try:
            # Convert input values to Decimal for precise calculations
            num1 = Decimal(request.form['num1'])
            num2 = Decimal(request.form['num2'])
            operator = request.form['operator']

            # Perform the calculation based on the operator
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    error = "Error: Division by zero is undefined"
            else:
                error = "Invalid operator"
        except InvalidOperation:
            error = "Invalid input: Please enter valid numbers."
        except Exception as e:
            error = f"An error occurred: {str(e)}"

    return render_template('calculator.html', result=result, error=error)


# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


# Initialise the database and run the app
if __name__ == '__main__':
    init_db()
    app.run(port=5000, debug=True)