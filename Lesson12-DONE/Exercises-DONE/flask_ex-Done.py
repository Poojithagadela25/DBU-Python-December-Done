# app.py

# Import necessary modules from the Flask package
from flask import Flask, request, redirect, url_for, abort

# Create an instance of the Flask class
app = Flask(__name__)

# --------------------
# Ex1. Exercise 1: URL Building and Redirection
# Objective:
# Create a route /redirect-me that redirects the user to the homepage /. Use the url_for function to build the URL dynamically.
# 
# Instructions:
# 	•	Import the redirect and url_for functions from flask.
# 	•	Define a new route /redirect-me.
# 	•	Inside the view function, use url_for('hello_world') to get the URL for the homepage.
# 	•	Use redirect() to redirect the user to the homepage.
# --------------------

# Route for redirecting to homepage
@app.route('/redirect-me')
def redirect_me():
    # Use url_for to get the URL for the 'home' route dynamically and redirect
    return redirect(url_for('home'))  # Redirecting to the home route using url_for


# --------------------
# Exercise 2: Exercise: Conditional Redirection Based on User Input
# Objective:
#
# Create a route that accepts user input via query parameters and redirects the user to different pages based on that input.
#
# Instructions:
#	1.	Create the /process Route:
#	•	Define a route /process that will handle the user input.
#	•	Use the request.args object to retrieve the query parameter named choice.
#	2.	Implement Conditional Logic:
#	•	If choice is 'dashboard', redirect the user to the /dashboard route.
#	•	If choice is 'profile', redirect the user to the /profile route.
#	•	If choice is any other value or not provided, redirect the user to the homepage /.
#	3.	Use Redirection Functions:
#	•	Utilize the redirect() and url_for() functions from Flask to perform the redirections.
#	•	Ensure that the code is clean and includes detailed comments explaining each step.
#	4.	Define Target Routes:
#	•	Make sure the /dashboard, /profile, and / routes are defined and return a simple message indicating the page.
# --------------------

@app.route('/process')
def process_choice():
    # Retrieve the 'choice' parameter from the query string
    choice = request.args.get('choice')
    
    # Check the value of 'choice' and redirect accordingly
    if choice == 'dashboard':
        # Redirect to the 'dashboard' route
        return redirect(url_for('dashboard'))
    elif choice == 'profile':
        # Redirect to the 'profile' route
        return redirect(url_for('profile'))
    else:
        # Redirect to the 'home' route if 'choice' is invalid or not provided
        return redirect(url_for('home'))

# Route for the dashboard page
@app.route('/dashboard')
def dashboard():
    return 'Welcome to your dashboard!'

# Route for the profile page
@app.route('/profile')
def profile():
    return 'This is your profile page.'

# Route for the homepage
@app.route('/')
def home():
    return 'Welcome to the homepage!'

if __name__ == '__main__':
    app.run(debug=True)
    