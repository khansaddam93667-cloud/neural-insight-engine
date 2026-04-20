from flask import Flask, send_file, request, jsonify
import os
from dotenv import load_dotenv

# Load environment variables from .env file (if it exists)
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the main neural_hub.html page."""
    # Assuming neural_hub.html is in the same directory as app.py
    return send_file('neural_hub.html')

@app.route('/api/research', methods=['POST'])
def deep_research_vector():
    """Placeholder endpoint for the Deep Research Vector search bar."""
    data = request.get_json()

    # In a real application, you would access the API_KEY like this:
    # api_key = os.environ.get("API_KEY")

    query = data.get('query', '') if data else ''

    return jsonify({
        "status": "success",
        "message": f"Received research query: {query}",
        "data": {
            "results": [
                {"id": 1, "title": "Placeholder Result 1", "snippet": "This is a placeholder result for the query."},
                {"id": 2, "title": "Placeholder Result 2", "snippet": "More placeholder data."}
            ]
        }
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
