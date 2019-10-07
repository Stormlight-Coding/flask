from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '12345'

@app.route("/")
def home():
    if session.get('test'):
        print(session['test'])
        return render_template('home.html')
    else:
        return render_template('home.html')

@app.route("/checkout", methods = ['POST'])
def checkout():
    strawberries = int(request.form['strawberries'])
    raspberries = int(request.form['raspberries'])
    apples = int(request.form['apples'])
    bananas = int(request.form['bananas'])
    name = request.form['name']
    id = request.form['id']
    total = strawberries + bananas + raspberries + apples

    return render_template('checkout.html', strawberries = strawberries, raspberries = raspberries, apples = apples, bananas = bananas, name = name, id= id, total= total)

@app.route('/show', methods = ['POST'])
def show():
    print(request.form)
    session['test']= request.form['test']
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
