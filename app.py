from flask import Flask, request, jsonify
from wakeonlan import send_magic_packet

app = Flask(__name__)

@app.route('/wake_on_lan', methods=['POST'])
def wake_on_lan():
    macid = request.json.get('macid')
    if not macid:
        return jsonify({"error": "MAC ID is required"}), 400
    
    try:
        send_magic_packet(macid)
        return jsonify({"message": f"Wake-on-LAN packet sent to {macid}"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
