from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("index.html")

@app.route('/play/<x>')
def play_num(x):
    return render_template('play.html', times = int(x))

@app.route('/play/<x>/<color>')
def change(x, color):
    return render_template('change.html', times = int(x), color = color)

if __name__ == "__main__":
    app.run(debug=True)
