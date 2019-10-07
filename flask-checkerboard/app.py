from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<x>/<y>/<color1>/<color2>')
def home(x,y,color1, color2):
    print(x)
    print(y)
    return render_template('index.html', width = int(x), height = int(y), color1 = color1, color2 = color2)

if __name__ == "__main__":
    app.run(debug = True)
