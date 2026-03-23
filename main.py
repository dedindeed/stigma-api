from flask import Flask, request, jsonify

app = Flask(__name__)

# This variable stores the script in the cloud memory
queued_lua_code = ""

@app.route('/')
def home():
    return "Stigma API is Online!", 200

# DOOR 1: Your Python UI sends code HERE
@app.route('/api/execute', methods=['POST'])
def receive_script():
    global queued_lua_code
    data = request.get_json()
    
    if data and "script" in data:
        queued_lua_code = data["script"]
        print(f"Cloud received script: {queued_lua_code[:30]}...")
        return jsonify({"status": "ok", "msg": "Script stored in Cloud"}), 200
    
    return jsonify({"status": "error", "msg": "No script data"}), 400

# DOOR 2: Roblox pulls the code from HERE
@app.route('/api/get_script', methods=['GET'])
def give_script():
    global queued_lua_code
    # Send the code to Roblox and then clear it so it doesn't loop
    response_code = queued_lua_code
    queued_lua_code = "" 
    return jsonify({"script": response_code}), 200

if __name__ == "__main__":
    # Render uses port 10000 by default
    app.run(host="0.0.0.0", port=10000)
