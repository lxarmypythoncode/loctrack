from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Get the user's IP address
    ip_address = requests.get('https://api.ipify.org').text
    # Get location information based on IP address
    response = requests.get(f'https://ipinfo.io/{ip_address}/json')
    location_data = response.json()

    return render_template('index.html', location=location_data)

if __name__ == "__main__":
    app.run(debug=True)