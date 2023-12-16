from flask import Flask, render_template, request, redirect, url_for
import time;

app = Flask(__name__)

# Trang chủ
@app.route('/')
def home():
    return render_template('index.html')

# Trang Đăng ký
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        if not is_username_taken(username):
            save_user(username, password, email)
            return redirect(url_for('login'))
        else:
            return "Tài khoản đã tồn tại!"
    
    return render_template('register.html')

# Trang đăng nhập
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if is_valid_login(username, password):
            return "Thông tin đăng nhập đúng!"
        else:
            return "Sai thông tin đăng nhập!"
    
    return render_template('login.html')

# Trang phản hồi
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        username = request.form['username']
        feedback_text = request.form['feedback']
        
        if is_username_taken(username):
            localtime = time.localtime(time.time())
            save_feedback(username, feedback_text, localtime)
            return "Phản hồi đã được gửi!"
        else:
            return "Bạn phải đăng nhập để gửi phản hồi!"
    
    return render_template('feedback.html')

def is_username_taken(username):
    with open('DB.csv', 'r') as file:
        for line in file:
            stored_username = line.split(';')[0]
            if username == stored_username:
                return True
    return False

def save_user(username, password, email):
    with open('DB.csv', 'a') as file:
        file.write(f"{username};{password};{email}\n")

def is_valid_login(username, password):
    with open('DB.csv', 'r') as file:
        for line in file:
            stored_username, stored_password, _ = line.split(';')
            if username == stored_username and password == stored_password:
                return True
    return False

def save_feedback(username, feedback_text, localtime):
    with open('feedback.csv', 'a') as file:
        file.write(f"{username};{feedback_text};{localtime}\n")

if __name__ == '__main__':
    app.run(debug=True)