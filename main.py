from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Link to your raw GitHub JSON
DB_URL = "https://raw.githubusercontent.com/dedindeed/stigma-api/refs/heads/main/database.json"

@app.route('/')
def home():
    return "Stigma API is Running"

@app.route('/api/scripts')
def get_scripts():
    try:
        response = requests.get(DB_URL)
        return jsonify(response.json())
    except:
        return jsonify({"error": "Failed to fetch database"})

if __name__ == "__main__":
    app.run()
