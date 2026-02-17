from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    """Serve the secure comms grid application"""
    return render_template('index.html')

@app.route('/health')
def health():
    """Health check endpoint"""
    return {'status': 'ok'}, 200

if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True, host='0.0.0.0', port=5000)
