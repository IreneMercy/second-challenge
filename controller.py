from flask import Flask, render_template, url_for
from flask import request
import user as userDetails
user_credentials = {}

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_process', methods=['GET', 'POST'])
def login_process():
    username = request.values['Username']
    password = request.values['Password']
    if username in user_credentials.keys():
        if password ==  user_credentials[username][2]:
            return render_template('home.html')
        else:
            return render_template('login_failed.html')
    else:
        return render_template('not_found.html')
 

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html' )

@app.route('/signup_process', methods=['GET', 'POST'])
def signup_process():
    name = request.values['Name']
    username = request.values['Username']
    email = request.values['Email']
    password = request.values['Password']

    user_credentials[username] = (name, email, password)

    return render_template('login.html')

     




@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/work')
def work():
    return render_template('work.html')

@app.route('/adventure')
def adventure():
    return render_template('adventure.html')

@app.route('/destination')
def destination():
    return render_template('destination.html')

@app.route('/family')
def family():
    return render_template('family.html')

@app.route('/school')
def school():
    return render_template('school.html')

@app.route('/wishes')
def wishes():
    return render_template('wishes.html')

@app.route('/landing')
def landing():
    return render_template('landing.html')

if __name__ == "__main__":
    app.run(debug = True)


        