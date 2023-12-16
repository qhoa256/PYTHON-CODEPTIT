from flask import Flask, render_template, request, redirect, url_for,flash,get_flashed_messages
import time;

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'your_secret_key_here'

# Trang chủ
@app.route('/')
def home():
    return render_template('index.html')

# Trang đăng ký
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        # Kiểm tra xem tài khoản đã tồn tại hay chưa
        if not is_username_taken(username):
            save_user(username, password, email)
            flash('Đăng ký thành công', 'success')
            return redirect(url_for('login'))
        else:
            flash("Username đã tồn tại !!!",'error')
            return redirect(url_for('register'))
    
    return render_template('register.html')

# Trang đăng nhập
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if is_valid_login(username, password):
            flash('Đăng nhập thành công', 'success')
            return redirect(url_for('home'))
        else:
            flash('Đăng nhập thất bại', 'error')
            return redirect(url_for('login'))
    
    return render_template('login.html')


# Kiểm tra xem tài khoản đã tồn tại hay chưa
def is_username_taken(username):
    with open('DataBase.txt', 'r') as file:
        for line in file:
            stored_username = line.split(';')[0]
            if username == stored_username:
                return True
    return False

# Lưu thông tin người dùng vào DataBase.txt
def save_user(username, password, email):
    with open('DataBase.txt', 'a') as file:
        file.write(f"{username};{password};{email}\n")

# Kiểm tra xem thông tin đăng nhập có hợp lệ hay không
def is_valid_login(username, password):
    with open('DataBase.txt', 'r') as file:
        for line in file:
            stored_username, stored_password, _ = line.split(';')
            if username == stored_username and password == stored_password:
                return True
    return False

def save_feedback(username, feedback_text, localtime):
    with open('feedback.txt', 'a') as file:
        file.write(f"{username};{feedback_text};{localtime}\n")

if __name__ == '__main__':
    app.run(debug=True)