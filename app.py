# Importing essential libraries
from flask import Flask, render_template, request
import os
from src.util import *

# Initialize Flask application
app = Flask(__name__, template_folder='templates', static_folder='static')

# Define environment variable
env = os.getenv("run_env", "dev")

# Set base URL based on environment
if env == "dev":
    BASE_URL = "http://localhost:5000/"
elif env == "prod":
    BASE_URL = "google.com"

# To handle home page
@app.route('/')
def home():
    return render_template('index.html')

# To handle prediction page
@app.route('/prediction')
def prediction():
    # Get questions from util module (assuming this function exists)
    questions = get_questions()
    return render_template('prediction.html', questions=questions)


# To handle form submission and evaluation
@app.route('/evaluate', methods=['POST'])
def evaluate():
    if request.method == 'POST':
        # Evaluate questions using request data (assuming this function exists)
        final_results = evaluate_questions(request)
        return render_template('results.html', final_results=final_results)

@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
	app.run(debug=True)

