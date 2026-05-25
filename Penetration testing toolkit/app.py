from flask import Flask, render_template, request, jsonify

from modules.port_scanner import scan_ports
from modules.vuln_scanner import scan_website
from modules.password_checker import check_password_strength
from modules.osint_tool import gather_osint

import webbrowser

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# PORT SCANNER

@app.route('/portscan', methods=['POST'])
def portscan():

    data = request.get_json()

    target = data.get('target')

    result = scan_ports(target)

    return jsonify(result)

# VULNERABILITY SCANNER

@app.route('/vulnscan', methods=['POST'])
def vulnscan():

    data = request.get_json()

    url = data.get('url')

    result = scan_website(url)

    return jsonify(result)

# PASSWORD CHECKER

@app.route('/passwordcheck', methods=['POST'])
def passwordcheck():

    data = request.get_json()

    password = data.get('password')

    result = check_password_strength(password)

    return jsonify(result)

# OSINT TOOL

@app.route('/osint', methods=['POST'])
def osint():

    data = request.get_json()

    domain = data.get('domain')

    result = gather_osint(domain)

    return jsonify(result)

if __name__ == '__main__':

    webbrowser.open('http://127.0.0.1:5000')

    app.run(debug=True)