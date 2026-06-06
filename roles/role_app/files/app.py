from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello():
    return f"Hello! Debug mode is {app.config['DEBUG']}"

@app.route('/api/health')
def health():
    return "OK"

@app.route('/api/db-config')
def db_config():
    return {
        'host': app.config['DB_HOST'],
        'user': app.config['DB_USER'],
        'database': app.config['DB_NAME']
    }

if __name__ == '__main__':
    app.run(host='BIND_IP', port=app.config['PORT'], debug=app.config['DEBUG'])
