# Netcat

A modern, web-based netcat alternative built with Python and Flask. Designed as an educational project for application security.

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone or download the repository**
   ```bash
   git clone https://github.com/osfadsec/netcat.git
   cd netcat
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Mac/Linux
   # OR
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the web interface**
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

### Quick Start (Optional)

**Mac/Linux:**
```bash
chmod +x run.sh
./run.sh
```

**Windows:**
```bash
run.bat
```

## Usage

### TCP Connect
Connect to a remote host and send data through an active connection.

1. Click the **"TCP Connect"** tab
2. Enter target hostname or IP address
3. Enter the target port number
4. Set connection timeout (default: 5 seconds)
5. Click **"Connect"**
6. Once connected, send messages through the active session
7. Click **"Close"** to disconnect

**Example:**
- Host: `example.com`
- Port: `80`
- Timeout: `5`

### TCP Listen
Listen for incoming connections on a local port.

1. Click the **"TCP Listen"** tab
2. Enter a local port number (1024-65535)
3. Set listen timeout (default: 30 seconds)
4. Click **"Start Listening"**
5. The application will wait for an incoming connection
6. Once a client connects, you can send data
7. Click **"Close"** to disconnect

**Example:**
- Port: `9999`
- Timeout: `30`

**Testing:** From another terminal, run:
```bash
nc localhost 9999
```

### Port Scanning
Scan ports on a target host to identify open services.

1. Click the **"Port Scan"** tab
2. Enter target hostname or IP address
3. Specify ports in the format: `20-25,80,443,8000-8010`
4. Set timeout per port (default: 2 seconds)
5. Click **"Start Scan"**
6. View results showing open, closed, and error ports

**Port Format Examples:**
- Single port: `80`
- Port range: `20-25`
- Multiple ports: `80,443,22`
- Mixed format: `22,80,443,8000-8010`
- Common ports: `20-25,53,80,443,3306,5432,8080`

## Technical Details

### Backend (app.py)
- Flask web framework for HTTP handling
- REST API with JSON request/response
- Input validation for security
- Error handling with informative messages
- WSGI application for deployment

### Core Module (netcat_core.py)
- Python socket programming
- TCP connection management
- Port scanning with timeout protection
- Thread-safe connection tracking
- Resource cleanup on close

### Frontend (HTML/CSS/JavaScript)
- Responsive web design
- Tab-based navigation
- Real-time API communication
- Mobile-first approach

## Security Considerations

### Implemented
- ✅ Input validation (port ranges, host validation)
- ✅ Timeout protection (prevents hanging)
- ✅ Error messages without system details
- ✅ Thread-safe operations with locks
- ✅ Proper socket cleanup
- ✅ No hardcoded secrets

### Recommendations for Production
- 🔒 Add TLS/SSL support for encrypted connections
- 🔒 Implement authentication mechanisms
- 🔒 Add rate limiting and DOS protection
- 🔒 Enable HTTPS for web interface
- 🔒 Add comprehensive logging and auditing
- 🔒 Run behind a reverse proxy (Nginx, Apache)

## Troubleshooting

### "Address already in use" error
The port 5000 is already in use.

**Solution:**
```bash
# Find and kill the process
lsof -i :5000
kill -9 <PID>

# Or change the port in app.py
app.run(debug=True, host='127.0.0.1', port=5001)
```

### "ModuleNotFoundError: No module named 'flask'"
Flask is not installed.

**Solution:**
```bash
pip install -r requirements.txt
```

### Connection timeout errors
The target host is not reachable.

**Solutions:**
- Verify the host address is correct
- Check your internet connection
- Ensure the target service is running
- Increase the timeout value

### Dark mode button not working
JavaScript code not loaded.

**Solution:**
- Clear browser cache
- Refresh the page (Ctrl+F5)
- Check browser console for errors (F12)

## Educational Value

This project demonstrates:

### Network Programming
- Socket creation and management
- TCP/IP protocol fundamentals
- Port scanning techniques
- Connection handling and cleanup

### Web Development
- Flask framework usage
- REST API design patterns
- Frontend-backend communication
- HTML/CSS/JavaScript integration

### Application Security
- Input validation techniques
- Error handling best practices
- Resource management
- Thread safety
- Secure coding practices

### Software Engineering
- Code organization and structure
- Version control with Git
- Documentation best practices
- Responsive design principles

## System Requirements

- **Python:** 3.7 or higher
- **RAM:** 50MB minimum
- **Disk:** 10MB for installation
- **Browser:** Modern browser (Chrome, Firefox, Safari, Edge)
- **OS:** Windows, macOS, Linux