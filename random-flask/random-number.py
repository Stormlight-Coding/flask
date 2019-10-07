from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'abcd'

@app.route("/")
def randomHome():
    if 'number' in session:
        print(session['number'])
        return render_template('index.html', guess = session['guess'], number = session['number'])
    else:
        session['number'] = random.randint(1,100)
        return render_template('index.html')

@app.route('/guess', methods = ['POST'])
def guess():
    if int(request.form['guess-number']) == session['number']:
        session['guess'] = int(request.form['guess-number'])
        print('you guessed right!')
        return redirect('/')
    else:
        if int(request.form['guess-number']) > session['number']:
            session['guess'] = int(request.form['guess-number'])
            print('too high')
            return redirect("/")
        else:
            session['guess'] = int(request.form['guess-number'])
            print("too low")
            return redirect("/")

@app.route('/play-again', methods = ['POST'])
def playAgain():
    session.pop('number')
    session.pop('guess')
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
