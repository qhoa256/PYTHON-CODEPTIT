from flask import Flask, render_template, request, redirect, flash
import csv
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Check if the username already exists in DB.csv
        with open('database.csv', 'r', newline='') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if row[0] == username:
                    flash('Tài khoản đã tồn tại', 'error')
                    return redirect('/register')

        # If the username doesn't exist, add the user to DB.csv
        with open('database.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([username, password, email])
            flash('Đăng ký thành công', 'success')
        return redirect('/login')
    return render_template('register.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password match in DB.csv
        with open('database.csv', 'r', newline='') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if row[0] == username and row[1] == password:
                    flash('Thông tin đăng nhập đúng', 'success')
                    return redirect('/feedback')
        flash('Sai thông tin đăng nhập', 'error')
    return render_template('login.html')

# Route for the feedback page
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    username = request.args.get('username')
    if username:
        if request.method == 'POST':
            feedback_text = request.form['feedback']

            # Save feedback to feedback.csv
            with open('feedback.csv', 'a', newline='') as feedback_file:
                feedback_writer = csv.writer(feedback_file, delimiter=';')
                feedback_writer.writerow([username, feedback_text, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])

    return render_template('feedback.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
