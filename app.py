"""
Main Flask application for Netcat web interface
"""
from flask import Flask, render_template, request, jsonify
from netcat_core import NetcatCore
import json

app = Flask(__name__)
netcat = NetcatCore()

@app.route('/')
def index():
    """Render the main web interface"""
    return render_template('index.html')

@app.route('/api/connect', methods=['POST'])
def connect():
    """Establish a TCP connection to a remote host"""
    try:
        data = request.json
        host = data.get('host')
        port = int(data.get('port'))
        timeout = int(data.get('timeout', 5))

        if not host or not port:
            return jsonify({'error': 'Host and port are required'}), 400

        result = netcat.connect(host, port, timeout)
        return jsonify(result)
    except ValueError as e:
        return jsonify({'error': f'Invalid input: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Connection failed: {str(e)}'}), 500

@app.route('/api/listen', methods=['POST'])
def listen():
    """Start listening on a local port"""
    try:
        data = request.json
        port = int(data.get('port'))
        timeout = int(data.get('timeout', 30))

        if not port:
            return jsonify({'error': 'Port is required'}), 400

        result = netcat.listen(port, timeout)
        return jsonify(result)
    except ValueError as e:
        return jsonify({'error': f'Invalid input: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Listen failed: {str(e)}'}), 500

@app.route('/api/scan', methods=['POST'])
def scan_ports():
    """Scan ports on a target host"""
    try:
        data = request.json
        host = data.get('host')
        ports = data.get('ports')  # e.g., "20-25,80,443"
        timeout = int(data.get('timeout', 2))

        if not host or not ports:
            return jsonify({'error': 'Host and ports are required'}), 400

        result = netcat.scan_ports(host, ports, timeout)
        return jsonify(result)
    except ValueError as e:
        return jsonify({'error': f'Invalid input: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Scan failed: {str(e)}'}), 500

@app.route('/api/send', methods=['POST'])
def send_data():
    """Send data through an active connection"""
    try:
        data = request.json
        connection_id = data.get('connection_id')
        message = data.get('message')

        if not connection_id or message is None:
            return jsonify({'error': 'Connection ID and message are required'}), 400

        result = netcat.send_data(connection_id, message)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': f'Send failed: {str(e)}'}), 500

@app.route('/api/close', methods=['POST'])
def close_connection():
    """Close an active connection"""
    try:
        data = request.json
        connection_id = data.get('connection_id')

        if not connection_id:
            return jsonify({'error': 'Connection ID is required'}), 400

        result = netcat.close_connection(connection_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': f'Close failed: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
