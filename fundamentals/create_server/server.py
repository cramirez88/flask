from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def print(name):
    return f'Hi {name.capitalize()}'

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num, name):
    return f'{num * name}'

@app.errorhandler(404)
def pageNotFound():
    return "Sorry! No response. Try again."


if __name__== "__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  
  # Run the app in debug mode. after True add a comma and list another port number if some port number already is in usage
