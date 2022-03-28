from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/dojo')
def dojo():
    return 'Dojo!'


if __name__== "__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode. after True add a comma and list another port number if some port number already is in usage
