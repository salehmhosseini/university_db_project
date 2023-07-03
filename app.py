from flask import Flask, request , render_template , redirect ,url_for
import sqlite3



app = Flask(__name__)

@app.route('/')
def login():
    return render_template('landing_page.html')

@app.route('/login_page.html', methods=['GET', 'POST'])
def login_page():
    global username
    if request.method == 'POST':
        
        # Establish a connection to the SQLite database
        conn = sqlite3.connect('portal_pooya.db')
        cursor = conn.cursor()
        username = request.form['username']
        password = request.form['password']
        captcha = request.form['captcha']
        
        
          # Execute the SQL query to check if the username and password exist in the table
        cursor.execute("SELECT * FROM student_info WHERE uername=? AND password=?", (username, password))
        row = cursor.fetchone()
        
        if row is None:
            # Redirect to the signup page
            return render_template('login_page.html', alert_message='Invalid username or password.')
        
        elif int(captcha) != 44655:
            # Display an alert message
            return render_template('login_page.html', alert_message='Invalid captcha.')
        
        else:
            return redirect(url_for('student_page', username=username))

    
    return render_template('login_page.html')
                           
@app.route('/user_recovery_pass.html')
def recovery_pass():
    return render_template('user_recovery_pass.html')


@app.route('/StNo_and_pass_recovery.html')
def recovery_st_num():
    return render_template('StNo_and_pass_recovery.html')

@app.route('/signup_menue.html')
def signup_menu():
    return render_template('signup_menue.html')

@app.route('/student_signup.html' , methods=['GET', 'POST'])
def st_singup():
    if request.method == 'POST':
        
        first_name = request.form['first_name']
        last_name =  request.form['last_name']
        email =  request.form['email']
        national_code =  request.form['national_code']
        mobile =  request.form['mobile']
        gender =  request.form['gender']
        category =  request.form['category']
        entry_year =  request.form['entry_year']
        user_name =  request.form['user_name']
        password =  request.form['password']
        
        # Connect to the SQLite database
        conn = sqlite3.connect('portal_pooya.db')

        # Create a cursor object to execute SQL commands
        cursor = conn.cursor()

        # Define the SQL query
        sql = '''INSERT INTO student_info (national_code,first_name, last_name, email,mobile, gender, category, entry_year, uername, password)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

        # Define the parameter values for the query
        params = (national_code, first_name ,last_name, email , mobile, gender, category, entry_year, user_name, password)

        # Execute the query
        cursor.execute(sql, params)

        # Commit the transaction
        conn.commit()

        # Close the database connection
        conn.close()
        
        
        return redirect(url_for('login_page'))
        
    return render_template('student_signup.html')

@app.route('/proffesor_signup.html')
def prof_signup():
    return render_template('proffesor_signup.html')


@app.route('/student_page.html')
def student_page():
    return render_template('student_page.html')



def get_student_info(username):
    conn = sqlite3.connect('portal_pooya.db')
    cursor = conn.cursor()

    # Fetch student information by username
    cursor.execute("SELECT * FROM student_info WHERE uername=?", (username,))
    student_info = cursor.fetchall()
    
    conn.close()
    return student_info
    
    
@app.route('/student_info_read.html')
def student():
    student_info = get_student_info(username)
    return render_template('student_info_read.html', username=username, student_info=student_info)


    conn.close()
    return student_info

@app.route('/class_time.html')
def class_time():
    return render_template('class_time.html')

@app.route('/student_info_read.html')
def student_info_read():
    return render_template('student_info_read.html')


    
if __name__ == '__main__':
    app.run()
