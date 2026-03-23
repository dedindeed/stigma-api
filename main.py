from flask import Flask, request, jsonify

app = Flask(__name__)

# This variable holds the script until Roblox asks for it
queued_script = ""

@app.route('/api/execute', methods=['POST'])
def execute():
    global queued_script
    data = request.json
    queued_script = data.get("script", "")
    print(f"Received Script: {queued_script}")
    return jsonify({"status": "ok"}), 200

@app.route('/api/get_script', methods=['GET'])
def get_script():
    global queued_script
    # Send the script to Roblox and then clear the queue
    temp = queued_script
    queued_script = "" 
    return jsonify({"script": temp}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
