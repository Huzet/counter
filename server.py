from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'password'


@app.route('/')
def home():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] = int(session['counter']) + int(1)
    print(session)
    return(render_template('index.html'))


@app.route('/destroy_session')
def destroy():
    session['counter'] = 0
    return(redirect('/'))


@app.route('/add_two')
def add_two():
    session['counter'] = int(session['counter']) + int(1)
    return(redirect('/'))


if __name__ == "__main__":
    app.run(debug=True)
