from flask import Flask, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (important if calling from GitHub Pages)

# Simple homepage
@app.route('/')
def home():
    return render_template_string("""
    <h1>Hello from Flask!</h1>
    <p>This is a sample Flask app you can embed in your GitHub Pages site.</p>
    <p>Try the <a href="/api/hello">API endpoint</a>.</p>
    """)

# Example API route
@app.route('/api/hello')
def hello_api():
    return jsonify(message="Hello from the Flask API!")

if __name__ == '__main__':
    app.run(debug=True)