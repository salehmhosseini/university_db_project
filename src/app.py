from flask import Flask, request , render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login_page_pooya.html')



@app.route('/user_recovery_pass.html')
def recovery_pass():
    return render_template('user_recovery_pass.html')


@app.route('/StNo_and_pass_recovery.html')
def recovery_st_num():
    return render_template('StNo_and_pass_recovery.html')
    
if __name__ == '__main__':
    app.run()
