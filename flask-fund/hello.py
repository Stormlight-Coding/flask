# from flask import Flask  # Import Flask to allow us to create our app
# app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world():
#     return "This is the beginning of how to use Flask!  Hooray!!! #jobhunt2019 #pleasehireme"  # Return the string 'Hello World!' as a response
# if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
#     app.run(debug=True)    # Run the app in debug mo

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') #The function following the route rule is associated with the corresponding route!!!
def hello_world():
    return 'Hello World'

@app.route('/success')
def success():
    return "Success"

@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello " + name.capitalize()

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/John')
def say():
    return "Hi John!"

@app.route('/repeat')
def repeat():
    return "Dog " * 90

@app.route('/index')
def index():
    return render_template("index.html", phrase = "hello", times = 5)

@app.route('/lists')
def render_lists():
    student_info = [
        {'name': 'Michael', 'age': 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template('lists.html', random_numbers = [3,1,5], students = student_info)

@app.route('/table')
def name_table():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template('table.html', users = users)

if __name__ == '__main__':
    app.run(debug=True)
