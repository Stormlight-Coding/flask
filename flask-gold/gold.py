from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = '12345'

@app.route("/")
def home():
    if 'gold' in session:
        return render_template("index.html", gold = session['gold'], earnings = session['earnings'], activity = session['activity'])
    else:
        session['gold'] = 0
        session['earnings'] = 0
        session['activity'] = []
        return render_template("index.html")

@app.route("/process", methods = ['POST'])
def find():
    if request.form['find'] == "farm":
        session['earnings'] = random.randint(10,20)
        session['gold'] += session['earnings']
        session['activity'].append("Went to the Farm and earned " + str(session['earnings']) + " gold")
        print("went to Farm")
        return redirect('/')
    elif request.form['find'] == "cave":
        session['earnings'] = random.randint(5,10)
        session['gold'] += session['earnings']
        session['activity'].append("Went to the Cave and earned " + str(session['earnings']) + " gold")
        print("went to cave")
        return redirect('/')
    elif request.form['find'] == "house":
        session['earnings'] = random.randint(10,20)
        session['gold'] += session['earnings']
        session['activity'].append("Went to the House and earned " + str(session['earnings']) + " gold")
        print("went to house")
        return redirect('/')
    elif request.form['find'] == "casino":
        roll = random.randint(5,50)
        pos_neg = random.randint(0,1)
        if pos_neg == 1:
            session['gold'] += roll
            session['earnings'] = roll
            session['activity'].append("Went to the Casino and earned " + str(session['earnings']) + " gold")
        else:
            session['gold'] -= roll
            session['earnings'] = -roll
            session['activity'].append("Went to the Casino and lost " + str(session['earnings']) + " gold")
        print("went to casino")
        return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
    session['gold'] = 0
    session['earnings'] = 0
    session['activity'] = []
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)


# if request.form['which_form'] == 'register':
#   //do registration process
# elif request.form['which_form'] == 'login':
#   //do login process
