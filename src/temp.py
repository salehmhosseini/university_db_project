from flask import Flask, request , render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login_page_pooya.html')

if __name__ == '__main__':
    app.run()
