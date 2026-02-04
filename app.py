from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

DATAMUSE_API_URL = "https://api.datamuse.com/words"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find', methods=['POST'])
def find_synonyms():
    data = request.get_json()
    word = data.get('word')
    
    if not word:
        return jsonify({'error': 'Word is required'}), 400

    # Sanitize input: Remove special characters, keep letters, numbers, and spaces
    import re
    word = re.sub(r'[^a-zA-Z0-9\s]', '', word).strip()
    
    if not word:
         return jsonify({'error': 'Invalid word format'}), 400

    try:
        # Query Datamuse API for synonyms (rel_syn) with a 5-second timeout
        response = requests.get(DATAMUSE_API_URL, params={'rel_syn': word}, timeout=5)
        response.raise_for_status()
        results = response.json()
        
        # Extract just the words
        synonyms = [item['word'] for item in results]
        
        # Requirement: Max 10 synonyms
        synonyms = synonyms[:10]
        
        return jsonify({'synonyms': synonyms})
    except requests.RequestException as e:
        return jsonify({'error': f'Failed to fetch synonyms: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
