from flask import Flask, render_template, url_for
from flask import Flask, render_template, url_for
import user as userDetails
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    user = userDetails
    # if userDetails():
        # return render_template('home.html', user=userDetails)

    return render_template('login.html', user=userDetails)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html', user=userDetails)

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


        