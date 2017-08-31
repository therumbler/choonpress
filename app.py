from flask import Flask
from choonpress.utilities import get_config

app = Flask(__name__)

config = get_config()

@app.route('/')
def index():
    return 'in'

def main():
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    main()

