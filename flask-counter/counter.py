from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '12345'

@app.route("/")
def counter():
    if 'count' in session:
        session['count'] += 1
        print(session['count'])
        return render_template('index.html', count = session['count'])
    else:
        session['count'] = 0
        print(session['count'])
        return render_template("index.html", count = session['count'])

@app.route("/reset", methods = ['POST'])
def reset():
    session.pop('count')
    return redirect('/')

@app.route("/add_two", methods = ['POST'])
def addTwo():
    session['count'] += 1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
