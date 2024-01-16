import socket

from app import app
from app.adapters.vulnerabilities_adapter import take_latest_json, run_analysis
from app.core.interfaces.home_interface import render_main_page

ip_address = socket.gethostbyname(socket.gethostname())

@app.route('/')
def home():
    return render_main_page()

@app.route('/vulnerabilidades')
def vulnerabilities_route():
    return take_latest_json()

if __name__ == '__main__':
    run_analysis()
    app.run(host='0.0.0.0')
    print(f"La aplicación se está ejecutando en http://{ip_address}:5000/")